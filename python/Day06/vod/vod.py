# # ##start end mul
# # result = []
# # def cal(start, end, mul):
# #     for i in range(start, end, mul):
# #         result.append(i)
# #     return print(result)
# # cal(1,10,3)

# # 팩토리얼 구하기


# def fac(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fac(n-1)
    

# print(fac(4))

# ## 피보나치 
# count = 0
# memo ={
#     1:1,
#     2:1
#     }

# def fi(n):
#     print(f"피보나치 수열{n} 구합니다.")
#     global count
#     count += 1
#     if n in memo:
#         return memo[n]
#     output = fi(n-1)+ fi(n-2)
#     memo[n] = output
#     return output
# n = int(input("피보나치 수열을 구할 숫자를 입력"))
# fi(n)
# print(f'피보나치 수열{n}을 구하기 위해 {count}번 계산되었습니다')
# print(memo)


# 제너레이터 

def test():
    print("ㅈㅔ너레이터 함수")
    yield 1
    print("이것도 두번쨰 절에 포함일까?")
    print("두 번째 출력")
    yield 2

output = test()
print("세번째 출력")

x = next(output)
print("네 번째 출력")
print(x)
y= next(output)
print(y)
print("e다섯번쨰")
z = next(output)

my_dog : str = "hunt"
my_dog : int = 7

dogs : list[str] = ["닥스훈트", "시바견", "웰시코기"]
dogs : dict[str, int] = {
    "닥스훈트"  : 21
}

def hunt(name: str) -> str:
    return name[0]
def hunt_info(name: str, age : int= 7)-> str:
    return name + str(age)
def hunt_happy(name:str) -> None:
    print("간식줄게"+name)