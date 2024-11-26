# 오류

## 구문오류 
print("오류는 아주 사소한 것부터 발생합니다.")

## 에외처리 

### 조건문 사용한 예외처리 
# x, y = map(int, input("밑변과 높이를 입력해요").split(" "))
# print(f"삼각형의 넓이는 {x*y/2}입니다.")

# x, y =input("밑변과 높이를 입력해요").split(" ")
# if x.isdigit() and y.isdigit():
#     x, y = int(x), int(y)
#     print(f"삼각형의 넓이는 {x*y/2}입니다.")
# else:
#     print("정수를 넣어줘")
    



### try 예외처리

# x, y = map(int, input("밑변과 높이를 입력해요").split(" "))
# print(f"삼각형의 넓이는 {x*y/2}입니다.")

# x, y =input("밑변과 높이를 입력해요").split(" ")
# try:
#     x, y = int(x), int(y)
#     print(f"삼각형의 넓이는 {x*y/2}입니다.")
# except:
#     print("정수를 넣어줘")

## pass 키워드 조합

# list_input = ["1", "4", "3", "스파이"]
# catch_spy = []

# for i in list_input:
#     try:
#         int(i)
#         catch_spy.append(i)
#     except:
#         pass
# print(f'{list_input}내부에')
# print(f"{catch_spy}입니다.")

# try:
#     x, y = map(int, input("밑변과 높이 입력").split(" "))
#     print(f'삼각형의 높이는{x*y/2}')
# except Exception as exception:
#     print("에러 타입: ",type(exception))
#     print("에러: ",exception)

# 예외 구분하기 
# numbers = [23,12,32,141]
# try:
#     number_input= int(input("찾고싶은 값의 위치를 입력"))
#     print(f'{numbers[number_input]}위치해 있습니다.')
# except ValueError as e:
#     print("정수로 입력해주세요",e)
# except IndexError as e:
#     print("리스트의 범위를 벗어났습니다",e)

# 모듈
### 불러오기
#from math import sin, cos, ceil, floor
# from math import * # 너무 많이 부르기 때문에 느려질 수 있음

# print(sin(5))
# print(cos(5))
# print(ceil(5.6))
# print(floor(5.2))

# as 구문 
## 모듈을 가져올 때 이름의 충돌이 발생할 수 있다. 혹은 그냥 축약해서 사용하고 싶을 떄
# import math as m

#### os 모듈
# import os 
# print("현재 운영체제: ", os.name)
# print("현재 디렉토ㄹ;: ", os.getcwd())
# print("현재 폴더 정보: ", os.listdir())

# os.mkdir("asd") # 폴더 만들기
# os.rmdir("asd") # 폴더 삭제

# with open("asd.txt","w") as file:
#     file.write("수강생 ㅎㅇ")
# os.rename("asd.txt", "23") # 파일 만들고 쓰기
# os.remove("asd.txt") # 파일 제거 

# os.system("ls") # 맥
# os.system("dir") # 윈도우

# datetime 모듈
# import datetime as d
# print("오늘 날짜와 시간 출력")
# now = d.datetime.now()

# print("오늘 날짜와 시간 출력")
# print(now.year, "년")
# print(now.month, "월")
# print(now.day, "일")
# print(now.hour, "시")
# print(now.minute, "분")
# print(now.second, "초")

# from urllib import request

# target = request.urlopen("https://www.naver.com") 
# web_code = target.read()# 이거 안쓰면 못본다

# print(web_code)

# from urllib import request
# from bs4 import BeautifulSoup

# target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

# soup =BeautifulSoup(target, "html.parser")

# for location in soup.select("location"):
#     print("도시 :", location.select_one("city").string)
#     print("날씨 :", location.select_one("wf").string)
#     print("최저기온 :", location.select_one("tmn").string)
#     print("최고기온 :", location.select_one("tmx").string)

# 데코레이터
# def test(function):
#     def csos():
#         print("응용력을 키우자")
#         function()
#         print("실행이 될까?")

#     def wrapper():
#         print("허언증이 재발했습니다")
#         function()
#         print ("격리되었습니다.")
#     return  wrapper

# @test
# def oz():
#     print("머릿속의 지우개")

# oz()

