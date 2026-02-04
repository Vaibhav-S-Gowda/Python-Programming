# async_semaphore_requests.py
import sys
import asyncio
import aiohttp
import time
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


URLS = ["https://httpbin.org/delay/1"] * 10  # example endpoints that delay 1s

async def fetch(session, url, sem, idx):
    async with sem:
        start = time.time()
        async with session.get(url) as resp:
            txt = await resp.text()
            elapsed = time.time() - start
            print(f"{idx} status {resp.status} time {elapsed:.2f}")
            return resp.status

async def main():
    sem = asyncio.Semaphore(5)
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url, sem, i) for i, url in enumerate(URLS)]
        results = await asyncio.gather(*tasks)
    
    print("Done:", results)
    # Add this line to let the proactor loop settle
    await asyncio.sleep(0.250)

if __name__ == "__main__":
    asyncio.run(main())
