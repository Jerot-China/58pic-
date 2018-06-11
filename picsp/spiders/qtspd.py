# -*- coding: utf-8 -*-
import scrapy
from picsp.items import PicspItem
from scrapy.http import Request

class QtspdSpider(scrapy.Spider):
    name = 'qtspd'
    allowed_domains = ['58pic.com']
    start_urls = ['http://www.58pic.com/piccate/3-0-0-default-0_2_0_0_default_0-1.html']
    def start_requsets(self):
        global headers
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Accept': '*/*',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        }
        url = 'http://www.58pic.com/piccate/3-0-0-default-0_2_0_0_default_0-1.html'
        yield Request(url, headers=headers)

    def parse(self, response):
        item = PicspItem()
        shops = response.xpath("//div[@class='flow-item qt-card-primary']")
        # 获取最大页数
        page = response.xpath("//div[@class='qt-pagination']/a[1]/text()").extract()[0]
        pic_name = []
        pic_url = []
        for shop in shops:
            name = shop.xpath("./p/span[2]/text()").extract()
            pic_name.append(name)
            original_url = shop.xpath("./div/a/img/@data-original").extract()
            src_url = shop.xpath("./div/a/img/@src").extract()
            if original_url==[]:
                pic_url.append(src_url)
            else:
                pic_url.append(original_url)
        item['pic_name'] = pic_name
        item['pic_url'] = pic_url
        # 根据获取的页数来循环爬取
        for i in range(2,int(page)+1):
            next_url = "http://www.58pic.com/piccate/3-0-0-default-0_2_0_0_default_0-"+ str(i) +".html"
            print(next_url)
            yield Request(next_url, callback=self.parse, headers=headers)
        yield item


        
