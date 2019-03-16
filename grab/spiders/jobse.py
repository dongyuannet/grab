# -*- coding: utf-8 -*-
import scrapy
from scrapy import FormRequest,Request


class LoginSpider(scrapy.Spider):
    name = "jobse"
    allowed_domains = ["51job.com"]
    start_urls = ['https://i.51job.com/userset/my_51job.php']
    login_url = 'https://login.51job.com/login.php?lang=c'

    def parse(self, response):
        print('6666666')

    def start_requests(self):
        yield scrapy.Request(self.login_url,callback=self.login,meta={'username':'','password':''})

    def login(self,response):
        print(response.body.decode('gbk'))
    