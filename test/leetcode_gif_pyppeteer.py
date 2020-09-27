import asyncio
import os

import requests
from urllib import parse
from lxml import etree
from pyppeteer import launch


async def main():
    # 使用launch方法调用浏览器，其参数可以传递关键字参数也可以传递字典。
    browser = await launch(
        {'headless': True, 'args': ['--disable-infobars', '--window-size=1920,1080', '--no-sandbox']})
    # 打开一个页面
    page = await browser.newPage()
    # await page.setViewport({'width': 1920, 'height': 1080})   # 设置页面的大小
    # 打开链接
    await page.goto(
        "https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-by-leetcode-soluti/")
    page_content = await page.content()
    folder = await page.title()

    print(page_content)

    await page.close()
    await browser.close()

    page = etree.HTML(page_content)

    all_img = page.xpath("//img/@src")

    os.makedirs(folder, exist_ok=True)

    for img in all_img:
        with open(folder + "/" + parse.urlparse(img).path.split("/")[-1], "wb") as f:
            f.write(requests.get(img).content)


# 调用
asyncio.get_event_loop().run_until_complete(main())

