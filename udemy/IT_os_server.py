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

# url변경하기

url = "https://www.udemy.com/api-2.0/discovery-units/all_courses/?p=1&page_size=16&subcategory=&instructional_level=&lang=&price=&duration=&closed_captions=&subs_filter_type=&subcategory_id=138&source_page=subcategory_page&locale=ko_KR&currency=krw&navigation_locale=en_US&skip_price=true&sos=ps&fl=scat"

res = requests.get(url) #비동기통신방식 get방식으로 호출되는 url을 response 변수로 나는 가져올거야
res.encoding = 'UTF-8' # UTF-8 지원하는 방식으로 한글 가능
result=json.loads(res.text) # 호출해서 가져온 url 내용을 text로 가져오면서 json형태로 변환해서 result에 넣을거야

# url 카테고리에 붙여줄 메인 사이트
site_url = "https://www.udemy.com"

# 페이지 자동 변환을 위한 코드
page_url1 = "https://www.udemy.com/api-2.0/discovery-units/all_courses/?p="
page_url2 = "&page_size=16&subcategory=&instructional_level=&lang=&price=&duration=&closed_captions=&subs_filter_type=&subcategory_id=138&source_page=subcategory_page&locale=ko_KR&currency=krw&navigation_locale=en_US&skip_price=true&sos=ps&fl=scat"


# < 페이지 크롤링 코드 - (IT - 운영체제 및 서버) 131p>

lecture_title = [] # 강의명
lecture_url = [] # url
lecture_instructor = [] # 강사명
lecture_rating = [] # 별점
lecture_cou_rating = [] # 별점 수
lecture_num_subscriber = [] # 수강생 수
lecture_total = [] # 강의 수
lecture_total_time = [] # 강의 총 시간


for i in range(1, 132):
    page_url = page_url1+str(i)+page_url2
    page_res = requests.get(page_url)
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
        
# print(lecture_title, "\n\n", len(lecture_url), "\n\n", len(lecture_instructor),"\n\n", len(lecture_rating),
#       "\n\n",len(lecture_cou_rating),"\n\n", len(lecture_num_subscriber),"\n\n", len(lecture_total),"\n\n",len(lecture_total_time))

lecture_list = pd.DataFrame(zip(lecture_title,lecture_url,lecture_instructor,lecture_rating,lecture_cou_rating,lecture_num_subscriber,lecture_total,lecture_total_time),
                            columns=['강의명','url','강사명','별점','별점 수','수강생 수','강의 수','강의 총 시간'])
#print(lecture_list)
lecture_list.to_csv("IT_os_server.csv", index=False)