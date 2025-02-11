#fib.py
from functools import lru_cache
import time

@lru_cache
def fib(n: int) -> int:
    num1 = 0
    num2 = 1
    next = 1
    count = 0
    start_clock = time.time()
    while count<=n:
        end_clock = time.time()
        print("Finished in", end_clock-start_clock , "f(" ,count, "):", num1) # Add timer 
        num1 = num2
        num2 = next
        next = num1 + num2
        count += 1

if __name__ == "__main__":
    fib(100)