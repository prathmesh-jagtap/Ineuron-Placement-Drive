"""Implement a decorator function called ‘timer’ that measures 
the execution time of a function. The ‘timer’ decorator should print 
the time taken by the decorated function to execute. Use the ‘time’ module 
in Python to calculate the execution time.

Example:

import time

@timer
def my_function():
    # Function code goes here
    time.sleep(2)

my_function()

Output:
"Execution time: 2.00123 seconds"
"""

import time


def timer(func):
    def wrap_fun(*args):
        start = time.perf_counter()
        result = func(*args)
        end = time.perf_counter()
        print(f"Execution time: {end - start} seconds")
        return result
    return wrap_fun


@timer
def my_function():
    time.sleep(2)


my_function()
