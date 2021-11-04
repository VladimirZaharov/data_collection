from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client.Discounts
collection = db.DiscountsCollection

serv = Service("C:\python_courses\data_collection\chromedriver.exe")
driver = webdriver.Chrome(service=serv)
driver.implicitly_wait(10)
driver.get("https://www.citilink.ru")
assert "Ситилинк" in driver.title
start_page = driver.find_elements(by=By.XPATH, value="/html/body/div[2]/div[2]/main/div/div[1]/div/div[1]/div/div[1]/div[1]/div")
count = 0
for i in start_page:
    if count <= 1:
        count+=1
        continue
    else:
        temp = i.get_attribute('data-params')
        link = driver.find_element(by=By.XPATH, value=f"/html/body/div[2]/div[2]/main/div/div[1]/div/div[1]/div/div[1]/div[1]/div[@data-params='{temp}']/a").get_attribute('href')
        number = driver.find_element(by=By.XPATH, value=f"/html/body/div[2]/div[2]/main/div/div[1]/div/div[1]/div/div[1]/div[1]/div[@data-params='{temp}']").get_attribute('data-gtm-position')
        temp_dict = {
            'number_id': number,
            'link': link,
            'shop': 'citilink'
        }
        collection.insert_one(temp_dict)
driver.close()
