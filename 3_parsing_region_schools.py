from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

lst = []
regions = []
reg = 'zabajkalskij-kraj'
reg2 = f'https://school-edu.ru/{reg}/'
with open(f'regions/{reg}.txt', encoding='utf8') as f:
    for i in f:
        regions.append(i.strip())
for region in regions:
    cnt = 1
    while cnt != 200:
        tmp = []
        params = {'jsf': 'epro-archive', 'pagenum': cnt}
        r = requests.get(region, params=params)
        r1 = r.status_code
        r = r.text
        if r1 != 100000:
            soup = BeautifulSoup(r, "lxml")
            for link in soup.find_all('a'):
                if link.has_attr('href'):
                    l = link.get('href')
                    if l != 'https://school-edu.ru/' and l != '#content' and l != '#' and l != 'https://school-edu.ru' and l not in lst and l != reg2:
                        if l not in lst:
                            lst.append(l)
                            tmp.append(l)
                            with open(f'pages/{reg}.txt', 'a', encoding='utf8') as f:
                                f.write(l)
                                f.write('\n')
            cnt += 1
        print(len(tmp))
        if len(tmp) != 0:
            continue
        else:
            break
