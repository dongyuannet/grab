# -*- coding: utf-8 -*-
import scrapy


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    login_url = 'https://www.zhihu.com/signup'
    start_urls = ['https://www.51job.com']
    showindex = 'https://www.zhihu.com/api/v3/oauth/sign_in'
    def start_requests(self):

        yield scrapy.Request(self.login_url,callback=self.login,meta={},dont_filter = False)
        pass
    def login(self,response):
       

        formdata = {'username':'','password':''}
        yield scrapy.FormRequest(self.showindex,formdata=formdata,callback=self.parse_login,meta={},dont_filter = False)
        pass

    def parse_login(self,response):
        
        Cookie2 = response.request.headers.getlist('Cookie')
        print(Cookie2)

        
