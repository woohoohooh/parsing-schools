# тут собирал ссылки на регионы - https://school-edu.ru/

from urllib.request import urlopen
from bs4 import BeautifulSoup

resp = urlopen('https://school-edu.ru')
html = resp.read().decode('utf-8')
soup = BeautifulSoup(html, "lxml")
try:
    for link in soup.find_all('a'):
        if link.has_attr('href'):
            with open('old/1_parsing_regions.txt', 'a', encoding='utf8') as f:
                f.write(f"https://school-edu.ru{link.get('href')}")
                f.write('\n')
except:
    ...

# import requests
# params = {'jsf': 'epro-archive', 'pagenum': 1}
# r = requests.get('https://school-edu.ru', params=params)
# r = r.text



# r3 = r2.find('"')
# r4 = r2[:r3]
# print(r1)
#

# count = r.count('http')
# count2 = 0
# urls = []
# count_r = 0
# for i in r[:]:
#     r1 = r.find('https://')
#     r2 = r[r1:]
#     if 'http' in r:
#         print('yyyyyyyyy')
#         count2 += 1





