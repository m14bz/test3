import requests
from bs4 import BeautifulSoup
import re
import json
from tqdm import tqdm
class CoronaVirusSpider(object):

    def __init__(self):
        self.home_url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'

    def get_content_from_url(self, url):
        """"
        根据url，获取响应的字符串数据
        :param url: 请求的URL
        :return: 响应内容的字符串
        """
        response = requests.get(url)
        return response.content.decode()


    def parse_home_page(self, home_page):
        """
        解析首页内容，获取解析后的Python数据
        :param home_page: 首页的内容
        :return: 解析后的Python数据
        """
        # 2.从疫情首页，提取最近一日各国数据
        soup = BeautifulSoup(home_page, 'lxml')
        script = soup.find(id='getListByCountryTypeService2true')
        text = script.string
        # print(text)

        # 3.从疫情数据中，获取json格式的字符串
        json_str = re.findall(r'\[.+\]', text)[0]
        # print(json_str)

        # 4.把json格式的字符串转化为Python类型
        data = json.loads(json_str)
        return data

    def save(self, data, path):
        # 5.以json格式保存最近一日各国疫情数据
        with open(path, 'w', encoding='utf8') as fp:
            json.dump(data, fp, ensure_ascii=False)

    def crawl_last_day_corona_virus(self):
        """
        采集最近一天的各国疫情信息
        :return:
        """
        # 1.发送请求，获取首页内容
        home_page = self.get_content_from_url(self.home_url)
        # 2.解析首页内容,获取最近一天的各国疫情数据
        last_day_corona_virus = self.parse_home_page(home_page)
        # 3.保存数据
        self.save(last_day_corona_virus,'data/last_day_corona_virus.json')

    def crawl_corona_virus(self):
        """
        采集从1月23号以来各国疫情数据
        :return:
        """
        # 1.加载各国疫情数据
        with open('data/last_day_corona_virus.json',encoding='utf8') as fp:
            last_day_corona_virus = json.load(fp)
        # print(last_day_corona_virus)
        # 定义列表，用于存储各国从1月23日以来的疫情数据
        corona_virus = []
        # 2.遍历各国疫情数据
        for country in tqdm(last_day_corona_virus, '采集1月23日以来的各国疫情信息'):
            # 3.发送请求，获取各国从1月23号至今的json数据
            statistics_data_url = country['statisticsData']
            statistics_data_json_str = self.get_content_from_url(statistics_data_url)
            # 4.把json数据转换为Python类型的数据，添加到列表
            statistics_data = json.loads(statistics_data_json_str)['data']
            # print(statistics_data)
            for one_day in statistics_data:
                one_day['provinceName'] = country['provinceName']
                one_day['countryShortCode'] = country['countryShortCode']
            # print(statistics_data)
            corona_virus.extend(statistics_data) # 将元素放到列表里去
            # 5.保存列表的数据以JSON格式保存为文件
        self.save(corona_virus, 'data/corona_virus.json')
    def run(self):
        # self.crawl_last_day_corona_virus()
        self.crawl_corona_virus()

if __name__ == '__main__':
    spider = CoronaVirusSpider()
    spider.run()