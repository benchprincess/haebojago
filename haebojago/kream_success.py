from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from pymongo import MongoClient

# MongoDB 연결
client = MongoClient('mongodb://localhost:27017/')
db = client['kreamadmin']
products_collection = db['products']

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

options = Options()
options.add_argument(f"user-agent={user_agent}")
options.add_experimental_option('detach', True)
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_experimental_option('excludeSwitches', ['enable-automation'])

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

url = "https://kream.co.kr/"
driver.get(url)
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, ".search_btn_box").click()
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys("핑크")
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(Keys.ENTER)
time.sleep(1)

for i in range(10):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(0.3)
    driver.save_screenshot("/Users/jiwon/Desktop/oz/benchprincess/haebojago/crawling/kream_img/supreme"+str(i)+".png")

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

items = soup.select(".product_card")

for i in items:
    product_name = i.select_one(".translated_name")

    if "비비안" in product_name.text:
        product_brand = i.select_one(".product_info_brand.brand")
        product_price = i.select_one(".amount")
        product_wish = i.select_one(".text")

        # MongoDB에 저장
        product_data = {
            'name': product_name.text,
            'brand': product_brand.text,
            'price': product_price.text,
            'wish': product_wish.text,
        }
        products_collection.insert_one(product_data)

# 데이터 출력
cursor = products_collection.find({})
num = 1
for document in cursor:
    print(f"[{num}]")
    print(f"브랜드 : {document['brand']}")
    print(f"제품명 :  {document['name']}")
    print(f"가  격 : {document['price']}")
    print(f"저  장 :  {document['wish']}")
    print()

    num += 1

# driver.quit()
