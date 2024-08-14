import random
import time

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=chrome_options)

url = "" # 请在这里输入你的问卷url

for i in range(100):
    driver.get(url)

    dx_div = driver.find_elements(By.CSS_SELECTOR, ".field.ui-field-contain")

    for each_dx_div in dx_div:
        xxks = each_dx_div.find_elements(By.CSS_SELECTOR, ".ui-checkbox")

        xxks_counts = len(xxks) - 1 # 除掉其他剩下的个数

        choose_counts = random.randint(1, xxks_counts) # 选中的个数

        choose_index = random.sample(range(0, xxks_counts), choose_counts)

        for index in choose_index:
            try:
                xxks[index].click()
            except selenium.common.exceptions.ElementClickInterceptedException:
                try:
                    choose_box = xxks[index].find_element(By.CSS_SELECTOR, ".jqcheck")
                    choose_box.click()
                except selenium.common.exceptions.ElementClickInterceptedException:
                    div_box = xxks[index].find_element(By.CSS_SELECTOR, ".label")
                    div_box.click()

    commit = driver.find_element(By.ID, "ctlNext")
    commit.click()

    time.sleep(5)
