import random

def guess_game():
    print("Welcome to the guess Game!")

    pc_number = random.randint(0, 20)
    guesses = []

    for attempt in range(1, 10):
        try:
            guess = int(input(f"Attempt {attempt}:  your guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if guess < 0 or guess > 20:
            print("Your guess is out of the valid range.")
            continue

        guesses.append(guess)

        if guess == pc_number:
            print(f"afarin! hadse dorost {pc_number} in {attempt} attempts.")
            break
        else:
            if guess < pc_number:
                print("boro bala.")
            else:
                print("bia payin.")

    else:
        print("Game Over!", pc_number)

    print("Your guesses were:", guesses)

if __name__ == "__main__":
    guess_game()