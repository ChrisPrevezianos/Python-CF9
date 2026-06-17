def memoize(func):
    cache = {}
 
    def wrapper(n):
        if n in cache:
            print(f"Cache hit for Fibonacci({n})")
        else:
            print(f"Calculating Fibonacci({n})")
            cache[n] = func(n)
        return cache[n]
   
    return wrapper
 
@memoize
def fibonacci(n):
    if n <= 1: return n
    return fibonacci(n-1) + fibonacci(n-2)
 
def main():
    print([fibonacci(n) for n in range(10)])
 
if __name__ == "__main__":
    main()
