import random
nodeinput = {"weather" : [random.randint(0, 1), 1], "weekend" : [random.randint(0, 1), 1]}

leave = False
while leave != True:
    value = (nodeinput["weather"][0] * nodeinput["weather"][1]) + (nodeinput["weekend"][0] * nodeinput["weather"][1])
    print(value)
    corect = input("your answer: weather {} weekend {}".format(nodeinput["weather"], nodeinput["weekend"]))
    if value == corect:
        correct += {str([nodeinput["weather"][0] + [nodeinput["weather"][0]]) : "*"]}