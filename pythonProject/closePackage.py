# 使用atm小案例

def account_create(initial_amount=0):

    def atm(num,deposit=True):
        nonlocal initial_amount
        if deposit:
            initial_amount+=num
            print(f"存款：+{num}，账户余额:{initial_amount}")
        else:
            initial_amount-=num
            print(f"取款：-{num}，账户余额:{initial_amount}")
    return atm

atm=account_create(24)
atm(100)
atm(200)
atm(250,deposit=False)