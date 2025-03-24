import threading
import time

def task():
    # Tính toán đơn giản: đếm số lần lặp
    count = 0
    for _ in range(100000000):
        count += 1

# Sử dụng multithreading với GIL
def multithreading_test():
    start_time = time.time()
    threads = []
    for _ in range(10):  # Tạo 10 luồng
        thread = threading.Thread(target=task)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    end_time = time.time()
    print("Multithreading with GIL time:", end_time - start_time)

# Chỉ sử dụng một luồng
def single_thread_test():
    start_time = time.time()
    for _ in range(10):  # Thực hiện task 10 lần liên tiếp với một luồng
        task()
    end_time = time.time()
    print("Single thread time:", end_time - start_time)

multithreading_test()
single_thread_test()
