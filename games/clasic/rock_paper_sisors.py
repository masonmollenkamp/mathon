import random
m = ["rock", "paper", "sissors"]
com = random.choice(m)
print("boost gives you 7 in 10 chance of winning")
player = input("rock paper sissors boost or quit")
while (player != "quit"):
  if player == "boost":
    input("rock paper or sissors")
    win = random.randrange(1,10)
    if player == "boost":
      if win < 7:
        print("You win!")
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
  player = input("rock paper sissors boost or quit")
