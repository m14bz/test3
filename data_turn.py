

# 导入pandas包
import pandas as pd
import datetime as dt
import numpy as np
from pandas import Series,DataFrame


# 获取列表中返回的数值，如果没有对应的值，则返回默认的default。
def safe_list_get (l, idx, default):
  try:
    return l[idx]
  except IndexError:
    return default




# 读取Excel数据，选取省份这张表
res = pd.read_csv("data/corona_virus.csv")




# 显示前几行
#
# print(res.dtypes)

# 数据集中的日期范围一共有多少天？并且安装日期进行排序
days = np.sort(res["日期"].unique())
print(days)
# 数据集中的省市范围一共有多少个？
provinces = res["国家"].unique()
print(type(provinces))

data = {'province':Series(provinces)}

df = DataFrame(data)
print(type(df))





# df["www"] =  df['province'].apply(lambda x: dt.datetime.strftime(x, '%Y-%m-%d'))
'''
print("##############")
# print(    res[(res.Date2String=='2020-02-18')&(res.省份=='北京')]   )

print(    type(res[(res.Date2String=='2020-02-18')&(res.省份=='北京')]["累计确诊"]  ) )
print(   (res[(res.Date2String=='2020-02-18')&(res.省份=='北京')]["累计确诊"]).tolist()[0]   )
print(   safe_list_get( (res[(res.Date2String=='2020-02-18')&(res.省份=='北京')]["累计确诊"]).tolist(), 0, 0 )  )
print("##############")
'''


for i in days:
    df[i] = df['province'].apply(lambda x:   safe_list_get((res[(res.日期==i)&(res.国家==x)]["确诊人数"]).tolist(), 0, 0 )       )


print(df.head())
print(df.shape)


df.to_excel('data/data_result666666.xlsx', sheet_name='data_result_By_Province')



