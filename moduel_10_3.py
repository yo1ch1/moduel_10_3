import threading
import random
import time

class Bank(threading.Thread):
    def __init__(self):

        super().__init__()
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            cash_up = random.randint(50, 500)
            self.balance += cash_up
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {cash_up}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            cash_out = random.randint(50, 500)
            print(f'Запрос на {cash_out}')
            if self.balance >= cash_out:
                self.balance -= cash_out
                print(f'Снятие: {cash_out}. Баланс: {self.balance}')
            else:
                print('Недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')