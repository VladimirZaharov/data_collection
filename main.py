from pymongo import MongoClient
from lxml import html
import requests
import time


def add_vacancies(some_dict):
    client = MongoClient('localhost', 27017)
    db = client['news_db']
    news_collection = db.news_collection
    news_collection.insert_many(some_dict)

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
def request_to_mail(number):
    try:
        time.sleep(1)
        response = requests.get('https://mail.ru',
        headers = header
        )
        root = html.fromstring(response.text)

        link = root.xpath(
            f'//*[@id="grid:middle"]/div[2]/div[3]/div[1]/ul/li[{number}]//a/@href'
        )
        news_text = root.xpath(
            f'//*[@id="grid:middle"]/div[2]/div[3]/div[1]/ul/li[{number}]//a/text()'

        )
        news_dict = {
            'link': link,
            'news': news_text
        }
        return news_dict
    except:
        print('Ошибка запроса')


for i in range(6):
    result = request_to_mail(i)
    add_vacancies(result)
