first_list = []
print(first_list)
## list() 쓰면 형변환 됨
# 사칙연산도 된다?
first_list = [23, "이건 리스트"*3, 1.2, 2/3]
print(first_list)

로또 = [3, 5, 14, 33, 41, 44]
print(로또[1:3])
print(로또[-1])
print(로또[-1::])
로또2 = [2,12,15,24,33,39]

print((로또+로또2))
print(로또.count(33))

even= list(range(2,10,2))
print(even)

print(even.index(even.len()))