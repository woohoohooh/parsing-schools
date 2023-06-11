# тут собирал ссылки на города - https://school-edu.ru/altajskij-kraj/
from urllib.request import urlopen
from bs4 import BeautifulSoup

cities = []

with open('old/1_parsing_regions.txt', encoding='utf8') as f:
    for i in f:
        cities.append(i.strip())

try:
    for i in cities:
        x = i.find('ru/')
        y = i[x+2:].replace('/', '')
        resp = urlopen(i)
        html = resp.read().decode('utf-8')
        soup = BeautifulSoup(html, "lxml")
        try:
            for link in soup.find_all('a'):
                if link.has_attr('href'):
                    with open(f'regions/{y}.txt', 'a', encoding='utf8') as ff:
                        ll = f"https://school-edu.ru{link.get('href')}"
                        if ll != 'https://school-edu.ru#' and ll != 'https://school-edu.ruhttps://school-edu.ru/' and ll != 'https://school-edu.ru#content' and ll != 'https://school-edu.ruhttps://school-edu.ru':
                            ff.write(f"{link.get('href')}")
                            ff.write('\n')
        except:
            ...
except:
    ...