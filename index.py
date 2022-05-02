from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(
    "/Users/nob1mac/dev.proglearning/lesson-webscraping-python/chromedriver"
)
driver.get("https://proglab.nbr41.com/")  # open the page

print("...open")

# chrome でDOMからselectorを取得しておく（右クリ>Copy）
link_button = driver.find_element_by_xpath(
    '//*[@id="__next"]/div/header/div/div[2]/div/a'
)
link_button.click()

print("...move form page")

sleep(0.5)

for i in range(1, 5):
    sleep(0.2)
    xpath = '//*[@id="__next"]/div/main/div/div[2]/div[1]/div[' + str(i) + "]/i"
    checkbox = driver.find_element_by_xpath(xpath)
    checkbox.click()

print("...all checked")


open_form_button = driver.find_element_by_xpath(
    '//*[@id="__next"]/div/main/div/div[2]/div[2]/button'
)
open_form_button.click()

print("...open form")

sleep(1)

iframe = driver.find_element_by_xpath(
    '//*[@id="__next"]/div/main/div/div[2]/div[2]/div/iframe'
)
url = iframe.get_attribute("src")
print(url)
driver.get(url)  # open the page

email_form = driver.find_element_by_xpath(
    '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input'
)
email_form.send_keys("watashinoaddressda@gmail.com")

sleep(2)
driver.close()  # 自動で閉じる
