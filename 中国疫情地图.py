# coding=gbk
import json
import re

import jsonpath
from pyecharts.charts import Map,Geo
from pyecharts import options as opts
from pyecharts.globals import GeoType,RenderType




# 2.��JOSN��ʽ�ļ�ת��ΪPYTHON���͵�����
# 2.1����ָ����ļ��Ķ���
with open('data/last_day_corona_virus_of_china.json', encoding='utf8') as fp:   #�ҵĵ�������Ҫ����encoding='utf8'��,��Ȼ������.
    # 2.2���ظ��ļ�����ת��
    python_list = json.load(fp)
    print(python_list)
    print(type(python_list))
    #print(python_list[0]['provinceName''])

    python_list = re.sub(r'provinceShortName', 'cityName', python_list)


    #ʡ������
    provincename = jsonpath.jsonpath(python_list, "$..cityName'")
    print(provincename)

    confirmedCount = jsonpath.jsonpath(python_list, "$..confirmedCount'")
    print(confirmedCount)
    #����ֵ�
    data_list = list(zip(provincename,confirmedCount))
    print(data_list)



#��Ӣ��ӳ����ֵ�

# 4 ���ݿ��ӻ�
map = Map().add(series_name="�й�����ֲ�",
                data_pair=data_list,
                maptype="china",

                is_map_symbol_show=False
                    )


map.set_series_opts(label_opts=opts.LabelOpts(is_show=False))    #����ʾ��������

map.set_global_opts(title_opts=opts.TitleOpts(title="��������") ,  #���ñ���
                    visualmap_opts=opts.VisualMapOpts(max_=2500,is_piecewise=True))
map.render('�й�����ֲ�.html')