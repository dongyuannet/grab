# -*- coding: utf-8 -*-
import scrapy
import urllib.parse
import time

class JobSpider(scrapy.Spider):
    name = 'job'
    allowed_domains = ['51job.com']
    login_url = 'https://login.51job.com/login.php'
    start_urls = ['https://www.51job.com']
    showindex = 'https://i.51job.com/userset/my_51job.php'
    def start_requests(self):
        formdata = {'loginname':'','password':'',"from_domain":'i','action':'save','lang':'c','isread':'on'}
        yield scrapy.FormRequest(url = self.login_url,formdata=formdata,callback=None,meta={},dont_filter = False,method='POST')
        pass
   
    def parse(self, response):
        print('666666')
        print('石鑫' in response.text)
        pass
