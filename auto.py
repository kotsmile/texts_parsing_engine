import parsing_engine as pe
import utils
from urllib.parse import urljoin, urlparse
import time
import re
import pickle
import random

#
# AUTO_IMG = {
#     'text': {
#         'img': {'class': ['image-gallery-thumbnail-image', True, '_some'], '_extra': ('_else', lambda x: x['src'])}
#     },
#     'link': {'p': {'_extra': ('_nothing', None)}},
#     'theme_tag': {}
# }
#
# AUTO_HEADER = {
#     'text': {
#         'div': {'class': ['CardHead-module__title', True, '_some'], '_extra': ('_else', utils.enter)}
#     },
#     'link': {'p': {'_extra': ('_nothing', None)}},
#     'theme_tag': {}
# }


def avito_photo(s):
    s = 'https:' + s['data-url']
    return s


AVITO_IMG = {
    'text': {
        'div': {'class': ['gallery-img-frame', True, '_some'], '_extra': ('_else', avito_photo)}
    },
    'link': {'p': {'_extra': ('_nothing', None)}},
    'theme_tag': {}
}

AVITO_HEADER = {
    'text': {
        'span': {'class': ['title-info-title-text', True, '_some'], '_extra': ('_else', lambda x: x.text)}
    },
    'link': {'p': {'_extra': ('_nothing', None)}},
    'theme_tag': {}
}

AVITO_LINK = {
    'text': {
        'p': {'_extra': ('_nothing', lambda x: x)}
    },
    'link': {'h3': {'class': ['item-description-title', True, '_some'], '_extra': ('_else', None)}},
    'theme_tag': {}
}


def get(url=None):
    imgs = pe.web_parse(url=url, config=AVITO_IMG, anti_block=True)[0]
    time.sleep(1)
    header = pe.web_parse(url=url, config=AVITO_HEADER, html_print=False, anti_block=True)[0]
    time.sleep(1)
    return header[0], imgs


def find_links(page=1):
    link = f'https://www.avito.ru/moskva/avtomobili?p={page}&radius=1000&f=188_0b0.1375_0b0.1374_0b0.1286_0b0&i=1'
    return pe.web_parse(url=link, config=AVITO_LINK, html_print=False, anti_block=True)[1]





t = time.time()
PAGES = (1, 50)
machines = {}

for i in range(*PAGES):
    print(f'PAGE #{i}')
    urls = find_links(i)
    all_len = len(urls)
    t_page = time.time()
    for i, u in enumerate(urls):
        try:
            t = random.random() * 3
            print(f'{i * 100 / all_len:.0f}% wait: {t:.1f} s')
            k, v = get(u)
            time.sleep(random.random() * 10)
            if k in machines.keys():
                machines[k] += v
            else:
                machines[k] = v
        except IndexError or KeyboardInterrupt:
            print(u)
    print(f'page time: {(time.time() - t_page)//60} m')

print(time.time() - t)
with open('results/res_dict', 'wb') as f:
    pickle.dump(machines, f)

machines = dict()
with open('results/res_dict', 'rb') as f:
    machines = pickle.load(f)

with open('results/res.txt', 'w') as f:
    for k, v in machines.items():
        top = str(k) + '\n' + '\n'.join(v) + '\n\n'
        f.write(top)
        print(k)
        print('============')
        print(*v, sep='\n')
        print('============\n\n')
