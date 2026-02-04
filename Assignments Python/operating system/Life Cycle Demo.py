from multiprocessing import Process
import time

def work():
    print("Process started")
    time.sleep(2)
    print("Process finished")

if __name__ == "__main__":
    p =Process(target=work)
    print("Before start: ", p.is_alive())
    p.start()
    print("After start: ", p.is_alive())
    p.join()
    print("After join: ", p.is_alive())