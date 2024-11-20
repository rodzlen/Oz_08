##Live Session 
### 프로젝트 : 간단한 ATM 관리 시스템
balance = 1000 # 현재 잔액
receipts = []

while True:
    num=int(input("사용하실 기능을 선택해 주세요\n1. 입금, 2. 출금, 3. 영수증 보기, 4. 사용 종료"))
    if num == 1:
        #입금기능
        deposit_amount=int(input('입금할 금액을 입력해 주세요 : ')) # input은 str형태로 받음 int로 형변환
        balance += deposit_amount # 잔액에 입금금액 추가
        receipts.append(('입금', deposit_amount, balance))

        print(f'입금 금액은{deposit_amount}원, 현재 잔액은{balance}원입니다.')
    elif num == 2:
        # 출금 기능
        withdraw_amount=int(input('출금할 금액을 입력해 주세요 : ')) # input은 str형태로 받음 int로 형변환
        withdraw_amount=min(balance, withdraw_amount)
        balance -= withdraw_amount # 잔액에 출금 금액 추가
        receipts.append(('출금', withdraw_amount, balance))

        print(f'출금 금액은{withdraw_amount}원, 현재 잔액은{balance}원입니다.')
    elif num == 3:
        #영수증 내역 출력
        print(receipts)
    elif num == 4:
        #종료기능
        print("사용을 종료합니다.")
        break




