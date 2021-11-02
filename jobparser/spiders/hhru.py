# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse

from jobparser.items import JobparserItem


class HhruSpider(scrapy.Spider):
    name = 'hhru'
    allowed_domains = ['hh.ru']
    start_urls = ['https://tula.hh.ru/search/vacancy?area=&st=searchVacancy&text=python']

    def parse(self, response: HtmlResponse):
        next_page = 'https://tula.hh.ru' \
                    + response.css('a[class="bloko-button"][data-qa="pager-next"]').attrib['href']
        print(next_page)
        response.follow(next_page, callback=self.parse)
        vacansy = response.css(
            'div.vacancy-serp div.vacancy-serp-item div.vacancy-serp-item__row_header '
            'a.bloko-link::attr(href)'
        ).extract()
        for link in vacansy:
            yield response.follow(link, callback=self.vacansy_parse)

        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def vacansy_parse(self, response: HtmlResponse):
        vacancy_name = response.css('h1[data-qa="vacancy-title"]::text').getall()
        salary_from = response.xpath('//*[@id="HH-React-Root"]/div/div/div/div/div[1]/div[1]/div/div/div[2]/span[1]/text()[2]').get()
        salary_to = response.xpath('//*[@id="HH-React-Root"]/div/div/div/div/div[1]/div[1]/div/div/div[2]/span[1]/text()[4]').get()
        vacancy_link = response.xpath('/html/head/link[9]').get()
        vacancy_site = 'HH.ru'
        print('\nНазвание вакансии: ', vacancy_name)
        print('Зарплата от: ', salary_from)
        print('Зарплата до: ', salary_to)
        print('Ссылка на вакансию: ', vacancy_link)
        print('Взято с сайта: ', vacancy_site)



        yield JobparserItem(vacancy_name=vacancy_name, salary_from=salary_from, salary_to=salary_to, vacancy_link=vacancy_link, vacancy_site=vacancy_site)
