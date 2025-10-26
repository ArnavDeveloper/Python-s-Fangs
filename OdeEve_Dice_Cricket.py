#Odd eve is a classic game of us students. Its fun and interesting and does not require any material just hands. Thats why its a cult classic among school students. Its going to be a long one :). Its a game based on luck.
import math
import random

# Initial setup
Toss = input("Odd or even? :")
Score = 0
CompScore = 0

while Toss.lower() not in ["odd", "even"]:
    print("Invalid Choice")
    Toss = input("Odd or even? :")

Moves = (1, 2, 3, 4, 5, 6)

if Toss.lower() == "odd":
    Choice = 1
else:
    Choice = 2

Move = int(input(f"Make your move from these choices {Moves} : "))

RandomToss = random.randint(1, 6)
print(RandomToss)

if (RandomToss + Move) % 2 == 0:
    print(f"{RandomToss} + {Move} = {RandomToss + Move}")
    Done = 2
    print("Its Even")
else:
    print(f"{RandomToss} + {Move} = {RandomToss + Move}")
    Done = 1
    print("Its Odd")

Options = ["Batting", "Balling"]

# Outer loop to continue the match until a winner is determined
game_over = False

if Choice == Done:  # You won the toss
    Choice2 = input("Ok what will you choose, Batting or Balling : ")

    while not game_over:
        if Choice2.lower() == "batting":
            # Your batting
            Number = int(input(f"Make your move from these choices {Moves} : "))
            while True:
                CompMove = random.randint(1, 6)
                print(f"My move : {CompMove}")
                if Number == CompMove:
                    print(Score)
                    print("Hah! you lose my turn.")
                    break
                else:
                    Score += Number
                    print(f"Your current score : {Score}")
                    Number = int(input(f"Next Move {Moves} : "))

            print("Get Ready to bowl")
            Number = int(input(f"Make your move from these choices {Moves} : "))

            while True:
                CompMove = random.randint(1, 6)
                print(f"My move : {CompMove}")
                if Number == CompMove:
                    print(CompScore)
                    print(f"My score : {CompScore}   Your Score : {Score}")
                    print("Oops I lost.")
                    game_over = True
                    break
                else:
                    CompScore += CompMove
                    print(f"My current score : {CompScore}")
                    Number = int(input(f"Next Move {Moves} : "))
                    if CompScore > Score:
                        print(f"My score : {CompScore}   Your Score : {Score}")
                        print("Ha! I win")
                        game_over = True
                        break

        elif Choice2.lower() == "balling":
            # Your bowling
            Number = int(input(f"Make your move from these choices to bowl {Moves} : "))

            while True:
                CompMove = random.randint(1, 6)
                print(f"My move : {CompMove}")
                if Number == CompMove:
                    print(CompScore)
                    print(f"My score : {CompScore}   Your Score : {Score}")
                    print("Oops I lost.")
                    break
                else:
                    CompScore += CompMove
                    print(f"My current score : {CompScore}")
                    Number = int(input(f"Next Move {Moves} : "))

            while True:
                CompMove = random.randint(1, 6)
                print(f"My move : {CompMove}")
                if Number == CompMove:
                    print(Score)
                    print("Hah! you lose")
                    break
                else:
                    Score += Number
                    print(f"Your current score : {Score}")
                    Number = int(input(f"Next Move {Moves} : "))
                    if Score > CompScore:
                        print(f"My score : {CompScore}   Your Score : {Score}")
                        print("Alas! You win")
                        game_over = True
                        break

else:  # You lost the toss, computer chooses
    CompChoice = random.choice(Options)
    print(f"Ok i choose {CompChoice}")

    while not game_over:
        if CompChoice.lower() == "bowling":
            # Computer chooses to bowl, you bat
            Number = int(input(f"Make your move from these choices to bat {Moves} : "))

            while True:
                CompMove = random.randint(1, 6)
                print(f"My move : {CompMove}")
                
                if Number == CompMove:
                    print(Score)
                    print("Hah! you lose my turn.")
                    break
                else:
                    Score += Number
                    print(f"Your current score : {Score}")
                    Number = int(input(f"Next Move {Moves} : "))

            print("Get Ready to bowl")
            Number = int(input(f"Make your move from these choices {Moves} : "))

            while True:
                CompMove = random.randint(1, 6)
                print(f"My move : {CompMove}")  
                if Number == CompMove:
                    print(CompScore)
                    print(f"My score : {CompScore}   Your Score : {Score}")
                    print("Oops I lost.")
                    game_over = True
                    break
                else:
                    CompScore += CompMove
                    print(f"My current score : {CompScore}")
                    Number = int(input(f"Next Move {Moves} : "))
                    if CompScore > Score:
                        print(f"My score : {CompScore}   Your Score : {Score}")
                        print("Ha! I win")
                        game_over = True
                        break

        elif CompChoice.lower() == "batting":
            # Computer chooses to bat, you bowl
            Number = int(input(f"Make your move from these choices to bowl {Moves} : "))

            while True:
                CompMove = random.randint(1, 6)
                print(f"My move : {CompMove}")
                if Number == CompMove:
                    print(CompScore)
                    print(f"My score : {CompScore}   Your Score : {Score}")
                    print("Oops I lost.")
                    break
                else:
                    CompScore += CompMove
                    print(f"My current score : {CompScore}")
                    Number = int(input(f"Next Move {Moves} : "))
            print("Your turn to bat")
            Number=int(input(f"Your choice from {Moves}: "))

            while True:
                CompMove = random.randint(1, 6)
                print(f"My move : {CompMove}")
                if Number == CompMove:
                    print(Score)
                    print("Hah! you lose")
                    break
                else:
                    Score += Number
                    print(f"Your current score : {Score}")
                    Number = int(input(f"Next Move {Moves} : "))
                    if Score > CompScore:
                        print(f"My score : {CompScore}   Your Score : {Score}")
                        print("Alas! You win")
                        game_over = True
                        break

# IN BATTING- YOU WILL MAKE MOVES FROM 1 TO 6 AND THE NO. YOU CHOOSE WILL GET ADDED TO YOUR SCORE. YOUR GOAL DURING THIS IS TO SCORE AS HIGH AS POSSIBLE. YOU WILL GET OUT IF YOUR GUESS IS SAME AS THE OPPONENT BALLER.

# IN BALLING YOU MUST GUESS WHAT MOVE THE OPPONENT IS GOING TO MAKE AND STOP THEM FROM SCORING.