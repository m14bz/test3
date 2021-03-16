# coding=gbk
import json
from operator import attrgetter
import pandas as pd
import jsonpath
from dateutil.parser import parse


def turn_list(dataids):                         #   ���ڸ�ʽת��
    list_1 = []
    for dateid in dateids:
        a = str(dateid)
        b = parse(a)
        dateid = b.strftime('%Y-%m-%d')
        list_1.append(dateid)
    return list_1


# 2.��JOSN��ʽ�ļ�ת��ΪPYTHON���͵�����
# 2.1����ָ����ļ��Ķ���
with open('data/corona_virus.json') as fp:   #�ҵĵ�������Ҫ����encoding='utf8'��,��Ȼ������.
    # 2.2���ظ��ļ�����ת��
    python_list = json.load(fp)


#  3 ��ȡ����


    #��������
    countryname = jsonpath.jsonpath(python_list,"$..provinceName'")


    #ȷ������
    confirmedCount=jsonpath.jsonpath(python_list,"$..confirmedCount'")
    #print(confirmedCount)

    dateids = jsonpath.jsonpath(python_list, "$..dateId'")
    dateids = turn_list(dateids)                           #���ݸ�ʽת��




    #����ֵ�
    data_list = list(zip(countryname,confirmedCount,dateids))
    print(type(data_list))

    name = ['����','ȷ������','����']
    test = pd.DataFrame(columns=name,data=data_list)

    test = test.dropna(axis=1, how='any')
    test.to_csv('data/corona_virus.csv')







