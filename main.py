import random

'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([1, -1, 0])

youstr = input("Enter your choice (s = snake, w = water, g = gun): ").lower()

youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}


if youstr not in youDict:
    print("Invalid choice! Please choose s, w, or g.")
    exit()

you = youDict[youstr]

print(f"You chose {reverseDict[you]}")
print(f"Computer chose {reverseDict[computer]}")

if computer == you:
    print("It's a draw ")

elif (computer == -1 and you == 1) or \
     (computer == 1 and you == 0) or \
     (computer == 0 and you == -1):
    print("You win 🎉")

else:
    print("You lose ")
