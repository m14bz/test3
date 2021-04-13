# coding=gbk
import json
from pyecharts.charts import Map,Geo
from pyecharts import options as opts
import jsonpath
import requests
import re
from bs4 import BeautifulSoup

# 2.发送请求获取疫情首页内容
response =requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia')
home_page =response.content.decode()
#print(home_page)

# 3.使用BeautifulSoup提取疫情数据
soup = BeautifulSoup(home_page, 'lxml')
script = soup.find(attrs={'id': 'getAreaStat'})   #国内getAreaStat，国际getListByCountryTypeService2true
text = script.string #用的string类型拿到了

# 4.使用正则表达式, 提取json字符串
json_str =re.findall(r'\[.+\]', text)[0] # 取出findall列表中的第0个元素

json_str=re.sub(r'provinceShortName','cityName',json_str)
print(json_str)
python_list = json.loads(json_str)
#provincename = jsonpath.jsonpath(python_list, "$..cityName'")
#print(provincename)

confirmedCount = jsonpath.jsonpath(python_list, "$..confirmedCount'")
print(confirmedCount)
