import time
 
def get_time(n):
    start_time = time.perf_counter()
    result = sum(range(n)) # 0 + 1 + 2 + ... + (n -1)
    end_time = time.perf_counter()
    print(f"My function took {end_time - start_time:.5f} seconds to run")
    return result
 
 
def main():
    print(get_time(10_000_000))
 
 
if __name__ == "__main__":
    main()
