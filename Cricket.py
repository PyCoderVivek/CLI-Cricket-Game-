import random

def play_cricket():
    player_score = 0
    computer_score = 0
    overs = int(input("Enter the no. of Overs : "))
    balls_per_over = 6
    wicket=0
    c_wickets=0

    for over in range(overs):
        print(f"\nOver {over + 1}:")
        for ball in range(balls_per_over):
            input("Press Enter to bowl...")

            user_runs = random.randint(0, 6)
            computer_runs = random.randint(0, 6)

            print(f"You scored {user_runs} runs!")
            print(f"Computer scored {computer_runs} runs!")

            if user_runs==0 :
                wicket=wicket+1
            if wicket==10 :
                break
            if computer_runs==0:
                c_wickets=c_wickets+1
            if c_wickets==10:
                break

            player_score += user_runs
            computer_score += computer_runs

            print(f"Your total score:{player_score}/{wicket}")
            print(f"Computer's total score: {computer_score}/{c_wickets}")

    print("\nGame Over!")
    if player_score > computer_score:
        print("Congratulations! You won!")
    elif computer_score > player_score:
        print("Computer wins. Better luck next time!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_cricket()
