import requests
from bs4 import BeautifulSoup

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options

import psycopg2

chrome_options = Options()

chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")


url_google = 'https://www.google.com/search?q=ozon&newwindow=1&sca_esv=562531629&source=hp&ei=qeH1ZPLZPLqlwPAPlt6dkAY&iflsig=AD69kcEAAAAAZPXvusBj3jUBan8BseIbknFruv1vQiUE&ved=0ahUKEwiy0vDUjZGBAxW6EhAIHRZvB2IQ4dUDCAk&uact=5&oq=ozon&gs_lp=Egdnd3Mtd2l6IgRvem9uMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyCBAAGIAEGLEDMggQABiABBixAzIIEAAYgAQYsQMyCBAAGIAEGLEDMggQABiABBixAzILEAAYgAQYsQMYgwEyCxAAGIAEGLEDGIMBMggQABiABBixA0j2DVCfB1iWC3ABeACQAQCYATegAdABqgEBNLgBA8gBAPgBAagCCsICEBAAGAMYjwEY6gIYjAMY5QLCAhAQLhgDGI8BGOoCGIwDGOUCwgIREC4YgAQYsQMYgwEYxwEY0QPCAgUQABiABMICDhAuGIAEGLEDGMcBGNEDwgILEAAYigUYsQMYgwHCAgsQLhiKBRixAxiDAcICCxAuGIAEGLEDGIMB&sclient=gws-wiz'


browser = webdriver.Chrome(options=chrome_options)

url_ozon = 'https://www.ozon.ru/category/korm-dlya-sobak-12302/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=%D0%9A%D0%BE%D1%80%D0%BC+%D0%B4%D0%BB%D1%8F+%D1%81%D0%BE%D0%B1%D0%B0%D0%BA'

url_ozon2 = 'https://www.ozon.ru'


browser.get(url_google)
time.sleep(2)

#age_confirm_btn = browser.find_element(By.XPATH, "//div[@class='OrganicTitleContentSpan organic__title']")
ozon_btn = browser.find_elements(By.TAG_NAME, "h3")
ozon_btn[0].click()

browser.switch_to.window(browser.window_handles[1])
del ozon_btn
time.sleep(2)

browser.execute_script("window.scrollTo(0, 3000)")
time.sleep(5)

products = browser.find_elements(By.XPATH, "//div[@class='d3w z3ab a4zb']")

print(len(products))

print(products[0])
print(products[0].text)

# text_field = browser.find_element(By.XPATH, "//input[@name='text']")
# time.sleep(5)

# text_field.send_keys("Корм для собак")
# time.sleep(1)
#
# search_btn = browser.find_element(By.XPATH, "//div[@class='u0w a2421-a a2421-a3']")
# search_btn.click()
# time.sleep(5)
