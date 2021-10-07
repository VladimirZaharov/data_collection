from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                    'Authorization':'Basic cG9zdG1hbjpwYXNzd29yZA=='}
req = requests.get('https://tula.hh.ru/search/vacancy?text=python+developer', headers=headers).text
soup = bs(req, 'html.parser')
vacancy = soup.select(".vacancy-serp-item__row_header")
vacancy_dict = {}
for i, pos in enumerate(vacancy):
    vacancy_name = pos.find(attrs={'data-qa': 'vacancy-serp__vacancy-title'})
    vacancy_name_txt = vacancy_name.text
    vacancy_comp = pos.find(attrs={'data-qa': "vacancy-serp__vacancy-compensation"})
    try:
        vacancy_comp_txt = vacancy_comp.text
    except AttributeError:
        vacancy_comp_txt = 'не указано'
    vacancy_href = pos.find(attrs={'data-qa': 'vacancy-serp__vacancy-title'})
    vacancy_href_attr = vacancy_href.attrs['href']
    vacancy_dict[i+1] = [vacancy_name_txt, vacancy_comp_txt, vacancy_href_attr]
print(vacancy_dict)
frame = pd.DataFrame(vacancy_dict)
