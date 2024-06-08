import time
from concurrent.futures import ThreadPoolExecutor

import requests


def get_status_code(url: str) -> int:
    response = requests.get(url)

    return response.status_code


start = time.time()
# with ThreadPoolExecutor() as pool:
#     urls = ['http://www.example.com' for _ in range(100)]
#     results = pool.map(get_status_code, urls)
#     for result in results:
#         print(result)
for _ in range(100):
    print(get_status_code('https://www.example.com'))

end = time.time()
print(f'finished requests in {end - start:.4f} second(s)')
