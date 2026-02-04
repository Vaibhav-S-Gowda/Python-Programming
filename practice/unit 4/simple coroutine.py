# async_basic_coroutine.py
import asyncio
import time

async def coro(name, delay):
    print(f"{name} start at {time.time():.2f}")
    await asyncio.sleep(delay)
    print(f"{name} end at {time.time():.2f}")
    return name

async def main():
    t0 = time.time()
    result = await coro("A", 2)
    print("Result:", result, "Total time:", time.time() - t0)

if __name__ == "__main__":
    asyncio.run(main())
