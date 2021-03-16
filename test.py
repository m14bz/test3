import requests
import re


def parse_url(page_url,f):

    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
    try:
        r=requests.get(page_url,headers=headers,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        html = r.text
    except:
        print('访问失败')

    # print(html)
    #获取省或城市的信息，为避免遗漏省份，可以先将"provinceShortName"替换"cityName"再分析
    html=re.sub(r'provinceShortName','cityName',html)
    #再把关于中国的部分取出来
    html=re.search('{ window.getAreaStat =.+?window.getIndexRecommendList2',html)
    html=html.group()
    # print(html)
    cities=re.findall(r"""
    {.*?"cityName":"(.+?)",                         #城市名称
    "currentConfirmedCount":(-?\d+),                  #现存确诊
    "confirmedCount":(\d+),                         #累计确诊
    .+?"curedCount":(\d+),                          #治愈
    "deadCount":(\d+)                               #死亡
        """, html, re.VERBOSE | re.DOTALL)

    # print(type(cities))
    for city in cities:
        city = list(city)
        # print(city)
        f.write('{},{},{},{},{}\n'.format(''.join(city[0]), ''.join(city[1]), ''.join(city[2]), ''.join(city[4]),
                                          ''.join(city[3])))


def main():
    page_url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'
    with open('data/epidemic situation.csv', 'a', encoding='utf-8') as f:
        parse_url(page_url, f)


main()