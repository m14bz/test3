import requests
from bs4 import BeautifulSoup

response = requests.get("https://ncov.dxy.cn/ncovh5/view/pneumonia")
home_page = response.content.decode()
# print(home_page)

soup = BeautifulSoup(home_page, 'lxml')
script = soup.find(attrs={'id':'getListByCountryTypeService2true'})
print(script)
with open('filename.text', 'a', encoding='utf-8') as file:
    file.write('\n'.join(script))
