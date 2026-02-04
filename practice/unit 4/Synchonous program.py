# sync_demo.py
import time

def step(name, delay):
    print(f"{name} start")
    time.sleep(delay)
    print(f"{name} end")

def main():
    start = time.time()
    step("A", 1)
    step("B", 1)
    step("C", 1)
    print("Total time:", time.time() - start)

if __name__ == "__main__":
    main()
