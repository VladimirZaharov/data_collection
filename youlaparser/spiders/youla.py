import scrapy
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader

from youlaparser.items import YoulaparserItem


class YoulaSpider(scrapy.Spider):
	name = 'youla'
	allowed_domains = ['youla.ru']
	start_urls = ['https://youla.ru/tula/zhivotnye/sobaki']

	def parse(self, response):
		ads_links = response.xpath('//*[@id="app"]/div[1]/div[3]/div/div/main/section/div/ul//@href').extract()
		for link in ads_links:
			yield response.follow(link, callback=self.parse_ads)

	def parse_ads(self, response: HtmlResponse):
		name = response.xpath('//*[@id="app"]/div[1]/div[4]/main/div/div[2]/div[2]/div/section[1]/div/div[1]/div/div[1]/h2/text()').extract()
		species = response.xpath('//*[@id="app"]/div[1]/div[4]/main/div/div[2]/div[3]/div/section[1]/div/div[1]/div/ul/li[3]/dl/dd[3]/text()').extract()
		photos = response.xpath('//*[@id="app"]/div[1]/div[4]/main/div/div[2]/div[2]/div/section[1]/div/div[1]/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div[3]/div[1]/div/img/@src').extract()
		location = response.xpath('//*[@id="app"]/div[1]/div[4]/main/div/div[2]/div[3]/div/section[1]/div/div[1]/div/ul/li[1]/dd/div/div/span/text()').extract()
		print(name, photos, species, location)
		yield YoulaparserItem(name=name, photos=photos,species=species, location=location)
