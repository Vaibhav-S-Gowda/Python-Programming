# process_lifecycle.py
import multiprocessing
import time
import os

def worker(sec):
    print(f"Worker {os.getpid()} started, sleeping {sec}s")
    time.sleep(sec)
    print(f"Worker {os.getpid()} done")

if __name__ == "__main__":
    p = multiprocessing.Process(target=worker, args=(5,))
    print("Before start is_alive:", p.is_alive())
    p.start()
    print("After start is_alive:", p.is_alive())
    time.sleep(2)
    if p.is_alive():
        print("Terminating process now...")
        p.terminate()
    p.join()
    print("After join is_alive:", p.is_alive(), "exitcode:", p.exitcode)
