import requests

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'altajskij-kraj'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'amurskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'arhangelskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'astrahanskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'belgorodskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'brjanskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'chechenskaja-respublika'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'cheljabinskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'chukotskij-avtonomnyj-okrug'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'chuvashskaja-respublika'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'evrejskaja-avtonomnaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'habarovskij-kraj'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'hanty-mansijskij-avtonomnyj-okrug-jugra'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'irkutskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'ivanovskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'jamalo-neneckij-avtonomnyj-okrug'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'jaroslavskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'kabardino-balkarskaja-respublika'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'kaliningradskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'kaluzhskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'kamchatskij-kraj'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'karachaevo-cherkesskaja-respublika'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'kemerovskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'kirovskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'kostromskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'krasnodarskij-kraj'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'krasnojarskij-kraj'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'kurganskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'kurskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'leningradskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'lipeckaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'magadanskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'moskovskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'moskva'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'neneckij-avtonomnyj-okrug'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'nizhegorodskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'novgorodskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'novosibirskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'omskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'orenburgskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'orlovskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'penzenskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'permskij-kraj'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'primorskij-kraj'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'pskovskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'respublika-adygeja'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'respublika-altaj'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'respublika-bashkortostan'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'respublika-burjatija'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'respublika-dagestan'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'respublika-hakasija'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'respublika-ingushetija'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'respublika-kalmykija'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'respublika-karelija'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'respublika-komi'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'respublika-krym'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'respublika-marij-jel'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'respublika-mordovija'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'respublika-saha-jakutija'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'respublika-severnaja-osetija-alanija'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'respublika-tatarstan'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'respublika-tyva'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'rjazanskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'rostovskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'sahalinskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'samarskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'sankt-peterburg'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'saratovskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'sevastopol-2'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'smolenskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'stavropolskij-kraj'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'sverdlovskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'tambovskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'tjumenskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'tomskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'tulskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'tverskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'udmurtskaja-respublika'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'uljanovskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'vladimirskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'volgogradskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'vologodskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'voronezhskaja-oblast'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data = 'zabajkalskij-kraj'
schools = []
cnt = 1
with open(f'pages/{data}.txt', encoding='utf8') as f:
    for i in f:
        schools.append(i.strip())
r = ''
d = ''
for i in schools:
    try:
        r = requests.get(i, timeout=7)
    except:
        ...
    try:
        d = r.status_code
    except:
        ...
    if d == 200:
        try:
            r = r.text
        except:
            ...
        try:
            b1 = r.find('<div class="jet-table__cell-text">Россия')
            if b1 > 0:
                b2 = r[b1+42:]
                b3 = b2.find('</div></div>')
                b4 = b2[:b3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f'——————————————————————————— {b4} ———————————————————————————')
                    f.write('\n')
        except:
            ...
        try:
            a1 = r.find('<h1 class="elementor-heading-title elementor-size-default">Информация об учебном заведении ')
            if a1 > 0:
                a2 = r[a1+91:]
                a3 = a2.find('</h1></div>')
                a4 = a2[:a3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(a4)
                    f.write('\n')
        except:
            ...
        try:
            c1 = r.find('<div class="jet-table__cell-text">+7')
            if c1 > 0:
                c2 = r[c1+34:].replace('+', '')
                c3 = c2.find('</div></div>')
                c4 = c2[:c3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(c4)
                    f.write('\n')
        except:
            ...
        try:
            d1 = r.find('<div class="jet-table__cell-text">http')
            if d1 > 0:
                d2 = r[d1+34:]
                d3 = d2.find('</div></div>')
                d4 = d2[:d3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(d4)
                    f.write('\n')
        except:
            ...
        try:
            e1 = r.find('<b>Электронная почта:</b></div></div></div></td><td class="jet-table__cell elementor-repeater-item-5f97434 jet-table__body-cell"><div class="jet-table__cell-inner"><div class="jet-table__cell-content"><div class="jet-table__cell-text">')
            if e1 > 0:
                e2 = r[e1+235:]
                e3 = e2.find('</div></div>')
                e4 = e2[:e3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(e4)
                    f.write('\n')
        except:
            ...
        try:
            f1 = r.find('<div class="jet-table__cell-text">https://vk')
            if f1 > 0:
                f2 = r[f1+34:]
                f3 = f2.find('</div></div>')
                f4 = f2[:f3]
                with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
                    f.write(f4)
                    f.write('\n')
        except:
            ...
        cnt += 1
    else:
        with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
            f.write('ОШИБКА КОННЕКТА')
            f.write('\n')

with open(f'fin/{data}.txt', 'a', encoding='utf8') as f:
    f.write(f'—————————————————————————————————————————————————————— {cnt} ——————————————————————————————————————————————————————')


