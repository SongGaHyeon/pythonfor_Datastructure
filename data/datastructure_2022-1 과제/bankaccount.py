class BankAccount:
    def __init__(self, acc_name=None, acc_number=None, balance=0):
        #초기화(?) 같은 작업, self는 객체를 가리킨다. acc_name(계좌이름),acc_number(계좌번호), balance(계좌 내 금액)=0으로
        # 설정해주는 작업
        self.account_name=acc_name  #argument로 받은 데이터를 넣어준다
        self.account_number=acc_number
        self.balance=balance

    def show_balance(self): #안에 있는 금액을 보여주는 함수로 , self로 객체를 받고 self.balance로 그 객체의 balance를 출력해준다
        print(self.balance)

    def show_account_info(self):
        # 계좌의 정보를 보여주는 함수. self (객체)의 account_name, account_number, balance 를 출력해준다
        print(self.account_number, self.account_name, self.balance)

    def deposit(self, amount):
        # 입금. 객체와 함께 amount를 argument로 받아 지금의 금액 (balance)에 amount( 입금할 금액 ) 넣어준다
        self.balance+=amount

    def withdraw(self, amount):
        # 출금. 객체와 함께 amount를 argument로 받아 지금의 금액(balance)에서 출금 금액(amount) 를 빼준다.
        self.balance-=amount

acc= BankAccount("Mr.Kim", 10476, 30000)
acc.show_balance()
acc.deposit(20000)
acc.show_balance()
acc.withdraw(10000)
acc.show_balance()