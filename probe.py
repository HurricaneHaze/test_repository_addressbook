import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = r'C:\Users\yus\Downloads\chrome_web_driver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=path)
driver.implicitly_wait(2)
driver.get('https://www.youtube.com/')
search = driver.find_elements_by_xpath('//*[@id="search"]')
input_txt = search[2]
input_txt.send_keys("Денчик грудные")
input_txt.send_keys(Keys.ENTER)

time.sleep(5)
driver.quit()
