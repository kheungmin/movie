import pandas as pd

df=pd.read_csv("m_udemy.csv")

df.rename(
    columns={"강의명":"title",
             "수강생 수":"num_students",
             "강의 총 시간":"total_time",
             "강의 수":"num_videos",
             "강사명":"name_instructor",
             "별점":"stars"},
    inplace=True
)

df.drop("별점 수",axis=1,inplace=True)
df.to_csv("f_udemy.csv", index=False)