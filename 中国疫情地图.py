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
provincename = jsonpath.jsonpath(python_list, "$..cityName'")
print(provincename)

confirmedCount = jsonpath.jsonpath(python_list, "$..confirmedCount'")
print(confirmedCount)
data_list = list(zip(provincename,confirmedCount))
print(data_list)

# 4 ���ݿ��ӻ�
map = Map().add(series_name="�й�����ֲ�",
                data_pair=data_list,
                maptype="china",

                is_map_symbol_show=False
                    )


map.set_series_opts(label_opts=opts.LabelOpts(is_show=False))    #����ʾ��������

map.set_global_opts(title_opts=opts.TitleOpts(title="��������") ,  #���ñ���
                    visualmap_opts=opts.VisualMapOpts(max_=70000,is_piecewise=True,pieces=[
                 {"min": 20000},
                 {"min": 10000, "max": 19999},
                 {"min": 5000, "max": 9999},
                 {"min": 3000, "max": 4999},
                 {"min": 1000, "max": 2999},
                 {"min": 500, "max": 999},
                 {"min": 200, "max": 499},
                 {"min": 100, "max": 199},
                 {"min": 10, "max": 99},
                 {"max": 9},]))

map.render('�й�����ֲ�.html')