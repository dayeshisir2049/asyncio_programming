import time
import requests

def read_exmaple():
    resp = requests.get('https://www.example.com')
    print(resp.status_code)


if __name__ == '__main__':
    start = time.time()

    read_exmaple()
    read_exmaple()

    end = time.time()

    print(f'costs: {end  - start:.2f}')

