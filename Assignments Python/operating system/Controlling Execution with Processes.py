import multiprocessing
import time

def infinite_task():
    while True:
        print("Running...")
        time.sleep(1)

if __name__ == "__main__":
    p = multiprocessing.Process(target=infinite_task)
    p.start()

    time.sleep(3)
    
    print("Terminating process...")
    p.terminate()

    p.join()
    print("Process terminated")