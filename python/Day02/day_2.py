'''
식별자 > 변수

식별자는 프로그래밍 언어에서 변수, 함수 , 클래스, 모듈 등의 이름을 지정하는 모든 명칭을 뜻함

변수명은 변수의 이름을 뜻한다. (값을 저장할 메모리 공간을 참조하기위해 사용되는 이름) 

변수는 데이터를 저장하는 컨테이너이고 변수명은 컨테이너를 가르키는 이름

자료형을 명시하지 않기 때문에 실행할 때마다 자료형을 구분하는 작업을 거쳐서 정적 언어보다 상대적으로 느림
'''
# # print("{}{} {}".format(8, "기","백엔드")) # 8 기 
# num = 8
# str_a = "기"
# str_b = "백엔드"

# print(f'{num}{str_a} {str_b}')

# # format() 사용 예시
# data = [1,2,3,4]
# print("{}{}{}".format(*data)) # * 와일드카드를 사용하면 전부 대입 - 초과하거나 오류나진 않음 

num1 = "2"
num2 = 3
print(int(num1)+num2) # 문자열을 int로 변환 가능하지만

print(21+29)

############# 중요 !! //, % 는 정수만 반환한다.

position = "백엔드"
get_in = "3명 타세요"

print(position * 3)

print(0.1+0.2)