from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv = Service("C:\python_courses\data_collection\chromedriver.exe")
driver = webdriver.Chrome(service=serv)
driver.get("https://www.google.com/intl/ru/gmail/about/")
assert "Gmail" in driver.title
start_page = driver.find_element(by=By.XPATH, value="/html/body/header/div/div/div/a[2]")
start_page.click()
elem = driver.find_element(by=By.ID, value='identifierId')
assert "No results found." not in driver.page_source
elem.send_keys('zaharovv281@gmail.com')
login_page = driver.find_element(by=By.XPATH, value='//*[@id="identifierNext"]/div/button/span')
login_page.click()
password_page = driver.find_element(by=By.XPATH, value='//*[@id="password"]/div[1]/div/div[1]/input')
password_page.send_keys('24101990yana')
password_page_btn = driver.find_element(by=By.XPATH, value='//*[@id="passwordNext"]/div/button/div[2]')
accept_page = driver.find_element(by=By.XPATH, value='//*[@id="yDmH0d"]/c-wiz[2]/c-wiz/div/div[1]/div/div/div/div[2]/div[3]/div/div[2]/div/div[2]')
accept_page.click()
# далее письма перебрать так и не понял как, формируются програмно
driver.close()

