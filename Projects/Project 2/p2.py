
import threading
import math
import time
import asyncio

class PrimeThread(threading.Thread):
    def __init__(self, start, stepsize, result, time_limit):
        super().__init__()
        self.start = start
        self.stepsize = stepsize
        self.result = result
        self.time_limit = time_limit
        self.highest_prime = -1
        self.starttime = time.time()
    
    def run(self):
        n = self.start
        while time.time() - self.starttime < self.time_limit:
            if self.is_prime(n):
                self.highest_prime = n
            n += self.stepsize
        self.result.append(self.highest_prime)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def high_prime(time_limit, number_of_threads):
    threads = []
    results = []
    for i in range(number_of_threads):
        thread = PrimeThread(i, number_of_threads, results, time_limit)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    return max(results) if results else "failed"

def primes_in_range(start, stepsize, result, time_limit):
    highest_prime = -1
    starttime = time.time()

    number = start

    while time.time() - starttime < time_limit:
        if is_prime(number):
            highest_prime = number
        number += stepsize

    result.append(highest_prime)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

async def calculate_fibonacci_n_factorial(prime, factorial_input):
    loop = asyncio.get_event_loop()
    fib_task = loop.run_in_executor(None, fibonacci, prime)
    fact_task = loop.run_in_executor(None, factorial, factorial_input)
    fib_result, fact_result = await asyncio.gather(fib_task, fact_task)
    return fib_result, fact_result
  
def main():
    
    print("Calculating highest prime sooner than you can spell your name backwards...")
    highest_prime_result = high_prime(30, 4)
    print("Highest prime:", highest_prime_result)

    print("Calculating Fibonacci and Factorial faster than you can say 'abracadabra'...")
    fact_input = 10
    fib_input, fact_input = asyncio.run(calculate_fibonacci_n_factorial(highest_prime_result, fact_input))
    print("Fibonacci of {}: {}".format(highest_prime_result, fib_input))
    print("Factorial of {}: {}".format(fact_input, fact_input))
    print("Done!")
if __name__ == "__main__":
    main()