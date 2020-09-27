import os

import requests
from urllib import parse
from lxml import etree
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                          desired_capabilities=DesiredCapabilities.CHROME)

url = "https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-by-leetcode-soluti/"

driver.get(url)
folder = driver.title
page_content = driver.page_source

driver.close()

page = etree.HTML(page_content)

all_img = page.xpath("//img/@src")

os.makedirs(folder, exist_ok=True)

for img in all_img:
    with open(folder + "/" + parse.urlparse(img).path.split("/")[-1], "wb") as f:
        f.write(requests.get(img).content)
