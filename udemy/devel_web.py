from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import json
import requests
import pandas as pd

def get_chrome_driver():
      chrome_options = webdriver.ChromeOptions()
      
      driver = webdriver.Chrome(
          service=Service(ChromeDriverManager().install()),
          options=chrome_options
      )
      return driver
  


#url = "https://www.udemy.com/courses/development/web-development/?p=1"

#여기서 p=1&page 이 부분, 숫자를 올리면 페이지가 변경되어 자료 수집이 가능하다. -> for문을 이용해서 크롤링이 끝나면 페이지를 넘겨준다.
#세부계획은 하단에
#문제: 첫번째 강의는(items)으로 나오며, 그 이후 강의들은 curriculum_items으로 나온다.
#-> 그러면 items수집 할 때 두 가지로 나누어서 (둘 다 써서) 수집한다. (두 번쓰기), ex) items에서 한 번, curriculum_items 한 번
# 그래서 조건을 걸어주어야한다. 일단 조건 걸기 전에 필요한것은?
# 필요한 것: 
# 중복되는 것들이 있는데 엘리먼트 형식도 아님. 
# items는 하나다. 그렇다면 if items가 있다면

# <목표 - 페이지에서 내용물 뽑아내기> 
# 1번. items에서 ~ 들을 뽑아내겠다. 그리고 curriculum_items에서 ~ 들을 뽑아낸다. 
# 2번. 이 두 작업이 끝나면 페이지를 넘기고 다시 1번을 반복한다(x- items다시x). 끝 페이지까지 반복한다. ( 페이지 수를 지정해야하는가? 이러면 강의가 늘어나면 추후 관리 문제?
# 페이지 수를 [:-1]까지 이런식으로는 못하나)

# items 만나면 이 작업을 실행하라, curriculum_items을 만나면 이 작업을 실행하고, 다시 curiculum을 만나면
# 위에 내용 다 불가 -> id를 기준점으로? 그리고 수집, 그 다음 id가 없으면 다음페이지로 ->

# 페이지 자동 변환을 위한 코드
url1 = "https://www.udemy.com/api-2.0/discovery-units/all_courses/?p="
url2 = "&page_size=16&subcategory=&instructional_level=&lang=&price=&duration=&closed_captions=&subs_filter_type=&subcategory_id=8&source_page=subcategory_page&locale=ko_KR&currency=krw&navigation_locale=en_US&skip_price=true&sos=ps&fl=scat"
#for i in range(1,4):
#    print(url1+str(i)+url2)
#여기서도 페이지가 한번에 바뀌면 안되니깐, 그렇다고 여기서만 계속 for를 달아가면서 할순없잖아?
    
###
# 처음 스크래이핑하려했으나 실패
#lectures = driver.find_elements(
#    By.CSS_SELECTOR,
#    "div:not(.course-card--image-wrapper--1F9ny) > h3" #div중에서 이미지 url을 제외하고 가져온다, 사진은 필요없음
#)
#print(len(lectures))
#
#for lec_text in lectures:
#    texts = lec_text.text
#    print(texts)
#    print(len(lectures))
#------------------------------

# 클래스화 해보았지만 일단은 제외
#page_crawling= PageCrawling()

#class PageCrawling:
#    def __init__(self):
#        driver = get_chrome_driver()
#        driver.get(url)
#        driver.implicitly_wait(time_to_wait=5) #5초 간 페이지 로딩 기다려주기
#        page_element = driver.find_element_by_xpath("/html/body/pre").text
#        driver.quit()
#        print(page_element)

# class PageCrawling:
#     def __init__(self):
#         driver = get_chrome_driver()
#         driver.get(url)
#         driver.implicitly_wait(time_to_wait=5) #5초 간 페이지 로딩 기다려주기
        
#         page_element = driver.find_element_by_xpath("/html/body/pre").text #find_element_by를 사용하여라? 버전때문?
#         dict(page_element) #딕셔너리 형태로 변환하고 싶었는데 변환이 안되네 -> 
#         print(page_element)
        
#         driver.quit()
# page_crawling = PageCrawling()
#--------------------------------

# 키워드 추출을 위한 str형태 - dict으로 변환을 위한 시도 -> 실패
#def d_page_element(**kwargs): #이걸 거치면 str-> None 타입으로 변경이 된다
#    print(type(page_element))
#print(type(d_page_element()))
#print(d_page_element())
#d_page_element(page_element)
#---------------------------

###############
#driver = get_chrome_driver()
#driver.get(url)
#driver.implicitly_wait(time_to_wait=5) #5초 간 페이지 로딩 기다려주기
#page_element = driver.find_element_by_xpath("/html/body").text
#driver.quit()
#print(page_element)

#j_page_element = json.loads(page_element)
# 변환 확인 - 성공
#print(j_page_element) -> 정상 데이터 추출
#print(type(j_page_element)) -> dict 형태로 나옴
#----------
# print(j_page_element[0]) -> 아무것도 안나옴

# print(j_page_element['unit'][0]) -> KeyError: 0
#-----
#k_j_page_element = j_page_element['unit']
#print(k_j_page_element) -> value 값 쭈욱 데이터 다 나옴
#-----

#values 값에서 빼오고 싶다 특정 키워드 들을, json 형태인 딕셔너리 형태긴 하지만 해당 특성을 이용하기가 어렵다?

#print(j_page_element.keys()) -> key 확인해보니 key가 하나로만(길이) 이루어져있음- 타고 타고 들어가본다?
#print("values값은 : ", len(j_page_element.values())) # values 값도 하나(길이)로만 이루어져있음-> 당연히 키 'unit'을 제외하고 다 나옴 

# 내가 원하는 자료들만 담는 작업이 필요할텐데 이를 어디에 담아두냐 -> 성공하면 셀레니움 이용하여 홈페이지를 변경해주어야한다.-> 이거 실행되는거확인함
# 그러면 변수 만들어서 거기에 자료를 담고, 그리고 해당 변수들을 합쳐두는 작업이 필요하다 -> 리스트 형태로 담아야 추후 합칠 때 좋음
# 그리고 나중에 불러와서 판다스를 이용하여 데이터프레임 형태로 만들어야한다
# 그러려면 .csv 파일 형태로 만들어야된다.


#print(result['unit']['items'][0]["visible_instructors"][1]['title']) # 강사가 여러명이면 데이터 혼잡? 그리고 다른 곳에도 모두 설정해야함

# def first_lecture():
#     print(result['unit']['items'][0]['title'])# 첫번째 제목
#     print(result['unit']['items'][0]['url']) # url - 나중에 ( + https://www.udemy.com/ )
#     print(result['unit']['items'][0]["visible_instructors"][0]['title']) # 강사이름
#     print(result['unit']['items'][0]["avg_rating_recent"]) # 별점
#     print(result['unit']['items'][0]["num_reviews"]) # 별점 참여자 수
#     print(result['unit']['items'][0]["num_subscribers"]) # 수강생 수 
#     print(result['unit']['items'][0]["num_published_lectures"]) # 강의 수 
#     print(result['unit']['items'][0]["content_info_short"]) # 강의 총 시간

# < 페이지 크롤링 코드 >

url = "https://www.udemy.com/api-2.0/discovery-units/all_courses/?p=1&page_size=16&subcategory=&instructional_level=&lang=&price=&duration=&closed_captions=&subs_filter_type=&subcategory_id=8&source_page=subcategory_page&locale=ko_KR&currency=krw&navigation_locale=en_US&skip_price=true&sos=ps&fl=scat"

res = requests.get(url) #비동기통신방식 get방식으로 호출되는 url을 response 변수로 나는 가져올거야
res.encoding = 'UTF-8' # UTF-8 지원하는 방식으로 한글 가능
result=json.loads(res.text) # 호출해서 가져온 url 내용을 text로 가져오면서 json형태로 변환해서 result에 넣을거야

site_url = "https://www.udemy.com"
page_url1 = "https://www.udemy.com/api-2.0/discovery-units/all_courses/?p="
page_url2 = "&page_size=16&subcategory=&instructional_level=&lang=&price=&duration=&closed_captions=&subs_filter_type=&subcategory_id=8&source_page=subcategory_page&locale=ko_KR&currency=krw&navigation_locale=en_US&skip_price=true&sos=ps&fl=scat"

# (개발 - 웹개발) 603p

lecture_title = [] # 강의명
lecture_url = [] # url
lecture_instructor = [] # 강사명
lecture_rating = [] # 별점
lecture_cou_rating = [] # 별점 수
lecture_num_subscriber = [] # 수강생 수
lecture_total = [] # 강의 수
lecture_total_time = [] # 강의 총 시간


for i in range(1, 604):
    page_url = page_url1+str(i)+page_url2 # url range로 숫자 대입해서 페이지 넘길 수 있도록 저장하기
    page_res = requests.get(page_url) # 난 페이지를 변경하면서 아래의 키워드들을 가져오고 싶어, 그러려면 페이지를 바꾸면서 가져와야해
    result = json.loads(page_res.text)
    for j in range(16):
        lecture_title.append(result['unit']['items'][j]['title'])
        lecture_url.append(site_url+result['unit']['items'][j]['url'])
        lecture_instructor.append(result['unit']['items'][j]["visible_instructors"][0]['title'])
        lecture_rating.append(result['unit']['items'][j]["avg_rating_recent"])
        lecture_cou_rating.append(result['unit']['items'][j]["num_reviews"])
        lecture_num_subscriber.append(result['unit']['items'][j]["num_subscribers"])
        lecture_total.append(result['unit']['items'][j]["num_published_lectures"])
        lecture_total_time.append(result['unit']['items'][j]["content_info_short"])
#        for k in range(1, 3): 여기서 다른 분류 페이지로 이동해 데이터 추출을 하려 하였지만 추후 관리 어려움으로 인해 따로 작성            
# print(len(lecture_title), "\n\n", len(lecture_url), "\n\n", len(lecture_instructor),"\n\n", len(lecture_rating),
#       "\n\n",len(lecture_cou_rating),"\n\n", len(lecture_num_subscriber),"\n\n", len(lecture_total),"\n\n",len(lecture_total_time))

lecture_list = pd.DataFrame(zip(lecture_title,lecture_url,lecture_instructor,lecture_rating,lecture_cou_rating,lecture_num_subscriber,lecture_total,lecture_total_time),
                            columns=['강의명','url','강사명','별점','별점 수','수강생 수','강의 수','강의 총 시간'])
#print(lecture_list)
lecture_list.to_csv("devel_web.csv", index=False)

#class_url3=""
#class_url4=""
# 여기서 id값이 변경되어야 함 - 이 url을 내가 적어서 그냥 넣는거말고, 리스트 형태로 분류 별 id를 저장해서 range로 돌릴수있을까



# id_lists = [8, 558, 10, 12, 14, 16, 18, 20, 362, 575]
#개발- [웹개발, 데이터과학, 모바일 개발, 프로그래밍언어, 게임개발, 데이터베이스설계및개발, 소프트웨어테스팅, 소프트웨어엔지니어링, 소프트웨어개발도구, 노코드개발]

# 첫번째 for문 위에 for문을 달아준다. 이것도 두번째 for문처럼 url을 쪼개고 거기에 id_lists를 차례대로 넣어준다
# 이러면 다 합쳐진다.

# 0.
# 이거 위에꺼 그냥 다 쓰는 방법
# 1.
# 이걸 클래스화 했다면 어땠을까? def foo(): 그 다음엔 for문 돌리고, 그리고 def foo(self, id)를 넣어서 url의 id에 지정하고,
# 그러면 id 값만 넣어주고 클래스를 분류별로 선언만 해주면 호출이 가능해진다

# 2. - > 이걸로 그리고 id_lists는 분류 별 id를 주석처리로 적어두자
# 3중 for문
# id를 리스트 형식으로 만들어 range 형식으로 url id에 각각 넣어주면서, range로 페이지를 넘길수있게, range로 인덱스를 바꾸며 데이터 수집








#"https://www.udemy.com/api-2.0/discovery-units/all_courses/?p=1&page_size=16&subcategory=&instructional_level
#=&lang=&price=&duration=&closed_captions=&subs_filter_type=&subcategory_id=8&source_page=subcategory_page&
#locale=ko_KR&currency=krw&navigation_locale=en_US&skip_price=true&sos=ps&fl=scat"


#"https://www.udemy.com/api-2.0/discovery-units/all_courses/?p=1&page_size=16&subcategory=&instructional_level
#=&lang=&price=&duration=&closed_captions=&subs_filter_type=&subcategory_id=558&source_page=subcategory_page&
#locale=ko_KR&currency=krw&navigation_locale=en_US&skip_price=true&sos=ps&fl=scat"

# 일단 전부 다 합쳐두게되면 나중에 다른 분들 사이트에서 가져온 내용과 합치기 어려울 수 있으니, 각 분류별로만 합쳐서 둔다
# 나중에 분류별로 되어있는것을 합치는 건 얼마 걸리지 않으니깐. li1+li2=li3 이런식이나, extend를 이용해서 list1.extend(list2) print(list1)이렇게. 
# id_lists = [1,2,3,4,5,6,7,8,9,10]
# for i in id_lists:
#   url