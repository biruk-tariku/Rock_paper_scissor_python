import random
player1 = input("Choose Rock, Paper, or Scissor: ").lower()
player2 = random.choice(["rock", "paper", "scissor"]).lower()
print("Player 2 chose:", player2)

if player1 == "rock" and player2 == "paper":
    print("Player 2 won")
elif player1 == "paper" and player2 == "scissor":
    print("Player 2 won") 
elif player1 == "scissor" and player2 == "rock":
    print("Player 2 won")
elif player1 == player2:
    print("It's a Tie")
else:
    print("Player 1 won")
