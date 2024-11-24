# создание класса, наследника класса Thread
import threading
from time import sleep

class Knight(threading.Thread):
    def __init__(self, name, power):
        super(Knight, self).__init__()
        self.name = name  # имя рыцаря - str
        self.power = power  # сила рыцаря - int
        self.enemy = 100  # у каждого рыцаря 100 врагов

    def run(self):
        print(f'{self.name}, на нас напали!')
        days_counter = 0
        while self.enemy:
            sleep(1)
            self.enemy -= self.power
            days_counter += 1
            print(f"{self.name} сражается {days_counter} день, осталось {self.enemy} воинов.")
        print(f"{self.name} одержал победу спустя {days_counter} дней(дня)!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()


