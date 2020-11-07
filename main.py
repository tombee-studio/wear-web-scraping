import requests
import re
import time
import tqdm
from bs4 import BeautifulSoup
import uuid

i = 0
for page in tqdm.tqdm(range(1, 100)):
    r = requests.get('https://wear.jp/men-coordinate/?pageno='+str(page))
    soup = BeautifulSoup(r.text, 'lxml')
    imgs = soup.find_all('img', attrs={"data-originalretina": re.compile('^//cdn.wimg.jp/coordinate')})
    items = [image.a.get("href") for image in soup.find_all('div', attrs={"class": "image"})]
    goods = soup.find_all('p', attrs={"class": "btn"})
    goods = goods[1::2]
    for img, good, item in zip(imgs, goods, items):
        u = requests.get("https://wear.jp{}".format(item))
        u_bs = BeautifulSoup(u.text, 'lxml')
        view = u_bs.find('p', {"class": "view_num"}).text
        i = i+1
        good_ = good.find('span')
        r = requests.get('http:' + img["data-originalretina"])
        with open(str('picture/men/m') + str(i) + '_' + str(good_.string) + '_' + str(view) + str('.jpeg'), 'wb') as file:
            file.write(r.content)
    time.sleep(2)


for page in tqdm.tqdm(range(1, 100)):
    r = requests.get('https://wear.jp/women-coordinate/?pageno=' + str(page))
    soup = BeautifulSoup(r.text, 'lxml')
    imgs = soup.find_all('img', attrs={"data-originalretina": re.compile('^//cdn.wimg.jp/coordinate')})
    items = [image.a.get("href") for image in soup.find_all('div', attrs={"class": "image"})]
    goods = soup.find_all('p', attrs={"class": "btn"})
    goods = goods[1::2]
    for img, good, item in zip(imgs, goods, items):
        u = requests.get("https://wear.jp{}".format(item))
        u_bs = BeautifulSoup(u.text, 'lxml')
        view = u_bs.find('p', {"class": "view_num"}).text
        i = i + 1
        good_ = good.find('span')
        r = requests.get('http:' + img["data-originalretina"])
        with open(str('picture/women/m') + str(i) + '_' + str(good_.string) + '_' + str(view) + str('.jpeg'),
                  'wb') as file:
            file.write(r.content)
    time.sleep(2)