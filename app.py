# write 'hello world' to the console
print('hello world')

# Import necessary modules
import random

#Define the game logic. You can create a function that takes the player's choice and the computer's choice and determines the winner based on the rules mentioned.
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

# Create the main game loop. This loop will continue until the player chooses to stop playing.
def main():
    player_score = 0
    total_rounds = 0

    while True:
        print("Enter your choice: rock, paper, or scissors (type 'quit' to exit)")
        player_choice = input().lower()

        if player_choice == 'quit':
            break
        elif player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please enter rock, paper, or scissors.")
            continue

        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print(f"Computer's choice: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(result)

        if result == "You win!":
            player_score += 1

        total_rounds += 1

    print(f"Game over! Your score: {player_score} wins out of {total_rounds} rounds.")

if __name__ == "__main__":
    main()

