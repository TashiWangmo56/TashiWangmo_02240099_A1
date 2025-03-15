import random

def guess_number_game():
    print("Welcome tp the Guess Number Game!")
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    number_to_guess = random.randint(start, end)
    attempts = 0

    while True:
         guess = int(input(f"Guess a number between {start} and {end}: "))
         attempts += 1
         if guess < number_to_guess:
             print("Too low! Try again.")
         elif guess > number_to_guess:
             print("Too high! Try again.")
         else:
             print(f"Congratulations! You guessed the number in {attempts} attempts.")
             break
             
if __name__ == "__main__":
    guess_number_game()

def rock_paper_scissors_game():
    print("Welcome to Rock Paper Scissors Game!")
    choices = ["rock", "paper", "scissors"]

    while True:
        user_choice = input("Enter your choice (rock, paper, scissors) or 'exit' to quit: ").lower()
        if user_choice == 'exit':
            print("Thanks for playing!")
            break
        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(choices)
        print(f"computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")

if __name__ == "__main__":
    rock_paper_scissors_game()
      