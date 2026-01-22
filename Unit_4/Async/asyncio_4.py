import asyncio
import time

# -------------------------------------------------
# ASYNCHRONOUS IMPLEMENTATION
# -------------------------------------------------

async def square_async(n):
    await asyncio.sleep(0.1)
    return n * n


async def compute_squares_async(start, end):
    tasks = []
    for i in range(start, end + 1):
        tasks.append(square_async(i))
    return await asyncio.gather(*tasks)


async def run_async(start, end):
    t0 = time.perf_counter()
    results = await compute_squares_async(start, end)
    t1 = time.perf_counter()

    for i, sq in enumerate(results, start):
        print("Async square of", i, "is", sq)

    return round(t1 - t0, 2)


# -------------------------------------------------
# SYNCHRONOUS IMPLEMENTATION
# -------------------------------------------------

def square_sync(n):
    time.sleep(0.1)
    return n * n


def compute_squares_sync(start, end):
    results = []
    for i in range(start, end + 1):
        results.append(square_sync(i))
    return results


def run_sync(start, end):
    t0 = time.perf_counter()
    results = compute_squares_sync(start, end)
    t1 = time.perf_counter()

    for i, sq in enumerate(results, start):
        print("Sync square of", i, "is", sq)

    return round(t1 - t0, 2)


# -------------------------------------------------
# USER INPUT
# -------------------------------------------------

start = int(input("Enter the starting value: "))
end = int(input("Enter the ending value: "))


# -------------------------------------------------
# RUN ASYNC
# -------------------------------------------------

print("\nRunning asynchronous program")
async_time = asyncio.run(run_async(start, end))
print(f"Asynchronous total time {async_time} seconds\n")


# -------------------------------------------------
# RUN SYNC
# -------------------------------------------------

print("Running synchronous program")
sync_time = run_sync(start, end)
print(f"Synchronous total time {sync_time} seconds\n")


# -------------------------------------------------
# TIME COMPARISON
# -------------------------------------------------

print("Time difference")

if sync_time > async_time:
    print(f"Asynchronous was faster by {round(sync_time - async_time, 2)} seconds")
else:
    print(f"Synchronous was faster by {round(async_time - sync_time, 2)} seconds")
