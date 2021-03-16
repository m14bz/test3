# coding=gbk
import json
from operator import attrgetter
import pandas as pd
import jsonpath
from dateutil.parser import parse


def turn_list(dataids):                         #   日期格式转换
    list_1 = []
    for dateid in dateids:
        a = str(dateid)
        b = parse(a)
        dateid = b.strftime('%Y-%m-%d')
        list_1.append(dateid)
    return list_1


# 2.把JOSN格式文件转化为PYTHON类型的数据
# 2.1构建指向该文件的对象
with open('data/corona_virus.json') as fp:   #我的电脑是需要加上encoding='utf8'的,不然会乱码.
    # 2.2加载该文件对象并转化
    python_list = json.load(fp)


#  3 提取数组


    #国家名称
    countryname = jsonpath.jsonpath(python_list,"$..provinceName'")


    #确诊人数
    confirmedCount=jsonpath.jsonpath(python_list,"$..confirmedCount'")
    #print(confirmedCount)

    dateids = jsonpath.jsonpath(python_list, "$..dateId'")
    dateids = turn_list(dateids)                           #数据格式转换




    #组成字典
    data_list = list(zip(countryname,confirmedCount,dateids))
    print(type(data_list))

    name = ['国家','确诊人数','日期']
    test = pd.DataFrame(columns=name,data=data_list)

    test = test.dropna(axis=1, how='any')
    test.to_csv('data/corona_virus.csv')







