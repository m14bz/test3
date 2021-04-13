# coding=gbk
import json
from pyecharts.charts import Map,Geo
from pyecharts import options as opts
import jsonpath
import requests
import re
from bs4 import BeautifulSoup

# 2.���������ȡ������ҳ����
response =requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia')
home_page =response.content.decode()
#print(home_page)

# 3.ʹ��BeautifulSoup��ȡ��������
soup = BeautifulSoup(home_page, 'lxml')
script = soup.find(attrs={'id': 'getAreaStat'})   #����getAreaStat������getListByCountryTypeService2true
text = script.string #�õ�string�����õ���

# 4.ʹ��������ʽ, ��ȡjson�ַ���
json_str =re.findall(r'\[.+\]', text)[0] # ȡ��findall�б��еĵ�0��Ԫ��

json_str=re.sub(r'provinceShortName','cityName',json_str)
print(json_str)
python_list = json.loads(json_str)
#provincename = jsonpath.jsonpath(python_list, "$..cityName'")
#print(provincename)

confirmedCount = jsonpath.jsonpath(python_list, "$..confirmedCount'")
print(confirmedCount)
