def memoize(func):
    cache = {}
    cache_stats = { "hits": 0, "misses": 0}
 
    def wrapper(n):
        if n in cache:
            cache_stats["hits"] += 1
            print(f"Cache hit for Fibonacci({n})")
        else:
            cache_stats["misses"] += 1
            print(f"Calculatinng Fibonacci({n})")
            cache[n] = func(n)
        return cache[n]
   
    def get_cache_stats():
        return cache_stats
    # Attach the stats function to the wrapper fo easy access
    wrapper.get_cache_stats = get_cache_stats
    return wrapper

@memoize
def fibonacci(n):
    if n <= 1: return n
    return fibonacci(n-1) + fibonacci(n-2)
 
def main():
    results = []

    for i in range(25):
        print(f"\n ----fibonacci({i})----")
        results.append(fibonacci(i))
        print("\n-> Fibonacci sequence:", results)

        # Print cache hits and misses
        cache_stats = fibonacci.get_cache_stats()
        print(f"Cache statistics: Hits - {cache_stats['hits']}, Misses - {cache_stats['misses']}")
 
if __name__ == "__main__":
    main()