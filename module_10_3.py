import threading
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.lock = threading.Lock()
        self.balance = 0

    def deposit(self):  # внесение средств на счёт
        for _ in range(100):
            increment = randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += increment
            print(f"Пополнение: {increment}. Баланс: {self.balance}.")
            sleep(0.001)

    def take(self):
        for _ in range(100):  # снятие средств со счёта, если их достаточно
            decrement = randint(50, 500)
            print(f"Запрос на {decrement}.")
            if self.balance >= decrement:
                self.balance -= decrement
                print(f"Снятие: {decrement}. Баланс: {self.balance}.")
            else:
                self.lock.acquire()
                print(f"Запрос отклонён, недостаточно средств.")
            sleep(0.001)


bk = Bank()
# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')