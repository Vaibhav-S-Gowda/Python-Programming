from multiprocessing import Pool

logs = [
    "Error: Disk full\nInfo: OK\nError: Network down",
    "Info: Started\nError: Timeout\nError: Crash",
    "Info: Running\nInfo: Running\nError: Memory leak"
]

def count_errors(log_data):
    return log_data.count("Error")

if __name__ == "__main__":
    with Pool(processes=3) as pool:
        results = pool.map(count_errors, logs)

    print("Errors per llog file: ", results)
    print("Total Errors: ", sum(results))