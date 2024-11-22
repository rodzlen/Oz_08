# 클래스 
'''
겍체 
    
'''
# # 클래스 선언
# class class_name:
#     def method(self):
#         return self
    
# class Person:
#     def hello(self):
#         print("수강생 여러분")
# 호출 = Person() # 인스턴스 변수로  클래스 객체를 초기화 
# 호출.hello()

# '''
# 클래스에 속성을 만들 수 있다. 
# '''
# class 클래스이름:
#     ## 인스턴스로 초기화 시키기만 해도 실행된다.
#     def __init__(self):
#         self.hello=print("안녕")

    
# 호출2 = 클래스이름()


# ## 에외처리 구문

# y = [10, 20, 30]
# try:
#     index, x = map(int, input("나눌 숫자를 입력하세요").split(','))
#     print(y[index]/x)
#     raise

# except ZeroDivisionError:
#     print("숫자를 0으로 나눌 수 없습니다")
# except IndexError:
#     print("잘못된 인덱스입니다.")
# else:
#     print("정상적으로 작동되었습니다.")
# finally:
#     print("실행을 종료합니다.")


fish_bread = {"팥붕어빵":{"재고":0,
                        "가격":0,
                        "판매량":0
                        },
                    "슈크림붕어빵":{"재고":0,
                        "가격":0,
                        "판매량":0
                        },
                    "망고붕어빵":{"재고":0,
                        "가격":0,
                        "판매량":0
                    }}
for i in fish_bread:
            print(f'{i}의 재고 :{fish_bread[i]["재고"]}')
