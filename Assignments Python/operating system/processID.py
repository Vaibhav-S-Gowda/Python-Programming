import os, threading
from multiprocessing import Process

def task():
    print("Task running")
    print("PID: ", os.getpid())

if __name__ == "__main__":
    print("Main Program PID: ", os.getpid())

    t = threading.Thread(target=task)
    t.start()
    t.join()

    p = Process(target=task)
    p.start()
    p.join()
