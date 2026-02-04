import os, multiprocessing as mp

def child():
    print("Child Process PID: ", os.getpid())

if __name__ == "__main__":
    print("Parent PID: ", os.getpid())

    p = mp.Process(target=child)
    p.start()
    p.join()