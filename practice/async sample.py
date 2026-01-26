import asyncio
import time

# An 'async' function is called a coroutine
async def fetch_data(source_id, delay):
    print(f"-> Task {source_id}: Fetching data (will take {delay}s)...")
    
    # Non-blocking sleep: allows other tasks to run while waiting
    await asyncio.sleep(delay) 
    
    print(f"<- Task {source_id}: Done!")
    return {"id": source_id, "data": "Success"}

async def main():
    start_time = time.perf_counter()

    print("Starting concurrent tasks...")

    # Create a list of tasks to run concurrently
    tasks = [
        fetch_data(1, 3),
        fetch_data(2, 1),
        fetch_data(3, 2)
    ]

    # gather() runs them all at once and waits for the result
    results = await asyncio.gather(*tasks)

    end_time = time.perf_counter()
    
    print("-" * 30)
    print(f"Results: {results}")
    print(f"Total time elapsed: {end_time - start_time:.2f} seconds")

# Run the entry point of the async program
if __name__ == "__main__":
    asyncio.run(main())