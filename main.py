import sys
import multiprocessing
import time
import math

sys.set_int_max_str_digits(10000)

def factorial(num):
    print(f"Computing Factorial of {num}")
    result=math.factorial(num)
    print(f"factorial of {num} is {result}")
    return result

if __name__=="__main__":
    numbers=[1000,2000,400]
    start_time=time.time()
    # with multiprocessing.Pool() as pool:
    #     results=pool.map(factorial,numbers)
    rnu=map(factorial,numbers)
    results=list(rnu)
    end_time=time.time()
    
    print(f"the time taked {end_time-start_time}")