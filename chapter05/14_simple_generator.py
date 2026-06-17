# yield: converts a simple function into generator
# yield: returns a generator object
 
# When a generator function is called, it returns a generator object BUT does not start execution immediately.
# When the next() function is called on the generator object, the generator function starts executing ultil it
# reached the yield statement. The value specified in the yield statement is returned to the caller, and the
# stete of the generator function is saved. The next time next() function is called, the generator resumes execution
# right after the yield statement, preserving the local variables and execution state.
 
def simple_generator():
    # print("The capital of", end=" ")
    yield "The capital of"
    # print("Greece is", end=" ")
    yield "Greece is"
    # print("Athens.")
    yield "Athens."
 
def main():
    gen = simple_generator()
    a = next(gen)
    # print(f"\na={a}\n")
    # print()
    b = next(gen)
    # print()
    c = next(gen)
 
    print("-------------------")
    import time
 
    gen = simple_generator()
    for g in gen:
        time.sleep(3)
        print(g, end=" ")
    print()
 
if __name__ == "__main__":
    main()