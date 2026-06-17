import time
 
def time_decorator(func):
    def inner_function(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{func.__name__} took {end_time - start_time:.5f} seconds to run.")
        return result
    return inner_function
 
def sum_function(n):
    return sum(range(n + 1))
 
sum_function = time_decorator(sum_function)
print(sum_function(1_000_000))
 
# print(sum_function(1_000_000))
 
@time_decorator
def my_add(num):
    return sum(range(num + 1))
