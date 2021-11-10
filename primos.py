from typing import List

def primos(num: int) -> bool:
    divisors: List[int] = [i for i in range(1, num + 1) if num % i == 0]
    return len(divisors) == 2

def run():
    primos(9)


if __name__ == '__main__':
    run()