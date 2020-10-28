import requests
import time
import pandas as pd
import asyncio
from pyppeteer import launch


async def get_car_detail_infos(browser, url):
    # 打开一个页面
    page = await browser.newPage()
    await page.setViewport({'width': 1920, 'height': 1080})  # 设置页面的大小
    await page.goto(url)
    await page.click(selector="#__next > main > section > section.jsx-2449301772.box.clearfix > section.jsx-4139250591.fl > span:nth-child(4)")
    d1 = await page.waitForXPath("""//*[@id="wrapper"]/div[2]/div/div[1]""")
    print(await page.evaluate('element => element.textContent', d1))
    print(dir(d1))
    # print(await page.xpath("""//*[@id="wrapper"]/div[2]/div/div[4]"""))
    # await page.close()



def read_car_list():
    df = pd.read_excel("car_list.xlsx")
    for _, d in df.iterrows():
        yield dict(d)


async def main():
    # 使用launch方法调用浏览器，其参数可以传递关键字参数也可以传递字典。
    browser = await launch(
        {'headless': False, 'args': ['--disable-infobars', '--window-size=1920,1080', '--no-sandbox']})
    for one_car in read_car_list():
        url = "https://www.dcdapp.com/auto/series/{}".format(one_car["id"])
        await get_car_detail_infos(browser, url)
        break

    while True:
        time.sleep(10)
    # await browser.close()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
