import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()

with open('RomeoAndJuliet.txt', 'wb') as playFile:
    for chunk in res.iter_content(100000):
        playFile.write(chunk)
print("File downloaded successfully!")

# Technical Notes:
# Network Complexity: Depends on file size and network latency; download time ≈ O(n),
# where n = file size.

# Time Complexity (Processing): O(n)
# Each byte is streamed from the network and written once to disk.

# Space Complexity: O(1)
# Uses chunked streaming (iter_content), so memory usage stays constant
# and only stores the current chunk in memory.

# Efficiency Considerations:
# - Chunk-based downloading avoids loading the entire file into RAM.
# - raise_for_status() enables fail-fast HTTP error handling.
# - Binary mode ('wb') preserves raw file integrity and avoids encoding overhead.

# Reliability Characteristics:
# - Safe for large file downloads.
# - Can be extended with retry logic and resume support.
# - Suitable for automation, ETL pipelines, and batch data ingestion.

# Possible Optimizations:
# - Add request timeout.
# - Implement retry mechanism for transient failures.
# - Tune chunk size based on disk and network performance.

# Typical Use Cases:
# - Automated dataset downloads
# - Log/data archival
# - CI/CD artifact fetching
# - Pre-processing stage in data pipelines