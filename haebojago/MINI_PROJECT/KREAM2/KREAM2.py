from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pymysql

# 데이터 베이스 연결
conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '900326',
    db = 'kream',
    charset = 'utf8mb4',
)
cur = conn.cursor()

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

driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys("비비안")
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(Keys.ENTER)
time.sleep(1)

base_url = "https://kream.co.kr/search?shop_category_id="
bag_id = 9
bag_url = f"{base_url}{bag_id}"
driver.get(bag_url)
time.sleep(1)

for i in range(10):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

items = soup.select(".search_result_item product")


for i in items:
    product_name = i.select_one(".translated_name").text
    product_brand = i.select_one(".product_info_brand.brand").text
    product_price = i.select_one(".amount").text
    product_wish = i.find("wish_figure", {"class":"text"}).text
    product_review = i.find("review_figure", {"class":"text"}).text
    sql = "INSERT INTO product (product_name, product_brand, product_price, product_wish, product_review) VALUES (%s, %s, %s, %s, %s)"
    cur.execute(sql,(product_name, product_brand, product_price, product_wish, product_review))
    conn.commit() 

# driver.quit()