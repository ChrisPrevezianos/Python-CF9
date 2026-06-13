import random
 
def get_user_guess():
    while True:
        try:
            return int(input("Please enter an int: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
 
def check_guess(secret, guess):
    if guess == secret:
        print(f"Bingo! Secret number: {secret}")
        return True
    elif abs(guess - secret) <= 5:
        print("Hot")
    else:
        print("Cold")
    return False
 
def main():
    secret_number = random.randint(1, 10)
    print(f"Secret number hacked: {secret_number}")
    MAX_TRIES = 5
    tries = 0
 
    while tries < MAX_TRIES:
        guess = get_user_guess()
        if check_guess(secret_number, guess):
            break
        tries += 1
 
    if tries == MAX_TRIES:
        print("You reached the max number of tries:", MAX_TRIES)
 
 
if __name__ == "__main__":
    main()

