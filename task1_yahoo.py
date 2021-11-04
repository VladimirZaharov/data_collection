from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from pymongo import MongoClient
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


client = MongoClient('localhost', 27017)
db = client.MailDataBase
collection = db.MailCollection

serv = Service("C:\python_courses\data_collection\chromedriver.exe")
driver = webdriver.Chrome(service=serv)
driver.implicitly_wait(10)
driver.get("https://www.yahoo.com")
assert "Yahoo" in driver.title
start_page = driver.find_element(by=By.ID, value="ybarMailLink")
start_page.click()

elem = driver.find_element(by=By.ID, value='login-username')
assert "No results found." not in driver.page_source
elem.send_keys('zaharovvladimir100@yahoo.com')
login_page = driver.find_element(by=By.ID, value='login-signin')
login_page.click()
password_page = driver.find_element(by=By.ID, value='login-passwd')
password_page.send_keys('fghjkl_345')
password_page_btn = driver.find_element(by=By.ID, value='login-signin')
password_page_btn.click()
accept_page = driver.find_elements(by=By.XPATH, value='//*[@id="mail-app-component"]/div/div/div[2]/div/div/div[2]/div/div[1]/ul/li')
count = 0
for i in accept_page:
    if count == 0:
        count+=1
        continue
    else:
        i.click()
        theme_message = driver.find_element(By.XPATH, '//*[@id="mail-app-component"]/div/div[2]/div[1]/header/div[2]/span/span').text
        from_message = driver.find_element(By.XPATH, '//*[@id="mail-app-component"]/div/div[2]/div[2]/ul/li/div/header/div[2]/div[1]').text
        date_message = driver.find_element(By.XPATH, '//*[@id="mail-app-component"]/div/div[2]/div[2]/ul/li/div/header/div[4]/span').text
        text_message = driver.find_element(By.XPATH, '//*[@id="mail-app-component"]/div/div[2]/div[2]/ul/li/div/div/div[1]').text
        dict_message = {
            'тема': theme_message,
            'от кого': from_message,
            'дата': date_message,
            'текст': text_message
        }
        collection.insert_one(dict_message)
        back = driver.find_element(By.XPATH, '//*[@id="mail-app-component"]/div/div[1]/button/span/span')
        back.click()
driver.close()
