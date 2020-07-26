import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

path = r'C:\Users\yus\Downloads\chrome_web_driver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=path)
driver.get('https://www.youtube.com/')
wait = WebDriverWait(driver, 2)

element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#search')))
element.send_keys("Денчик грудные")
element.send_keys(Keys.ENTER)

# search = driver.find_element_by_xpath('//*[@id="search"]')
# search = driver.find_element_by_id('search')
# search = driver.find_element_by_css_selector('#search')
# search.send_keys("Денчик грудные")
# search.send_keys(Keys.ENTER)
# search_button = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
# search_button.click()

driver.implicitly_wait(10)
driver.quit()
