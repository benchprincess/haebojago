from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 키보드 입려이라던지 어떠한 동작과 관련된 기능을 쓰기 위한 패키지
from selenium.webdriver.common.keys import Keys
# 클래스, 아이디, css_select를 이용하고자 할 때
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

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

driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys("슈프림")
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(Keys.ENTER)
time.sleep(1)


for i in range(20):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(0.3)
    driver.save_screenshot("/Users/jiwon/Desktop/oz/benchprincess/haebojago/crawling/kream_img/supreme"+str(i)+".png")

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

items = soup.select(".item_inner")

num = 1 
for i in items:
    product_name = i.select_one(".translated_name")

    if "후드" in product_name.text:
        product_brand = i.select_one(".product_info_brand.brand")
        product_price = i.select_one(".amount")
        product_wish = i.select_one(".text")

    print(f"[{num}]")
    print(f"브랜드 : {product_brand.text}")
    print(f"제품명 :  {product_name.text}")
    print(f"가  격 : {product_price.text}")
    print(f"리  뷰 : {product_wish.text}")
    print()

    num += 1
# driver.quit()