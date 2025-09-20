import random

print("Welcome to 'Guess the Number'!")
print("Choose a difficulty level:")
print("1. Easy (1-50, 10 attempts)")
print("2. Medium (1-100, 7 attempts)")
print("3. Hard (1-200, 5 attempts)")

# Choose a level
while True:
    choice = input("Enter 1 (Easy), 2 (Medium), or 3 (Hard): ")
    if choice == '1':
        max_number = 50
        attempts_left = 10
        break
    elif choice == '2':
        max_number = 100
        attempts_left = 7
        break
    elif choice == '3':
        max_number = 200
        attempts_left = 5
        break
    else:
        print("Invalid choice. Please try again.")

computer_number = random.randint(1, 100)
score = 100
points_lost_per_attempt = int(score / attempts_left)

print(f"\nI have picked a number between 1 and {max_number}. Try to guess it!")


while attempts_left > 0:
    print(f"Attempts left: {attempts_left}.")
    print()
    player_input = input(f"Your guess: ")

    if not player_input.isdigit():
        print("Please enter a valid number.")
        continue

    player_number = int(player_input)

    if player_number == computer_number:
        print("Correct! You guess it!")
        print(f"Your final score: {score}")
        break
    elif player_number > computer_number:
        print("Too High!")
    elif player_number < computer_number:
        print("Too Low!")

    attempts_left -= 1
    score -= points_lost_per_attempt

    if attempts_left == 0:
        print(f"\nGame over! The number was: {computer_number}")
        print(f"Your final score: {score}")