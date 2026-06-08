# def say_hello(name = "User"):
#     print("Hello {name}!")

def say_hello(name = "User"):
    """
    Prints a greeting message.

    Args:
        name: The name to greet. Defaults to 'User'
    """
    print(f"Hello {name}!")
    
def main():
    say_hello("Alice")
    say_hello()

    print(say_hello.__doc__)
    print("------------------")
    help(say_hello)

# main()

if __name__ == "__main__":
    main()