import threading
import multiprocessing
import time

total_Load = 1000  
lock = threading.Lock() 

def pasaload_thread(mobile_number, trans_load):
    global total_Load
    with lock:
        if total_Load >= trans_load:
            total_Load -= trans_load
            print(f"Threads: You successfully transferred {trans_load} load to {mobile_number}.")
        else:
            print("Insufficient balance.")


def pasaload_process(mobile_number, trans_load):
    global total_Load
    with lock:
        if total_Load >= trans_load:
            total_Load -= trans_load
            print(f"\nMultiprocessing: You successfully transferred {trans_load} load to {mobile_number}.")
        else:
            print("Insufficient balance.")

if __name__ == '__main__':
    mobile_number = input("Enter the mobile number: ")
    trans_load = int(input("Enter the amount of load you want to transfer: "))

    t1 = threading.Thread(target=pasaload_thread, args=(mobile_number, trans_load))
    t1.start()

    p1 = multiprocessing.Process(target=pasaload_process, args=(mobile_number, trans_load))
    p1.start()

    t1.join()
    p1.join()

    print(f"Your remaining load balance is {total_Load}")

