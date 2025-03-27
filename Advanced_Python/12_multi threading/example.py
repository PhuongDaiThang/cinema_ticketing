# import time

# def cal_square(numbers):
# 	print("calculate square number")
# 	for n in numbers:
# 		time.sleep(0.2)
# 		print ('square:', n*n)

# def cal_cube(numbers):
# 	print("calculate cube number")
# 	for n in numbers:
# 		time.sleep(0.2)
# 		print ('square:', n*n*n)

# arr = [2,3,7,9]
# t = time.time()
# cal_square(arr)
# cal_cube(arr)
# print ("done in ", time.time()- t)


#đa luồng
# from threading import Thread
# import threading
# import time


# def cal_square(numbers):
# 	print("calculate square number")
# 	for n in numbers:
# 		time.sleep(0.2)
# 		print ('square:', n*n)


# def cal_cube(numbers):
# 	print("calculate cube number \n")
# 	for n in numbers:
# 		time.sleep(0.2)
# 		print ('cube:', n*n*n)

# arr = [2,3,7,9]

# try:
# 	t = time.time()
# 	t1 = threading.Thread(target=cal_square, args=(arr,))
# 	t2 = threading.Thread(target=cal_cube, args=(arr,))
# 	t1.start()
# 	t2.start()
# 	t1.join()
# 	t2.join()
# 	print ("done in ", time.time()- t)
# except:
# 	print ("error")


# import threading

# def print_numbers():
#     for i in range(10):
#         print(i)

# def print_letters():
#     for letter in 'abcdefghij':
#         print(letter)

# def print_lettersz():
#     for letter in 'zxcvbnmasdfghjklqwertyuiop':
#         print(letter)

# # Tạo hai luồng
# thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_letters)
# thread3 = threading.Thread(target=print_lettersz)

# # Bắt đầu hai luồng
# thread1.start()
# thread2.start()
# thread3.start()

# # Đợi cho cả hai luồng hoàn thành
# thread1.join()
# thread2.join()
# thread3.join()

# print("Done!")

import threading

def print_numbers():
    for i in range(5):
        print(i)

t1 = threading.Thread(target=print_numbers)
t1.start()