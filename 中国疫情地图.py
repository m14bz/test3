# coding=gbk
import json
import re

import jsonpath
from pyecharts.charts import Map,Geo
from pyecharts import options as opts
from pyecharts.globals import GeoType,RenderType




# 2.把JOSN格式文件转化为PYTHON类型的数据
# 2.1构建指向该文件的对象
with open('data/last_day_corona_virus_of_china.json', encoding='utf8') as fp:   #我的电脑是需要加上encoding='utf8'的,不然会乱码.
    # 2.2加载该文件对象并转化
    python_list = json.load(fp)
    print(python_list)
    print(type(python_list))
    #print(python_list[0]['provinceName''])

    python_list = re.sub(r'provinceShortName', 'cityName', python_list)


    #省份名称
    provincename = jsonpath.jsonpath(python_list, "$..cityName'")
    print(provincename)

    confirmedCount = jsonpath.jsonpath(python_list, "$..confirmedCount'")
    print(confirmedCount)
    #组成字典
    data_list = list(zip(provincename,confirmedCount))
    print(data_list)



#中英文映射的字典

# 4 数据可视化
map = Map().add(series_name="中国疫情分布",
                data_pair=data_list,
                maptype="china",

                is_map_symbol_show=False
                    )


map.set_series_opts(label_opts=opts.LabelOpts(is_show=False))    #不显示国家名称

map.set_global_opts(title_opts=opts.TitleOpts(title="国内疫情") ,  #设置标题
                    visualmap_opts=opts.VisualMapOpts(max_=2500,is_piecewise=True))
map.render('中国疫情分布.html')