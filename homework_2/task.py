from bs4 import BeautifulSoup as bs
import requests
import views
from pymongo import MongoClient

def vacancy_search():
    headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                        'Authorization':'Basic cG9zdG1hbjpwYXNzd29yZA=='}
    req = requests.get('https://tula.hh.ru/search/vacancy?text=python+developer', headers=headers).text
    soup = bs(req, 'html.parser')
    vacancy = soup.select(".vacancy-serp-item__row_header")
    vacancy_list = []
    for i, pos in enumerate(vacancy):
        vacancy_dict = {}
        vacancy_name = pos.find(attrs={'data-qa': 'vacancy-serp__vacancy-title'})
        vacancy_name_txt = vacancy_name.text
        vacancy_comp = pos.find(attrs={'data-qa': "vacancy-serp__vacancy-compensation"})
        try:
            vacancy_comp_txt = vacancy_comp.text
        except AttributeError:
            vacancy_comp_txt = 'не указано'
        vacancy_href = pos.find(attrs={'data-qa': 'vacancy-serp__vacancy-title'})
        vacancy_href_attr = vacancy_href.attrs['href']
        vacancy_dict['vacancy name'] = vacancy_name_txt
        vacancy_dict['salary'] = vacancy_comp_txt
        vacancy_dict['vacancy link'] = vacancy_href_attr
        vacancy_list.append(vacancy_dict)
    return vacancy_list

def add_new_vacancies():
    client = MongoClient('localhost', 27017)
    db = client['vacancy_db']
    collection = db.vacancy_collection
    new_collection = vacancy_search()
    for vacancy in new_collection:
        search_result = collection.find({'vacancy link': vacancy})
        if search_result.isExhausted():
            collection.insert_one(vacancy)

