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

    await page.setCookie(cookie)
    await page.goto(url)
    await page.evaluate(js1)
    await page.evaluate(js3)
    await page.evaluate(js4)
    await page.evaluate(js5)
    await page.waitFor(1000)
    # await page.waitForNavigation()
    await next(page)

async def next(page):
    res = await page.content()
    print(res)
    return res


url = 'https://i.51job.com/userset/my_51job.php'

cookie =   {'name': '51job', 'value': '', 'domain': '.51job.com', 'path': '/', 'expires': 1579846082.746126, 'size': 476, 'httpOnly': True, 'secure': False, 'session': False}
loop = asyncio.get_event_loop()
loop.run_until_complete(main(url,cookie))