######################
##### Week_13.py #####
######################


import random
import math
import hashlib
import csv


import matplotlib.pyplot as plt


def Solution1():
    labels = ['Java', 'C/C++', 'Python', 'JavaScript']
    sizes = [35, 30, 25, 10]
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
    explode = (0, 0, 0.1, 0)

    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)

    plt.axis('equal')
    plt.show()


def Solution2():
    x = [i for i in range(10)]

    plt.figure()

    for i in range(1, 5):
        y1 = sorted([random.randint(1, 20) for dummy in range(10)])
        y2 = sorted([random.randint(1, 20) for dummy in range(10)])
        plot_index = int('22' + str(i))
        plt.subplot(plot_index)
        plt.plot(x, y1, c='r')
        plt.plot(x, y2, c='b')

    plt.show()


def Solution3():
    def Prob(n):
        return 1 - math.factorial(365) / ((365 ** n) * (math.factorial(365 - n)))

    x = [i for i in range(1, 101)]
    y = [Prob(i) for i in range(1, 101)]

    plt.figure()
    plt.plot(x, y)
    plt.show()


def Solution4():
    s = '''\
    Index: 4
    Timestamp: Thu Jul 25 16:20:00 2019
    Difficulty: 3
    Nonce: {Nonce}
    PrevHash: e4d7f1b4ed2e42d15898f4b27b019da4\
    '''

    difficulty = 3
    nonce = 0

    while True:
        result = hashlib.md5(bytes(s.format(Nonce=nonce), encoding='utf8'))
        hashCode = result.hexdigest()
        for i in range(0, difficulty):
            if hashCode[i] != '0':
                break
        else:
            print(hash)
            break
        nonce += 1

    print(nonce)


#####################
##### Homeworks #####
#####################


def Homework1():
    class Stock:
        def __init__(self, name, code):
            self.name = name
            self.code = code

        def set_name(self, name):
            self.name = name

        def set_code(self, code):
            self.code = code

        def get_name(self):
            return self.name

        def get_code(self):
            return self.code

    Samsung = Stock("삼성전자", "005930")
    print(Samsung.name)
    print(Samsung.code)
    print(Samsung.get_name())
    print(Samsung.get_code())


def Homework2():
    class Account:
        account_count = 0

        def __init__(self, name, balance):
            self.deposit_count = 0
            self.deposit_log = []
            self.withdraw_log = []

            self.name = name
            self.balance = balance
            self.bank = "SC은행"

            num1 = random.randint(0, 999)
            num2 = random.randint(0, 99)
            num3 = random.randint(0, 999999)

            num1 = str(num1).zfill(3)
            num2 = str(num2).zfill(2)
            num3 = str(num3).zfill(6)
            self.account_number = num1 + '-' + num2 + '-' + num3
            Account.account_count += 1

        @classmethod
        def get_account_num(cls):
            print(cls.account_count)

        def deposit(self, amount):
            if amount >= 1:
                self.deposit_log.append(amount)
                self.balance += amount

                self.deposit_count += 1
                if self.deposit_count % 5 == 0:
                    self.balance = (self.balance * 1.01)

        def withdraw(self, amount):
            if self.balance > amount:
                self.withdraw_log.append(amount)
                self.balance -= amount

        def display_info(self):
            print("은행이름: ", self.bank)
            print("예금주: ", self.name)
            print("계좌번호: ", self.account_number)
            print("잔고: ", self.balance)

        def withdraw_history(self):
            for amount in self.withdraw_log:
                print(amount)

        def deposit_history(self):
            for amount in self.deposit_log:
                print(amount)

    k = Account("Kim", 1000)
    k.deposit(100)
    k.deposit(200)
    k.deposit(300)
    k.deposit_history()

    k.withdraw(100)
    k.withdraw(200)
    k.withdraw_history()


def Homework3():
    class Vehicle:
        def __init__(self, wheel, price):
            self.wheel = wheel
            self.price = price

        def information(self):
            print("Count of wheel : ", self.wheel)
            print("Price : ", self.price)

    class Car(Vehicle):
        def __init__(self, wheel, price):
            super().__init__(wheel, price)

    class Bicycle(Vehicle):
        def __init__(self, wheel, price, pedal):
            super().__init__(wheel, price)
            self.pedal = pedal

        def information(self):
            super().information()
            print("Pedal : ", self.pedal)


def Homework4():
    f = open("File.csv", mode="wt", encoding="cp949", newline='')
    writer = csv.writer(f)
    writer.writerow(["종목명", "종목코드", "PER"])
    writer.writerow(["삼성전자", "005930", 15.59])
    writer.writerow(["NAVER", "035420", 55.82])
    f.close()


def Homework5():
    per = ["10.31", "", "8.00"]

    for i in per:
        try:
            print(float(i))
        except:
            print(0)
        else:
            print("clean data")
        finally:
            print("변환 완료")
