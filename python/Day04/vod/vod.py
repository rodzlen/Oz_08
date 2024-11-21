## VOD 실습 파일

## if문 문법
# 개수 = int(input("붕어빵 몇개 사실래요?"))

# if 개수 > 3:
#     print("개당 1800원입니다.") # 겁나 비쌈
# else: 
#     print("네 알겠습니다")

# if문 흐름
# 코드는 위에서 아래 순서대로 
# 예제 : 단어 a의 가운데 글자를 반환하는 코드
# 조건 : 단어의 길이가 짝수라면 가운데 두 글자를 출력하면 됩니다.
# 입력값 1 : "abced"
# dlqfurrkqt2 : "qwer"

# x = input()
# output = int(len(x)/2)

# if len(x) % 2 == 1:
#     print(x[(output)])
# else:
#     print(x[output-1:output+1])

# 절대값 정수가 담긴 정수 변수와 그 정수의 부호를 차례로 담은 부호 변수 

# 정수 = [10,5,8]
# 부호 = [True, False, True]

# 합 = 0

# for k in range(len(정수)): # range(0,len(정수),1)과 같음
#     if 부호[k] == False:
#         합 += 정수[k] * -1
#     else:
#         합 += 정수[k]
# print(합)
# print(len(정수))




# boong = {
#     "팥붕": { 
#         "가격" : 2000,
#         "수량":0},
#     "슈붕":{
#         "가격" : 2500,
#         "수량" : 0},
#     "잡붕":{
#         "가격": 3000,
#         "수량": 0}
# }

# # 방문이력 확인
# history=False

# while True :
#     sum =0 # 총 개수
#     total = 0 # 총 가격
#     ment=""# 결제 안내 멘트
    
#     # 방문이력에 따른 멘트
#     if history == True :
#         print("또 오셨네요! 붕어빵 인터내셔널입니다!")
#     else:    
#         history = True
#         print("환영합니다 고객님 붕어빵 인터내셔널입니다!")

#     # 제품별 구매 수량 입력
#     for i in boong:
#         count = int(input(f"구매할 {i}의 개수를 입력하세요"))
#         boong[i]["수량"] += count
#         sum += count
#         total += count * boong[i]["가격"]
#         ment += f"{i}{count}개, "

#     # 구매수량 선택 후 결제금액 안내
#     print(f"{ment}총 {sum}개 {total}원입니다.")

#     # 재구매 의사 묻기
#     again = input("구매를 계속 하시겠습니까? 1. 네, 2. 아니오")
#     if again == "2":
#         print("감사합니다. 또 오세요!")
#         break

# 오피스텔 = [[201,202],[301,302],[401,402]]
# for i in range(len(오피스텔)):
#     for j in range(2):
#         print(오피스텔[i][j])
#     print('-----')

# ohlc = [["open", "high", "low", "close"], [100, 110, 70, 100], [200, 210, 180, 190], [300, 310, 300, 310]]

# for i in range(1,4):
#     if ohlc[i][3] > 100:
#         print(ohlc[i])    

x = 17
a = list(map(int,str(x)))
result = x % sum(a) == 0
print(f'{x} {result}')