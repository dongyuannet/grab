# -*- coding: utf-8 -*-
import scrapy
from scrapy import FormRequest,Request


class LoginSpider(scrapy.Spider):
    name = "login"
    allowed_domains = ["example.webscraping.com"]
    start_urls = ['http://example.webscraping.com/user/profile']
    login_url = 'http://example.webscraping.com/places/default/user/login'

    def parse(self, response):
        print('6666666')

    def start_requests(self):
        yield scrapy.Request(self.login_url,callback=self.login)

    def login(self,response):
        formdata = {
            'email':'liushuo@webscraping.com','password':'12345678'}
        yield FormRequest.from_response(response,formdata=formdata,
                                        callback=self.parse_login)
    def parse_login(self,response):
        print('Welcome Liu' in response.text)
        return None
        # print('>>>>>>>>'+response.text)
        # if 'Welcome Liu' in response.text:
        #     yield from super().start_requests()