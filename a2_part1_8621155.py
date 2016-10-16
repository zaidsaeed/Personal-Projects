def perform_test():
    import random
    print("How many questions would you like to be tested on?")
    n = int(input("Enter a non negative integer for the answer:"))
    print ("This software tests you with", n, "questions:")
    print ("0) Addition")
    print ("1) Multiplication")
    o = int(input("Please make a selection (0 or 1):"))
    print("Please give the answers to the following additions:")
    s = random.sample(range(1,10),n)
    t = random.sample(range(1,10),n)
    counter = 0
    if o == 0:
        for i in range(0, n):
            print(s[i], end = " ")
            print ("+", end = " ")
            print (t[i], end = " ")
            z = int(input("="))
            if z != (s[i] + t[i]):
                print ("Incorrect! The correct answer is:", (s[i] + t[i]))
            else:
                counter = counter + 1
        if ((counter/n)*100) >= 80:
             print("Well done! Congratulations.")
        elif ((counter/n)*100) >= 60 and ((counter/n)*100) <= 80:
             print("Not too bad but please study and practice some more.")
        else:
             print("Please study more and ask your teacher for help.")

    if o == 1:
        for i in range(0, n):
            print(s[i], end = " ")
            print ("*", end = " ")
            print (t[i], end = " ")
            z = int(input("="))
            if z != (s[i] * t[i]):
                print ("Incorrect! The correct answer is:", (s[i] * t[i]))
            else:
                counter = counter + 1
        if ((counter/n)*100) >= 80:
             print("Well done! Congratulations.")
        elif ((counter/n)*100) >= 60 and ((counter/n)*100) <= 80:
             print("Not too bad but please study and practice some more.")
        else:
             print("Please study more and ask your teacher for help.")
