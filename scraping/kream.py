from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import pymysql
# 클래스, 아이디를 css_selector를 이용해서 원하는 값을 가져오기 위한 패키지
from selenium.webdriver.common.by import By # by문법

#키보드의 입력 형태를 코드로 작성하기 위해 사용하는 패키지
from selenium.webdriver.common.keys import Keys

header_user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"

options_ = Options() # 인스턴스화
options_.add_argument(f"User-Agent={header_user}")
options_.add_experimental_option("detach",True) # 자동으로 브라우저가 종료되지 않게 
options_.add_experimental_option("excludeSwitches",["enable-logging"])

driver = webdriver.Chrome(options=options_)
url ="https://kream.co.kr/"
driver.get(url)

# 돋보기 누르기 
driver.find_element(By.CSS_SELECTOR, ".btn_search.header-search-button.search-button-margin").click()

# 검색어 입력창 
# keyword = input("검색어를 입력하세요: ")
driver.find_element(By.CSS_SELECTOR,".input_search.show_placeholder_on_focus").send_keys("슈프림")
driver.find_element(By.CSS_SELECTOR,".input_search.show_placeholder_on_focus").send_keys(Keys.ENTER)

for i in range(10):
    driver.find_element(By.TAG_NAME,"body").send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)

html = driver.page_source
soup = BeautifulSoup(html,"html.parser")

items = soup.select(".item_inner")

product_list = []

for item in items:
    
    product_name = item.select_one(".translated_name").text
    if "후드" in product_name:
        category = "상의"
        brand = item.select_one(".product_info_brand.brand").text
        price = item.select_one(".amount").text
        product = [category,brand,product_name, price]
        product_list.append(product)

        print(category)
        print(brand.lstrip())
        print(product_name)
        print(price)

driver.quit()

connection = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='1234',
    db='kream',
    charset='utf8mb4',
    )

#mysql에 데이터를 넣거나 가져올 때 쿼리문을 실행시켜주는 등 
#데이터베이스와의 소통을 도와주는 역할
connection.cursor()

def execute_query(connection, query, args=None):
    with connection.cursor() as cursor:
        cursor.execute(query, args or ())
        if query.strip().upper().startswith('SELECT'):
            return cursor.fetchall()
        else:
            connection.commit()
for i in product_list:
    execute_query(connection,"INSERT INTO kream (category, brand, product_name, price) VALUES (%s,%s,%s,%s)",(i[0],i[1],i[2],i[3]))