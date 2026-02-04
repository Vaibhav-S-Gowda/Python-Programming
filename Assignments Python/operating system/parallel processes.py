from multiprocessing import Process
import time

def task(n):
    print(f"Task {n} started")
    time.sleep(2)
    print(f"Task {n} finished")

processes = []

start_time = time.time()

if __name__ == '__main__':
    for i in range(4):
        p = Process(target=task, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end_time = time.time()

    print("Total Time: ", end_time - start_time)