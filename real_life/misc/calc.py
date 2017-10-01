print ("for some reson the thig prints 4 answers the\n ones on the middle arecorrect \nand the continuing thing is brocen on mulipaction")
i = (5)
done = (0)
for i in range (0,10):
  if(done == 2):
      break 
  
  ecwater =(eval(input("1 = + 2 = - 3 = x 4 = %")))
  three = 0 
  if (done == 0):
    first_number = (eval(input("firt number")))
  two_number = (eval(input("seconed number")))
  if (done == 0):
    three_number = (eval(input("do you want 3erd number 0 no 1 yes")))
  if (three_number == 1 and done == 0):
    three = (eval(input("what is it")))
  if (ecwater == 1):
    if(three_number == 1):
      first_number = (first_number + two_number + three)
      print(first_number)
      done = 1
  if (three_number == 0):
      first_number = (first_number - two_number)
      print (first_number)
  if (ecwater == 2):
    if(three_number == 1):
      first_number = (first_number - two_number - three)
      print(first_number)
      done = 1
  if (three_number == 0):
      first_number = (first_number * two_number)
  if (ecwater == 3):
    if(three_number == 1):
      first_number = (first_number * two_number * three)
      print(first_number)
      done = 1
  if (three_number == 0):
      first_number + (first_number * two_number)
  if (ecwater == 4):
     if(three_number == 1):
       answer = (first_number / two_number)
       print(answer / three)
  if (three_number == 0):
    print (first_number + two_number)
  done1 =(eval(input("do you want to continue")))
  if (done1 != 1):
    done = 2
  if (done1 == 1):
    done = 1
    done = (1)
rateing = (eval(input("plese rate 1-10")))
if (rateing <= 4):
  why = input("why")
  print ("plese contact masonmollenkamp@gmail.com")
else:
  print("if you want to add something contact\nmasonmollnekamp@gmail.com")
