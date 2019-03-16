# -*- coding: utf-8 -*-
import scrapy
from scrapy import FormRequest,Request


class ZhihuseSpider(scrapy.Spider):
    name = "zhihuse"
    allowed_domains = ["zhihu.com"]
    start_urls = []
    login_url = 'https://www.zhihu.com/signup'

    def parse(self, response):
        print('6666666')

    def start_requests(self):
        yield scrapy.Request(self.login_url,callback=self.login,meta={'username':'','password':''})

    def login(self,response):
        print(response.body.decode('utf-8'))
    