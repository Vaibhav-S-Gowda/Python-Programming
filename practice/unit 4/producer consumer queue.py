# producer_consumer_queue.py
from multiprocessing import Process, Queue
import time

def producer(q, data_chunks):
    for chunk in data_chunks:
        print("Producer enqueue:", chunk)
        q.put(chunk)
        time.sleep(0.2)
    # signal consumers to stop
    for _ in range(2):
        q.put(None)

def consumer(q, cid):
    while True:
        item = q.get()
        if item is None:
            print(f"Consumer {cid} exiting")
            break
        print(f"Consumer {cid} processing {item}")
        time.sleep(0.5)

if __name__ == "__main__":
    q = Queue()
    data = [f"chunk-{i}" for i in range(6)]
    p = Process(target=producer, args=(q, data))
    c1 = Process(target=consumer, args=(q, 1))
    c2 = Process(target=consumer, args=(q, 2))

    p.start(); c1.start(); c2.start()
    p.join(); c1.join(); c2.join()
    print("All done")
