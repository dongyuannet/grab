import asyncio
import time
from pyppeteer.launcher import launch
from alifunc import mouse_slide, input_time_random
from exe_js import js1, js3, js4, js5
 
 
async def main(url,cookie):
    browser = await launch({'headless': False, 'dumpio': True,'args': ['--disable-extensions',
        '--hide-scrollbars',
        '--disable-bundled-ppapi-flash',
        '--mute-audio',
        '--no-sandbox',
        '--disable-setuid-sandbox',
        '--disable-gpu'] })
    page = await browser.newPage()
    await page.setUserAgent(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299')
 
    await page.goto(url)
    await page.evaluate(js1)
    await page.evaluate(js3)
    await page.evaluate(js4)
    await page.evaluate(js5)
    await page.next(page)
    
   
 
 
# 获取登录后cookie
async def next(page):
    res = await page.title()
    print(res)
    return res
 

cookie =  {'name': 'cookie2', 'value': '', 'domain': '.taobao.com', 'path': '/', 'expires': -1, 'size': 39, 'httpOnly': True, 'secure': False, 'session': True},
url = 'https://i.taobao.com/my_taobao.htm'
loop = asyncio.get_event_loop()
loop.run_until_complete(main( url,cookie))
