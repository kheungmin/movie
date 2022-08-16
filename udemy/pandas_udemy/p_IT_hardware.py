import pandas as pd

df = pd.read_csv("IT_hardware.csv")

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

df.to_csv("p_IT_hardware.csv", index=False)