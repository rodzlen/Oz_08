# first_list = []
# print(first_list)
# ## list() 쓰면 형변환 됨
# # 사칙연산도 된다?
# first_list = [23, "이건 리스트"*3, 1.2, 2/3]
# print(first_list)

# 로또 = [3, 5, 14, 33, 41, 44]
# print(로또[1:3])
# print(로또[-1])
# print(로또[::-1])
# 로또2 = [2,12,15,24,33,39]

# print((로또+로또2))
# print(33 in 로또)

# even= list(range(2,10,2))
# print(even)
# even *= 2
# print(even)
# print(even[len(even)-1])

# # list 값 넣기
# food = ["숙주", "분모자", ""]
# food.append("라면")
# print(food) 
# food.insert(0,"0번째 목이버섯")
# print(food)

# 튜플 = 1,
# print(type(튜플))

# asd = {"s": 1, "a":2}
# # print(asd[1]) 불가

# zxc = list(asd.items())
# print(zxc[1][1])

# fish = {
#     '팥' : {
#         'price' : 2000,
#         'quantity' : 0
#     },
#     '슈크림' : {
#         'price' : 2500,
#         'quantity' : 0
#     },
#     '잡채' : {
#         'price' : 3000,
#         'quantity' : 0
#     }
# }
# fish[0][1] = int(input('구매할 팥붕 수량을 입력하세요'))
# fish[1][1] = int(input('구매할 슈붕 수량을 입력하세요'))
# fish[2][1] = int(input('구매할 잡붕 수량을 입력하세요'))
# quantity = fish[0][1]+fish[0][1]+fish[0][2]
# total_pay = fish[0][0]*fish[0][1] +fish[1][0]*fish[1][1]+fish[2][0]*fish[2][1]
# print(f'{fish[0][0]} {fish[0][1]}개\n{fish[1][0]} {fish[0][1]}개\n{fish[2][1]} {fish[2][1]}개\n총 {quantity}개 결제 금액은 {total_pay}원입니다.')

채소 = {'당근', '감자'}
print(type(채소),채소)

채소.add('거짓말')
print(채소)
채소.update('채소는 아니고', '니얼굴')
print(채소)

#채소.remove("근") # 데이터에 존재하지 않으면 오류 일으킴
채소.discard("소")
채소.discard("소")
print(채소.pop())

채소2 = ['당근', '감자', '니']
print(채소.union(채소2))
print(채소.intersection(채소2))
print(채소.difference(채소2))
print(set.difference(채소,채소2))