from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
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
keyword = input("검색어를 입력해 주세요: ")
url= f'https://www.coupang.com/np/search?q={keyword}'
driver.get(url)


html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
items = soup.select('.search-product-wrap.adjust-spacing')

print(len(items))


ad_count = 0
for rank,item in enumerate(items,1):
    isad = item.select_one('.ad-badge-text')
    title = item.select_one('.name').text
    price = item.select_one('.price-value').text
    rocket = item.select_one('.badge.rocket')
    link =  item.find_parent('a').get('href')
    img =  item.select_one('.search-product-wrap-img')
    if isad:
        ad_count+=1
    else:
        print(rank-ad_count, '위')
        print('이름: '+ title)
        print('가격: '+price+'원')
        if img.get('data-img-src'): 
            img=img.get('data-img-src')
        else:
            img= img.get('src')
        img=img.replace('230x230ex','600x600ex')
        print('제품 사진'+f'https:{img}')
        print('로켓배송: ', 'Yes' if rocket else 'No')
        print('링크: ','https://www.coupang.com'+link)
        print('='*10)
        if rank-ad_count ==10:
            break

driver.quit()

now = datetime.now()

today = f"{now.year}년 {now.month}월 {now.day}일"
file_name = 'index.html'
title_text= "쿠팡 스크래핑"
main_text = f"""<a href='{link}'target='_blank'>
	<div class='image main'>
	<img src='{img}' alt='제품 이미지' />
    </div>
	<h2>{rank}위 제품명: {title}</h2>
    <b>{price}원</b>
    </a>"""
html_text =f"""<!DOCTYPE HTML>
<html>
	<head>
		<title>{title_text}</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<link rel="stylesheet" href="assets/css/main.css" />
		<noscript><link rel="stylesheet" href="assets/css/noscript.css" /></noscript>
	</head>
	<body class="is-preload">

		<!-- Wrapper -->
			<div id="wrapper">
				<!-- Header -->
					<header id="header">
						<a href="index.html" class="logo">Massively</a>
					</header>
				<!-- Main -->
					<div id="main">
						<!-- Post -->
							<section class="post">
								<header class="major">
									<span class="date">{today}</span>
									<h1>{title_text}</h1>
								</header>
                                {main_text}
							</section>
					</div>
			</div>

		<!-- Scripts -->
			<script src="assets/js/jquery.min.js"></script>
			<script src="assets/js/jquery.scrollex.min.js"></script>
			<script src="assets/js/jquery.scrolly.min.js"></script>
			<script src="assets/js/browser.min.js"></script>
			<script src="assets/js/breakpoints.min.js"></script>
			<script src="assets/js/util.js"></script>
			<script src="assets/js/main.js"></script>

	</body>
</html>"""


with open(f'{file_name}', 'w', encoding='utf-8') as f:
    f.write(html_text)
    