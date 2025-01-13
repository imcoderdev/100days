import time

current_time = time.time()
print(current_time)  # seconds since Jan 1st, 1970


# Write your code below 👇

def speed_calc_decorator(func):
    def wrapped_function():
        start_time=time.time()
        func()
        end_time=time.time()
        print(f"{func.__name__} run time: {end_time - start_time:.4f} seconds")
        print(end_time-start_time)
    return wrapped_function

@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


fast_function()
slow_function()