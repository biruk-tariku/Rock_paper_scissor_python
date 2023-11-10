# Rock_paper_scissor_python

a simple implementation of the classic Rock, Paper, Scissors game between a player (Player 1) and a computer-generated opponent (Player 2). The code takes input from the player, generates a random choice for Player 2, and then determines the winner based on the game's rules.


Here's a breakdown of how your code works:

1. `import random`: Imports the random module, which you'll use to generate a random choice for Player 2.

2. `player1 = input("Choose Rock, Paper, or Scissor: ").lower()`: Prompts the player to input their choice (Rock, Paper, or Scissors) and converts the input to lowercase to ensure case-insensitive comparison.

3. `player2 = random.choice(["rock", "paper", "scissor"]).lower()`: Generates a random choice for Player 2 (the computer) from the list of ["rock", "paper", "scissor"] and converts it to lowercase.

4. `print("Player 2 chose:", player2)`: Prints Player 2's choice to the console.

5. The following conditional statements check the outcome of the game:
   - If Player 1 chose "rock" and Player 2 chose "paper," Player 2 wins.
   - If Player 1 chose "paper" and Player 2 chose "scissor," Player 2 wins.
   - If Player 1 chose "scissor" and Player 2 chose "rock," Player 2 wins.
   - If both players made the same choice, it's a tie.
   - Otherwise, Player 1 wins.

6. The program prints the result of the game based on the condition that evaluates as true.

Overall, the code effectively simulates a simple Rock, Paper, Scissors game between a human player and a computer opponent.
