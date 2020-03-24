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
        #raise the max and min by the amount of correct problems more than 7.
        factMin += correct - 7
        factMax += correct - 7 
    else:
        if factMin - 10 - correct > 0:
            factMin -= 10 - correct
        else:
            factMin = 1

        if factMax - 10 - correct > 2:
            factMax -= 10 - correct
        else:
            factMax = 3
        
    print(str(correct) + "/10")
    print("\n")


    