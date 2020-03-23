import random

factMin = 1
factMax = 5

#Dynamicly change
for test in range(10):
    #Do ten problems and count the number correct
    correct = 0

    for n in range(10):
        dividend = random.randint(factMin, factMax)
        answer = random.randint(factMin, factMax)
        total = dividend * answer

        if input(str(total) + " / " + str(dividend)) == str(answer):
            correct += 1
    
    if correct > 7:
        factMin += correct - 8
        factMax += correct - 8
    else:
        factMin -= correct
        factMax -= correct

    
    print(str(correct) + "/10")


    