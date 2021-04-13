import json
import jsonpath
from pyecharts.charts import Map,Geo
from pyecharts import options as opts
from pyecharts.globals import GeoType,RenderType

fp=open('data/last_day_corona_virus_of_china.json')         #我的电脑是需要加上encoding='utf8'的,不然会乱码.
# 2.2加载该文件对象并转化
python_list = json.load(fp)
print(python_list)
print(type(python_list[0]))