# ##start end mul
# result = []
# def cal(start, end, mul):
#     for i in range(start, end, mul):
#         result.append(i)
#     return print(result)
# cal(1,10,3)

# 팩토리얼 구하기


def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)
    

print(fac(4))

## 피보나치 
count = 0
memo ={
    1:1,
    2:1
    }

def fi(n):
    print(f"피보나치 수열{n} 구합니다.")
    global count
    count += 1
    if n in memo:
        return memo[n]
    output = fi(n-1)+ fi(n-2)
    memo[n] = output
    return output
n = int(input("피보나치 수열을 구할 숫자를 입력"))
fi(n)
print(f'피보나치 수열{n}을 구하기 위해 {count}번 계산되었습니다')
print(memo)