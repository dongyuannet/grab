# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
import time
import requests
from scrapy.http import HtmlResponse
from selenium.webdriver.common.keys import Keys

class MmSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class MmDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

class ZhihuseSpiderMiddleware(object):
    """docstring for ClassName"""
    def process_request(self, request,spider):
        request.meta['proxy'] = 'http://42.202.23.9:808'
        if request.url != 'https://www.zhihu.com/signup':
            return None
        # 创建chrome参数对象
        opt = webdriver.ChromeOptions()
        # 把chrome设置成无界面模式，不论windows还是linux都可以，自动适配对应参数
        # opt.headless = True
        # 创建chrome无界面对象
        driver = webdriver.Chrome(options=opt)
        driver.get(request.url)

        username = request.meta['username']
        password = request.meta['password']
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[2]/span').click()
        time.sleep(1)
        driver.find_element_by_xpath('//input[@name="username"]').send_keys(username)
        driver.find_element_by_xpath('//input[@name="password"]').send_keys(password)
        # driver.find_element_by_xpath('//button[@type="submit"]').send_keys(Keys.SPACE)
        # driver.find_element_by_xpath('//button[type="submit"]').click()


        # driver.find_element_by_xpath('//button[@type="submit"]').click()
        # time.sleep(1)
        # driver.find_element_by_xpath('//button[@type="submit"]').click()
        # time.sleep(1)
        # driver.find_element_by_xpath('//button[@type="submit"]').click()
        return None
        return HtmlResponse(url=request.url, body=driver.title, request=request, encoding='utf-8', status=200)

class SeleniumSpiderMiddleware(object):
    """docstring for ClassName"""
    def process_request(self, request,spider):
        if request.url != 'https://login.51job.com/login.php?lang=c':
            return None
        # 创建chrome参数对象
        opt = webdriver.ChromeOptions()
        # 把chrome设置成无界面模式，不论windows还是linux都可以，自动适配对应参数
        opt.headless = True
        # 创建chrome无界面对象
        driver = webdriver.Chrome(options=opt)
        driver.get(request.url)
        username = request.meta['username']
        password = request.meta['password']
        time.sleep(3)
        driver.find_element_by_id('loginname').send_keys(username)
        driver.find_element_by_id('password').send_keys(password)
        driver.find_element_by_xpath('//*[@id="login_btn"]').click()
        driver.find_element_by_xpath('//*[@id="login_btn"]').click()
        time.sleep(3)
        return HtmlResponse(url=request.url, body=driver.title, request=request, encoding='gbk', status=200)
        
