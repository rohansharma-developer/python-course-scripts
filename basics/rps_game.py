import random

print("Welcome to Rocks, Paper, Scissors Game!")
choices = ["Rock", "Paper", "Scissors"]
chose = int(input("Choose: \n 0 for Rock \n 1 for Paper \n 2 for Scissors"))
computer = random.randint(0, 2)
print(f"You chose: {choices[chose]}")
print(f"Computer chose: {choices[computer]}")
if computer == chose:
	print("Tie")
elif choices[computer] == "Rock" and choices[chose] == "Paper":
	print("You Won!")
elif choices[computer] == "Paper" and choices[chose] == "Scissors":
	print("You Won!")
elif choices[computer] == "Scissors" and choices[chose] == "Rock":
	print("You Won!")
else:
	print("You Lost!")
