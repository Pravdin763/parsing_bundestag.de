import requests
from bs4 import BeautifulSoup
from time import sleep
import random
from download_info import json_file, csv_file

headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}

all_json_dict = {}      # в нем будет  вся инфа !
def all_info_card(url):     # собирается вся инфа с карточки пользователя, return не нужен, т.к. вся инфа записывается в словарь all_json_dict
    sleep(random.randint(1, 3))
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'lxml')

    res = soup.find('div', class_="col-xs-8 col-md-9 bt-biografie-name")

    name = res.find('h3').text.strip()
    post = res.find('p').text
    images = 'https://www.bundestag.de' + soup.find('div', class_="bt-bild-standard pull-left").find('img').get('data-img-xs-normal')
    soc = soup.find('ul', class_="bt-linkliste").find_all('li')
    social_media = tuple([i.find('a').get('href') for i in soc])       # список ссылок на соц сети

    all_json_dict[name] = {
        'post': post,
        'images': images,
        'url_card': url,
        'social_media': social_media
        }


for i in range(0, 721, 20):
    print(f'парсинг {i} страницы')
    url = f'https://www.bundestag.de/ajax/filterlist/de/abgeordnete/biografien/862712-862712?limit=20&noFilterSet=true&offset={i}'

    req = requests.get(url, headers=headers)

    result = req.content

    soup = BeautifulSoup(result, 'lxml')

    res = soup.find_all('div', class_="col-xs-4 col-sm-3 col-md-2 bt-slide")

    for count, card in enumerate(res, 1):
        sleep(random.randint(1, 3))
        card_id = 'https://www.bundestag.de' + card.find('a').get('href')
        all_info_card(card_id)      # вызов функции по собиранию инфы с карточки пользователя

        print(f'Парсинг {count} пользователя завершен')
    print(f'парсинг {i} страницы завершен')


csv_file(all_json_dict)
json_file(all_json_dict)


