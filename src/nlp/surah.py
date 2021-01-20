import scrapy
import os

LOCAL_FILENAME = 'original_surah.html'
LOCAL_FOLDER='nlp'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class SurahSpider(scrapy.Spider):
    name = 'Surah Al-Baqara'
    start_urls = [f'file://{BASE_DIR}/{LOCAL_FOLDER}/{LOCAL_FILENAME}']

    def parse(self, response):
    	# print(response.css('.verse.p-3.my-3::attr(data-text)').extract())
    	for idx, verse in enumerate(response.css('.verse.p-3.my-3.border-bottom::attr(data-text)')):
        	yield {'line': verse.extract(), 'num': idx + 1}