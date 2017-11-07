import random
m = ["rock", "paper", "sisors"]
com = random.choice(m)
player = input("rock paper sisors or quit")
while (player != "quit"):
  com = random.choice(m)
  if (player == "paper"):
    if com == "sisors":
      print("com wins")
    elif (com == "rock"):
      print("You win!")
    else:
      print("tie")
  if (player == "sisors"):
    if com == "rock":
      print("com wins")
    elif (com == "paper"):
      print("You win!")
    else:
      print("tie")
  if (player == "rock"):
    if com == "paper":
      print("com wins")
    elif (com == "sisors"):
      print("You win!")
    else:
      print("tie")
  player = input("rock paper sisors or quit")
