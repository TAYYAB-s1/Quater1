import random

def high_low_game():
    """Plays the High-Low game."""

    score = 0
    round_num = 1
    print("Welcome to the High-Low Game!\n--------------------------------")
    print("there will be 3 Rounds\n lets start")
    while True:
        
        print(f"Round {round_num}")

        your_number = int(input("Your number is: "))
       
     
        
        computer_number = random.randint(1, 100)

        while True:
            guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
            if guess in ["higher", "lower"]:
                break
            else:
                print("Invalid input. Please enter 'higher' or 'lower'.")

        if guess == "higher" and your_number > computer_number:
            print("You were right! The computer's number was", computer_number)
            score += 1
        elif guess == "lower" and your_number < computer_number:
            print("You were right! The computer's number was", computer_number)
            score += 1
        else:
            print("Aww, that's incorrect. The computer's number was", computer_number)
            score -=1

        print("Your score is now", score)

        round_num += 1

        if round_num > 3:
            break

    print("\nThanks for playing!")
    print("your score of 3 rounds is :3/",score)

    if score == 3:
        print("Congratulations! You have a perfect score!")
    elif score >= 2:
        print("Good job, you played really well!")
    elif score == 1:
        print("Not bad,but you can do better!")
    else:
        print("You need more practice!")
 
if __name__ :"main"
high_low_game()