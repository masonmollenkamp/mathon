pig = (eval(input("traslate pig laten into englesh 0 no 1 yes")))
if (pig == 1):
  word = (input("what is the latin word"))
  h = word[-3:-2] + word[:-3].lower()
  print(h)
else:
  word = (input("what is the word"))
  h = word[1:] + word[:1] + "ay"
  print(h)
