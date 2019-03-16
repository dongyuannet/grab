import asyncio
import time
from pyppeteer.launcher import launch
from alifunc import mouse_slide, input_time_random
from exe_js import js1, js3, js4, js5
# https://i.51job.com/userset/my_51job.php
async def main(username, pwd, url):

    browser = await launch({'headless': False, 'dumpio': True,'args': ['--no-sandbox'] })
    page = await browser.newPage()
    await page.setUserAgent(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299')
 
    await page.goto(url)
    await page.evaluate(js1)
    await page.evaluate(js3)
    await page.evaluate(js4)
    await page.evaluate(js5)
    time.sleep(1)
    await page.type('#loginname', username, {'delay': input_time_random() - 100})
    await page.type('#password', pwd, {'delay': input_time_random()-50})
    await page.click('#login_btn')
    await page.click('#login_btn')
    await page.waitFor(20)
    await page.waitForNavigation()
    await get_cookie(page)

async def get_cookie(page):
    res = await page.content()
    cookies_list = await page.cookies()
    print(cookies_list)
    cookies = ''
    for cookie in cookies_list:
        str_cookie = '{0}={1};'
        str_cookie = str_cookie.format(cookie.get('name'), cookie.get('value'))
        cookies += str_cookie
    print(cookies)
    time.sleep(10)
    return res

username = ''
pwd = ''
url = 'https://login.51job.com/login.php'
loop = asyncio.get_event_loop()
loop.run_until_complete(main(username, pwd, url))