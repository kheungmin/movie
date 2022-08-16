import pandas as pd

df = pd.read_csv("devel_d_science.csv")

# 강의 총 시간 전처리
# hour, minute, question
h = 0
m = 0
q = 0
for idx, row in df.iterrows():
    t = row["강의 총 시간"]
    if "시간" in t:
        h += 1
    if "분" in t:
        m += 1
    if "질문" in t:
        q += 1

def time_cleaner(row):
    if "시간" in row:
        clean_time = float(row.replace("시간", "")) * 60
    elif "분" in row:
        clean_time = float(row.replace("분", ""))
    else:
        clean_time = None
    return clean_time

df['강의 총 시간'] = df['강의 총 시간'].apply(
    time_cleaner
)

# 별점 전처리
df["별점"]=df["별점"].round(1)


print(df.head())

df.to_csv("p_devel_d_science.csv", index=False)












#print(test1)
# 분과 시간이 각각 있음, 분은 분대로, 시간은 시간대로 모아서 데이터프레임으로 만들어주고,
# 분은 한글 '분'만 drop을 이용해서 -1
#test1=test1.replace("시간","")

#if test1.str[:-1] == '간':


# test1 = (str(test1))
# test1 = test1.replace("시간","")

#print(test1.str[:-2])
# 이것만 뺄 수 있는 작업을 내가 할 수 있다면 거기서 이미 연산을 했지

#test1=str(df_devel_d_science.str.replace(pat=r'시간|분', repl=r'', regex=True))
#print(test1) # 012를 제외하고 3,4가 출력된다

#print(test1)
# test1=str(test1[:-3:-1][::-1].str.replace(pat=r'시간|분', repl=r'', regex=True))
# print(test1) # 0,1,2를 제외하고 3,4가 출력된다 - 이건 시간만을 뽑아내기 위한 코드였기 때문. 근데 여기선 인덱스 기준으로 끝에 2곳만 나온것으로보인다.

#test1 이라는 다음에 인덱스가 아닌 슬라이싱으로 출력을 했기 때문. 그러면 문자를 자르고자한다면 str뒤에 붙여야되지 않을까해서 붙이니 pat오류
#--
#test1_1=str(test1.str.replace(pat=r'시간', repl=r'*60', regex=True)) # 이거 그냥 따로 빼서 df로 만들고, 정수형해서 60곱함
# 여기 시간은 없앤 거를 다시 한 번 정규식을 돌리면 되잖아. 그러면 어떻게 해야할까? - 한 번에 패턴 두가지넣어서 없애면 구분을 지을수가 없으니 시간먼저하고, 분을 친다
#test1_2=str(test1_1.replace(pat=r'분', repl=r'', regex=True))
#--
# 위에 *60에서 *을 문자형으로 받아들일것같음
# 예상이 맞았고, 그러면 시간에만 끝에 60을 붙여서 만들어주고, 일단 int형으로 변경을 한다. 그러면 연산이 가능해지고, 내가 다룰 수 있다
# 이 때 replace로 (문자형만가능)

 # 이것도 따로 빼서 정수형 만들고 위에꺼랑 합침 -> 잠깐! 그러면 기존에
#정렬되어있는 데이터 자료들이랑 다 어긋나버린다 -> 그러면 망함ㅜ 어떻게할것이냐 -> ? -> 원하는것만 변경하는게 가장 좋음
#-> 
#test1_1=(str(test1_1))
#print(test1_1, type(test1_1))
#print(test1_2, type(test1_2))
# test2_1=test1.str.replace(pat=r'분', repl=r'', regex=True)
# test2_1=str(test2_1)
# print(type(test2_1))
# print(test2_1)
# 별점--------------
# test_rating = df_devel_d_science["별점"].head()
# test_rating=test_rating.round(1)
# print(test_rating)
# # 별점 끝

#hour_or_minute_list = []

# list(test1) -> 이렇게하면 문자열로 비교가 불가능해져. 아닌가 한 인덱스를 볼 때마다 잘라서 보았을 때니깐 리스트로 해볼만하겠다

# test1=list(test1)
# print(type(test1))
#print(test1)
# 인덱스마다 끝에 두 글자 확인을 하려면 for문으로 인덱스를 돌아간다. 해당 인덱스의 끝에 두 글자만 확인
#print(test1[:-3:-1][::-1])

# def hour_or_minute(test1):
#     #print(test1[:-3:-1][::-1])
#     for i in test1:
#         print(i)
#         if i[:-3:-1][::-1] == '시간':
#             print(i[:-3:-1][::-1])
#             i = str(i)
#             print(type(i))
#             i=i.replace("시간","")
#             print(i)
#             i=float(i)*60
#             print(i)
#             hour_or_minute_list.append(i)
#         elif i[:-2:-1][::-1] == '분':
#             print(i[:-2:-1][::-1])
#             i = str(i)
#             print(type(i))
#             i = i.replace("분","")
#             hour_or_minute_list.append(i)
#         return test1
# print(hour_or_minute(test1))
# print(hour_or_minute_list)

#test1을 리스트화해서 넣어준다?


# def hour_or_minute(test1):
#     print(test1[:-3:-1][::-1])
#     for i in test1:
#         # print(test1[:-3:-1][::-1].text)
#         if i[:-3:-1][::-1] == '시간': #i.text?
#             print(i)
        #     i = str(i)
        #     print(type(i))
        #     i=i.replace("시간","")
        #     print(i)
        #     i=float(i)*60
        #     print(i)
        #     hour_or_minute_list.append(i)
        #     print(hour_or_minute_list)            
        # elif i[:-2:-1][::-1] == '분':
        #     i = str(i)
        #     print(type(i))
        #     i = i.replace("분","")
        #     hour_or_minute_list.append(i)
        # return test1
    # print(hour_or_minute_list)
# print(hour_or_minute_list)
# print(hour_or_minute("3시간"))
#append를 안해줬어 -> append를 해주어야함
#연산을 마치고 append를 해야함 그리고 반대로 돌아가면서 데이터프레임을만든다?
# 그러면 리스트로받는다? 리스트를 데이터프레임으로?
# 리스트를 뽑아야함


# def hour_or_minute(test1):
#     print(test1[:])
#     if test1[:-3:-1][::-1] == '시간': # 끝이 시간이라면? 어떻게 시간만 가능할까?
#         print(test1[:-3:-1][::-1]) #test 전체를 넣어버리면 안된다?
#         test1 = str(test1)
#         print(type(test1))
#         test1=test1.replace("시간","")
#         print(test1)
#         test1=float(test1)*60
#         print(test1) #성공함ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ
#         test1 = float(test1)*60
#     elif test1[:-2:-1][::-1] == '분':
#         print(test1[:-2:-1][::-1])
#         # i = str(i)
#         # print(type(i))
#         # i = i.replace("분","")
#         # print(i)
#         #hour_or_minute_list.append(i)

# print(hour_or_minute("30분"))



# def hour_or_minute(test1):
#     for i in test1:
#         print(test1[:])
#         if i[:-3:-1][::-1] == '시간': # 끝이 시간이라면? 어떻게 시간만 가능할까?
#             print(i[:-3:-1][::-1]) #test 전체를 넣어버리면 안된다?
#             test1 = str(i)
#             print(type(i))
#             i=i.replace("시간","")
#             print(i)
#             test1=float(i)*60
#             print(i)
#         elif i[:-2:-1][::-1] == '분':
#             print(i[:-2:-1][::-1])
#             i = str(i)
#             print(type(i))
#             i = i.replace("분","")
#         return i
# print(hour_or_minute("3시간"))

# 다 되는거 -----------------------------------------------------------------
# def hour_or_minute(test1):
#     print(test1[:], type(test1))
#     if test1[:-3:-1][::-1] == '시간':
#         print(test1[:-3:-1][::-1]) 
#         test1 = str(test1)
#         print(type(test1))
#         test1=test1.replace("시간","")
#         print(test1)
#         test1=int(float(test1)*60)
#         print(test1)
#     elif test1[:-2:-1][::-1] == '분':
#         print(test1[:-2:-1][::-1])
#         test1 = str(test1)
#         print(type(test1))
#         test1 = test1.replace("분","")
#     return test1


# print(hour_or_minute("30분"))
# print(type(test1))
# apply 사용 및 for문을 돌린다?
#print(test1.apply(hour_or_minute, axis=1))

# -----------------------------------------------------------------

# append를 해야하나? 변경하고선 넣으라고 되어있지만 그 인덱스 자리에 넣으라고 되어있는 게 아니고, 그 변수에 넣어라. 라는 형식이잖아
# 그러면 전체 값이 들어오면 인덱스가 각각 들어가는 것이 아니다? 왜냐 for문이 아니니깐.
# 그렇다면 for문으로 각각 i에 대입을 하는데 만약 시간이라면 append해주고, 분이면 append를 해주어라.

# def hour_or_minute(test1):
#     print(test1[:])
#     if test1[:-3:-1][::-1] == '시간': # 끝이 시간이라면? 어떻게 시간만 가능할까?
#         print(test1[:-3:-1][::-1]) #test 전체를 넣어버리면 안된다?
#         test1 = str(test1)
#         print(type(test1))
#         test1=test1.replace("시간","")
#         print(test1)
#         test1=float(test1)*60
#         print(test1) #성공함ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ
#         test1 = str(test1.str.replace(pat=r'시간', repl=r'', regex=True))
#         print(test1)
#         test1 = float(test1)*60
#     else:
#         test1 = str(test1.str.replace(pat=r'분', repl=r'', regex=True))
#     return test1
# print(hour_or_minute("3시간"))


#class HourMinute()
#print(test1)
# def hour_or_minute(test1):
#     print(test1[:])
#     if test1[:-3:-1][::-1] == '시간': # 끝이 시간이라면? 어떻게 시간만 가능할까?
#         print(test1[:-3:-1][::-1]) #test 전체를 넣어버리면 안된다?
#         test1 = str(test1[:-3:-1][::-1].str.replace(pat=r'시간', repl=r'', regex=True)) #이러면 인덱스 순번이 잘린다 -> 실패
#         print(test1)
#         test1 = float(test1)*60
#     else:
#         test1 = str(test1.str.replace(pat=r'분', repl=r'', regex=True))
#     return test1
# print(hour_or_minute("3시간"))

#------------------------------
# def hour_or_minute(test1):
#     if test1[:-2] == '시간':
#         test1 = str(test1.str.replace(pat=r'시간', repl=r'', regex=True))
#         test1 = float(test1)*60
#     else:
#         test1 = str(test1.str.replace(pat=r'분', repl=r'', regex=True))
# print(hour_or_minute)
#---------------------------------
# def hour_or_minute(test1):
#     if test1[:-2] == '시간':
#         test1 = str(test1.str.replace(pat=r'시간', repl=r'', regex=True))
#         print(float(test1.str[:-2])*60)
#     else:
#         test1 = str(test1.str.replace(pat=r'분', repl=r'', regex=True))




#test1 = str(test1)
#print(test1, type(test1))
#print(test1.str[:-2]=='시간')  # .이 있어서 float으로
# def hour_or_minute(test1):
#     if test1[:-2] == '시간':
#         return float(test1.str[:-2])*60 #슬라이싱하면 복사가 되잖아. 그러면 완전히 잘라야함 떨어트려야함. -> 이거 안돼 시간만잘리는게아니고 분도포함돼있잖아

    # #시간인 것만 *을 해주어야한다. 전체를 변경은 불가하다.
    # else test1.str[:-1] == '분':
    #     return test1.rstrip("분")


# def hour_or_minute(test1):
#     if test1.str[:-2] == '시간':
#         test1=str(test1)
#         test1.replace("시간","")
#         return int(test1.rstrip("시간"))*60 #슬라이싱하면 복사가 되잖아. 그러면 완전히 잘라야함 떨어트려야함. -> 이거 안돼 시간만잘리는게아니고 분도포함돼있잖아
#     #시간인 것만 *을 해주어야한다. 전체를 변경은 불가하다.
#     else test1.str[:-1] == '분':
#         return test1.rstrip("분")

# def hour_or_minute(test1):
#     if test1.str[:-2] == '시간':
#         return int(test1.drop[:-2])*60 #슬라이싱하면 복사가 되잖아. 그러면 완전히 잘라야함 떨어트려야함.
#     else test1.str[:-1] == '분':
#         return .strdrop[:-1]

# rstrip을 이용해서 시간을 없애보자

# while test1.index < test1.index[:-1]:
    
#     if test1.index[:-1] == '분': continue
    
# 1.나눠서해도 인덱스 번호 섞여서 불가해보임.
# 다른 방안 - 빠지는 값에 fillna nan값이 되는것도 아님 -> 그러면 시간데이터만 추출하고 거기를(그자리를) nan값으로 채우고, 시간 데이터 작업 뒤에 다시 넣는다?
# 2. 동시에 데이터를 변경? 시간과 분의 문자열을 제거하고 시간만 따로 연산을 해야하는데 이를 진행할 수가 없음
# 시간에만 *60을 해야하는데 정규식으로 하려했지만 불가해보임
# apply를 이용? - 두 가지 변경을 하면서 곱을 어떻게?



#*****
# import pandas as pd

# df_devel_d_science = pd.read_csv("devel_d_science.csv")
# #df_devel_d_science["강의 총 시간"].head()
# df_devel_d_science.head()

# print(type(df_devel_d_science))
# df_devel_d_science["강의 총 시간"].replace("시간","시", regex=True, inplace=True)

# df_devel_d_science['시/분']=df_devel_d_science["강의 총 시간"].str[-1]

# df_devel_d_science["강의 총 시간"] = df_devel_d_science["강의 총 시간"].str.rstrip("시")
# df_devel_d_science["강의 총 시간"] = df_devel_d_science["강의 총 시간"].str.rstrip("분")

# df_devel_d_science.loc[df_devel_d_science["시/분"]=="시", "강의 총 시간"] = df_devel_d_science["강의 총 시간"]*60
# print(df_devel_d_science)


# #print(test1)
# # 분과 시간이 각각 있음, 분은 분대로, 시간은 시간대로 모아서 데이터프레임으로 만들어주고,
# # 분은 한글 '분'만 drop을 이용해서 -1
# #test1=test1.replace("시간","")

# #if test1.str[:-1] == '간':
    

# # test1 = (str(test1))
# # test1 = test1.replace("시간","")
# # print(test1)
# #print(test1.str[:-2])
# # 이것만 뺄 수 있는 작업을 내가 할 수 있다면 거기서 이미 연산을 했지

# # test1=str(test1.str.replace(pat=r'시간|분', repl=r'', regex=True))
# # print(test1) # 012를 제외하고 3,4가 출력된다


# # test1=str(test1[:-3:-1][::-1].str.replace(pat=r'시간|분', repl=r'', regex=True))
# # print(test1) # 0,1,2를 제외하고 3,4가 출력된다 - 이건 시간만을 뽑아내기 위한 코드였기 때문. 근데 여기선 인덱스 기준으로 끝에 2곳만 나온것으로보인다.

# #test1 이라는 다음에 인덱스가 아닌 슬라이싱으로 출력을 했기 때문. 그러면 문자를 자르고자한다면 str뒤에 붙여야되지 않을까해서 붙이니 pat오류
# #--
# #test1_1=str(test1.str.replace(pat=r'시간', repl=r'*60', regex=True)) # 이거 그냥 따로 빼서 df로 만들고, 정수형해서 60곱함
# # 여기 시간은 없앤 거를 다시 한 번 정규식을 돌리면 되잖아. 그러면 어떻게 해야할까? - 한 번에 패턴 두가지넣어서 없애면 구분을 지을수가 없으니 시간먼저하고, 분을 친다
# #test1_2=str(test1_1.replace(pat=r'분', repl=r'', regex=True))
# #--
# # 위에 *60에서 *을 문자형으로 받아들일것같음
# # 예상이 맞았고, 그러면 시간에만 끝에 60을 붙여서 만들어주고, 일단 int형으로 변경을 한다. 그러면 연산이 가능해지고, 내가 다룰 수 있다
# # 이 때 replace로 (문자형만가능)

#  # 이것도 따로 빼서 정수형 만들고 위에꺼랑 합침 -> 잠깐! 그러면 기존에
# #정렬되어있는 데이터 자료들이랑 다 어긋나버린다 -> 그러면 망함ㅜ 어떻게할것이냐 -> ? -> 원하는것만 변경하는게 가장 좋음
# #-> 
# #test1_1=(str(test1_1))
# #print(test1_1, type(test1_1))
# #print(test1_2, type(test1_2))
# # test2_1=test1.str.replace(pat=r'분', repl=r'', regex=True)
# # test2_1=str(test2_1)
# # print(type(test2_1))
# # print(test2_1)
# # 별점--------------
# # test_rating = df_devel_d_science["별점"].head()
# # test_rating=test_rating.round(1)
# # print(test_rating)
# # # 별점 끝

# hour_or_minute_list = []

# # list(test1) -> 이렇게하면 문자열로 비교가 불가능해져. 아닌가 한 인덱스를 볼 때마다 잘라서 보았을 때니깐 리스트로 해볼만하겠다

# # test1=list(test1)
# # print(type(test1))
# #print(test1)
# # 인덱스마다 끝에 두 글자 확인을 하려면 for문으로 인덱스를 돌아간다. 해당 인덱스의 끝에 두 글자만 확인
# #print(test1[:-3:-1][::-1])

# # def hour_or_minute(test1):
# #     #print(test1[:-3:-1][::-1])
# #     for i in test1:
# #         print(i)
# #         if i[:-3:-1][::-1] == '시간':
# #             print(i[:-3:-1][::-1])
# #             i = str(i)
# #             print(type(i))
# #             i=i.replace("시간","")
# #             print(i)
# #             i=float(i)*60
# #             print(i)
# #             hour_or_minute_list.append(i)
# #         elif i[:-2:-1][::-1] == '분':
# #             print(i[:-2:-1][::-1])
# #             i = str(i)
# #             print(type(i))
# #             i = i.replace("분","")
# #             hour_or_minute_list.append(i)
# #         return test1
# # print(hour_or_minute(test1))
# # print(hour_or_minute_list)

# #test1을 리스트화해서 넣어준다?


# # def hour_or_minute(test1):
# #     print(test1[:-3:-1][::-1])
# #     for i in test1:
# #         # print(test1[:-3:-1][::-1].text)
# #         if i[:-3:-1][::-1] == '시간': #i.text?
# #             print(i)
#         #     i = str(i)
#         #     print(type(i))
#         #     i=i.replace("시간","")
#         #     print(i)
#         #     i=float(i)*60
#         #     print(i)
#         #     hour_or_minute_list.append(i)
#         #     print(hour_or_minute_list)            
#         # elif i[:-2:-1][::-1] == '분':
#         #     i = str(i)
#         #     print(type(i))
#         #     i = i.replace("분","")
#         #     hour_or_minute_list.append(i)
#         # return test1
#     # print(hour_or_minute_list)
# # print(hour_or_minute_list)
# # print(hour_or_minute("3시간"))
# #append를 안해줬어 -> append를 해주어야함
# #연산을 마치고 append를 해야함 그리고 반대로 돌아가면서 데이터프레임을만든다?
# # 그러면 리스트로받는다? 리스트를 데이터프레임으로?
# # 리스트를 뽑아야함


# # def hour_or_minute(test1):
# #     print(test1[:])
# #     if test1[:-3:-1][::-1] == '시간': # 끝이 시간이라면? 어떻게 시간만 가능할까?
# #         print(test1[:-3:-1][::-1]) #test 전체를 넣어버리면 안된다?
# #         test1 = str(test1)
# #         print(type(test1))
# #         test1=test1.replace("시간","")
# #         print(test1)
# #         test1=float(test1)*60
# #         print(test1) #성공함ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ
# #         test1 = float(test1)*60
# #     elif test1[:-2:-1][::-1] == '분':
# #         print(test1[:-2:-1][::-1])
# #         # i = str(i)
# #         # print(type(i))
# #         # i = i.replace("분","")
# #         # print(i)
# #         #hour_or_minute_list.append(i)

# # print(hour_or_minute("30분"))



# # def hour_or_minute(test1):
# #     for i in test1:
# #         print(test1[:])
# #         if i[:-3:-1][::-1] == '시간': # 끝이 시간이라면? 어떻게 시간만 가능할까?
# #             print(i[:-3:-1][::-1]) #test 전체를 넣어버리면 안된다?
# #             test1 = str(i)
# #             print(type(i))
# #             i=i.replace("시간","")
# #             print(i)
# #             test1=float(i)*60
# #             print(i)
# #         elif i[:-2:-1][::-1] == '분':
# #             print(i[:-2:-1][::-1])
# #             i = str(i)
# #             print(type(i))
# #             i = i.replace("분","")
# #         return i
# # print(hour_or_minute("3시간"))

# # 다 되는거 -----------------------------------------------------------------
# # def hour_or_minute(test1):
# #     print(test1[:])
# #     if test1[:-3:-1][::-1] == '시간':
# #         print(test1[:-3:-1][::-1]) 
# #         test1 = str(test1)
# #         print(type(test1))
# #         test1=test1.replace("시간","")
# #         print(test1)
# #         test1=int(float(test1)*60)
# #         print(test1)
# #     elif test1[:-2:-1][::-1] == '분':
# #         print(test1[:-2:-1][::-1])
# #         test1 = str(test1)
# #         print(type(test1))
# #         test1 = test1.replace("분","")
# #     return test1


# # print(hour_or_minute(test1))

# # apply 사용 및 for문을 돌린다?
# #test1.apply(hour_or_minute, axis=1)

# # -----------------------------------------------------------------

# # append를 해야하나? 변경하고선 넣으라고 되어있지만 그 인덱스 자리에 넣으라고 되어있는 게 아니고, 그 변수에 넣어라. 라는 형식이잖아
# # 그러면 전체 값이 들어오면 인덱스가 각각 들어가는 것이 아니다? 왜냐 for문이 아니니깐.
# # 그렇다면 for문으로 각각 i에 대입을 하는데 만약 시간이라면 append해주고, 분이면 append를 해주어라.

# # def hour_or_minute(test1):
# #     print(test1[:])
# #     if test1[:-3:-1][::-1] == '시간': # 끝이 시간이라면? 어떻게 시간만 가능할까?
# #         print(test1[:-3:-1][::-1]) #test 전체를 넣어버리면 안된다?
# #         test1 = str(test1)
# #         print(type(test1))
# #         test1=test1.replace("시간","")
# #         print(test1)
# #         test1=float(test1)*60
# #         print(test1) #성공함ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ
# #         test1 = str(test1.str.replace(pat=r'시간', repl=r'', regex=True))
# #         print(test1)
# #         test1 = float(test1)*60
# #     else:
# #         test1 = str(test1.str.replace(pat=r'분', repl=r'', regex=True))
# #     return test1
# # print(hour_or_minute("3시간"))


# #class HourMinute()
# #print(test1)
# # def hour_or_minute(test1):
# #     print(test1[:])
# #     if test1[:-3:-1][::-1] == '시간': # 끝이 시간이라면? 어떻게 시간만 가능할까?
# #         print(test1[:-3:-1][::-1]) #test 전체를 넣어버리면 안된다?
# #         test1 = str(test1[:-3:-1][::-1].str.replace(pat=r'시간', repl=r'', regex=True)) #이러면 인덱스 순번이 잘린다 -> 실패
# #         print(test1)
# #         test1 = float(test1)*60
# #     else:
# #         test1 = str(test1.str.replace(pat=r'분', repl=r'', regex=True))
# #     return test1
# # print(hour_or_minute("3시간"))

# #------------------------------
# # def hour_or_minute(test1):
# #     if test1[:-2] == '시간':
# #         test1 = str(test1.str.replace(pat=r'시간', repl=r'', regex=True))
# #         test1 = float(test1)*60
# #     else:
# #         test1 = str(test1.str.replace(pat=r'분', repl=r'', regex=True))
# # print(hour_or_minute)
# #---------------------------------
# # def hour_or_minute(test1):
# #     if test1[:-2] == '시간':
# #         test1 = str(test1.str.replace(pat=r'시간', repl=r'', regex=True))
# #         print(float(test1.str[:-2])*60)
# #     else:
# #         test1 = str(test1.str.replace(pat=r'분', repl=r'', regex=True))




# #test1 = str(test1)
# #print(test1, type(test1))
# #print(test1.str[:-2]=='시간')  # .이 있어서 float으로
# # def hour_or_minute(test1):
# #     if test1[:-2] == '시간':
# #         return float(test1.str[:-2])*60 #슬라이싱하면 복사가 되잖아. 그러면 완전히 잘라야함 떨어트려야함. -> 이거 안돼 시간만잘리는게아니고 분도포함돼있잖아

#     # #시간인 것만 *을 해주어야한다. 전체를 변경은 불가하다.
#     # else test1.str[:-1] == '분':
#     #     return test1.rstrip("분")


# # def hour_or_minute(test1):
# #     if test1.str[:-2] == '시간':
# #         test1=str(test1)
# #         test1.replace("시간","")
# #         return int(test1.rstrip("시간"))*60 #슬라이싱하면 복사가 되잖아. 그러면 완전히 잘라야함 떨어트려야함. -> 이거 안돼 시간만잘리는게아니고 분도포함돼있잖아
# #     #시간인 것만 *을 해주어야한다. 전체를 변경은 불가하다.
# #     else test1.str[:-1] == '분':
# #         return test1.rstrip("분")

# # def hour_or_minute(test1):
# #     if test1.str[:-2] == '시간':
# #         return int(test1.drop[:-2])*60 #슬라이싱하면 복사가 되잖아. 그러면 완전히 잘라야함 떨어트려야함.
# #     else test1.str[:-1] == '분':
# #         return .strdrop[:-1]

# # rstrip을 이용해서 시간을 없애보자

# # while test1.index < test1.index[:-1]:
    
# #     if test1.index[:-1] == '분': continue
    
# # 1.나눠서해도 인덱스 번호 섞여서 불가해보임.
# # 다른 방안 - 빠지는 값에 fillna nan값이 되는것도 아님 -> 그러면 시간데이터만 추출하고 거기를(그자리를) nan값으로 채우고, 시간 데이터 작업 뒤에 다시 넣는다?
# # 2. 동시에 데이터를 변경? 시간과 분의 문자열을 제거하고 시간만 따로 연산을 해야하는데 이를 진행할 수가 없음
# # 시간에만 *60을 해야하는데 정규식으로 하려했지만 불가해보임
# # apply를 이용? - 두 가지 변경을 하면서 곱을 어떻게?
