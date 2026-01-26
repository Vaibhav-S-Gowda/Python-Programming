import asyncio
import aiohttp
import time

async def fetch_url(session, url):
    """Fetches a URL and returns the status code."""
    print(f"Requesting: {url}")
    try:
        async with session.get(url, timeout=10) as response:
            status = response.status
            # We use await here because reading the body is an I/O operation
            text = await response.text() 
            print(f"Finished: {url} with status {status}")
            return f"{url}: {status}"
    except Exception as e:
        return f"{url}: Failed due to {e}"

async def main():
    urls = [
        "https://www.google.com",
        "https://www.python.org",
        "https://www.github.com",
        "https://www.wikipedia.org",
        "https://www.reddit.com"
    ]

    start_time = time.perf_counter()

    # ClientSession is created once and shared across requests for efficiency
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(fetch_url(session, url))
        
        # Run all requests concurrently
        results = await asyncio.gather(*tasks)

    end_time = time.perf_counter()
    
    print("\n--- Summary ---")
    for res in results:
        print(res)
    print(f"\nTotal time for {len(urls)} requests: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())