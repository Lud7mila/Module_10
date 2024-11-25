# очереди
from queue import Queue
from time import sleep
from random import randint
import threading


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self, name):
        super(Guest, self).__init__()
        self.name = name

    def run(self):
        delay = randint(3, 10)
        #print(f"{self.name} будет есть {delay} сек.")
        sleep(delay)


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            if any((empty_table := table).guest == None for table in self.tables): # если есть свободный столик,
                empty_table.guest = guest  # то сажаем за него гостя
                print(f"{guest.name} сел(-а) за стол номер {empty_table.number}")
                guest.start()  # запускаем поток посаженного гостя
            else:  # иначе помещаем гостя в очередь
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def __get_released_table(self):  # возвращает занятый гостем столик, который нужно освободить
        if any((busy_table := table).guest != None and not busy_table.guest.is_alive() for table in self.tables):
            return busy_table
        else:
            return None

    def __all_tables_free(self):  # проверяет все ли столики свободны
        if any(table.guest != None for table in self.tables):
            return False
        else:
            return True

    def discuss_guests(self):
        while True:
            b_empty_queue = self.queue.empty()
            busy_table = self.__get_released_table()

            # если гость покушал и ушёл, то помечаем, что стол свободен
            if busy_table:
                print(f"{busy_table.guest.name} покушал(-а) и ушёл(ушла)")
                print(f"Стол номер {busy_table.number} свободен")
                busy_table.guest = None

                if not b_empty_queue:  # сажаем гостя из очереди за освободившийся стол
                    busy_table.guest = self.queue.get()
                    print(f"{busy_table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {busy_table.number}")
                    busy_table.guest.start()

            if b_empty_queue and self.__all_tables_free():
                break


# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()