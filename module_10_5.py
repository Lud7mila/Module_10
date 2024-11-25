# многопроцессность
import time
from multiprocessing import Pool, cpu_count

file_names = [f"./file {number}.txt" for number in range(1, 5)]

def read_info(name):  # name - название файла.
    with open(name, 'r') as file:
        #print(f"Данные файла '{name}':")
        all_data = []
        while True:
            line_data = file.readline()
            if line_data == '':
                break
            all_data.append(line_data)
        #print(all_data, "\n\n")

if __name__ == '__main__':  # для процессов необходима эта проверка
    start_time = time.time()
    list(map(read_info, file_names))
    end_time = time.time()
    print(f"Линейный вызов отработал за", end_time - start_time)

    start_time = time.time()
    with Pool(processes=4) as p:
        p.map(read_info, file_names)
    end_time = time.time()
    print(f"Многопроцессный вызов отработал за", end_time - start_time)
