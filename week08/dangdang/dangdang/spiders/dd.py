import scrapy
from dangdang.items import DangdangItem

class DdSpider(scrapy.Spider):
    name = 'dd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/cp01.54.06.00.00.00.html']

    def parse(self, response):
        item = DangdangItem()
        item["title"]=response.xpath("//a[@class='pic']/@title").extract()
        item["price"] = response.xpath("//span[@class='search_now_price']/text()").extract()
        print(item["title"])
        print(item["price"])
