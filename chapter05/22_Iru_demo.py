from functools import lru_cache
 
@lru_cache(maxsize=None)
def fibonacci_cached(n):
    if n <= 1: return n
    return fibonacci_cached(n-1) + fibonacci_cached(n-2)
 
def fibonacci_with_logging(n):
    if fibonacci_cached.cache_info().hits > 0:
        print(f"Cache hit for fibonacci({n})")
    else:
        print(f"Caclulating fibonacci({n})")
    return fibonacci_cached(n)
 
def main():
    print([fibonacci_with_logging(n) for n in range(10)])
 
if __name__ == "__main__":
    main()
