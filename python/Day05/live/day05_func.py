stock = {
    "팥붕어빵" : 10,
    "슈크림붕어빵" : 8,
    "초코붕어빵" : 5
}
sales = {
    "팥붕어빵" : 0,
    "슈크림붕어빵" : 0,
    "초코붕어빵" : 0
}
price ={
    "팥붕어빵" : 1000,
    "슈크림붕어빵" : 2000,
    "초코붕어빵" : 3000
}

total_sales = 0

def order_bread():
    while True:
            bread_type = input("주문하실 붕어빵의 맛을 골라주세요 : 팥붕어빵 | 슈크림붕어빵 | 초코붕어빵\n").strip()
            if bread_type == "뒤로가기":
                break
            bread_count = int(input("주문할 개수를 입력하세요\n"))
            if bread_type == "팥붕어빵" or bread_type == "슈크림붕어빵" or bread_type == "초코붕어빵":

                if stock[bread_type] > bread_count:
                    stock[bread_type] -= bread_count
                    sales[bread_type] += bread_count
                    print(f'{bread_type} {bread_count}개 판매되었습니다')
                else:
                    result = bread_count - stock[bread_type]
                    print(f'죄송합니다... 현재 {bread_type}는 {result}개 부족합니다.')
                    print("남은 수량 :")
                    for k, v in stock.items():
                        print(f'{k} {v}개')
            else:
                print("3가지 붕어빵 중에 선택해 주세요")

def admin():
    while True:
            bread_type = input("추가할 붕어빵 종류를 입력하세요 : 팥붕어빵 | 슈크림붕어빵 | 초코붕어빵\n").strip()
            if bread_type == "뒤로가기":
                break
            bread_count = int(input("추가할 붕어빵 개수를 입력하세요\n"))
            stock[bread_type] += bread_count
            print(f'{bread_type}의 재고가 {bread_count}개 추가었습니다.')
            print("현재 재고:")
            for bread_t, bread_c in stock.items():
                        print(f'{bread_t} {bread_c}개')
            else: 
                print("다시 입력해 주세요")




def main():
    while True:
        mode = input("모드를 선택해 주세요\n 1.관리 2. 주문 3. 종료\n").strip()
        if mode == '3' or mode == '종료':
            break
        if mode == '2' or mode == '주문':
            order_bread()
        if mode == '1' or mode == '관리':
            admin()

main()
for bread_t in sales:
    sum = sales[bread_t] * price[bread_t]
    if sum:
        total_sales += sum
        print(f'{bread_t} {sales[bread_t]}개 {format(sum, ',')}원')
print(f'오늘의 매출은 총 {format(total_sales, ',')}원 입니다.')
print("시스템을 종료합니다")


