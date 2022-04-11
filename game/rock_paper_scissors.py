import  random

#import game as game

user_wins = 0
computer_wins = 0
options = ["rock" , "paper" , "scissors"]
options[0]
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit : ").lower()
    if user_input == "q":
        break
    if user_input not in options:
       continue
    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print("Computer picked" , computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
            print("You won!")
            user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    elif user_input == "rock" and computer_pick == "rock":
            print("Draw Start again!")
            user_wins += 0

    elif  user_input == "scissors" and computer_pick == "scissors":
        print("Draw Start again!")
        user_wins += 0

    elif user_input == "paper" and computer_pick == "paper":
        print("Draw Start again!")
        user_wins += 0

    else:
        print("You Lost !")
        computer_wins += 1



#    else:
 #       print("")
  #      computer_wins += 0
   #     break
print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")
