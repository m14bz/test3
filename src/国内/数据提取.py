import json
from turtle import pd
import pandas as pd

import jsonpath
from pyecharts.charts import Map,Geo
from pyecharts import options as opts
from pyecharts.globals import GeoType,RenderType

fp=open('../../data/last_day_corona_virus_of_china.json')
python_list = json.load(fp)
print(python_list)
print(type(python_list[0]))
provinceName = jsonpath.jsonpath(python_list, "$..provinceName'")
countryname = jsonpath.jsonpath(python_list, "$..cityName'")
confirmedCount = jsonpath.jsonpath(python_list, "$..confirmedCount'")
suspectedCount = jsonpath.jsonpath(python_list, "$..suspectedCount'")
curedCount = jsonpath.jsonpath(python_list, "$..curedCount'")
deadCount = jsonpath.jsonpath(python_list, "$..deadCount'")
hyperlink = jsonpath.jsonpath(python_list, "$..statisticsData'")

print(countryname)
print(confirmedCount)
print(suspectedCount)
print(curedCount)
print(deadCount)
print(provinceName)
print(hyperlink)



print(type(python_list))



print(len(countryname))
print(len(confirmedCount))
print(len(suspectedCount))
print(len(curedCount))
print(len(deadCount))
print(len(provinceName))
print(len(hyperlink))



data_list = list(zip(countryname,confirmedCount,suspectedCount,curedCount,deadCount))  #每个省份每个城市具体感染，确珍，死亡疑似的人数
print(data_list)
name = ['省份', '确诊人数', '疑似人数','治愈人数','死亡人数']
test = pd.DataFrame(columns=name, data=data_list)
test.to_csv('../../data/last_day_corona_virus_of_china.csv')


hyperlink_list = list(zip(provinceName,hyperlink))  #每个省份自2020.1.18来死亡疑似的人数
print(hyperlink_list)
print(type(hyperlink_list))
