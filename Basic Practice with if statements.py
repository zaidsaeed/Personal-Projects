#Name : Zaid Saeed
#Student Number : 8621155
# Assignment Number 2
import random
#######Question1####
def size_format(i):
    ''' (Int) --> (Int)
This function takes the number of bytes inputted by the user and tells him/her how many metric units of bytes s/he has (mega,tera, kilo, etc)'''
    if i<0:
        print("Buy a new hard disk")
    elif i < 1000:
        print(i, "B")
    elif i > 1000 and i < (1000**2):
        i = round(i/1000, 1)
        print (i, "KB")
    elif i > (1000**2) and i < (1000**3):
        i = round(i/(1000**2), 1)
        print(i, "MB")
    elif i > (1000**3) and i < (1000**4):
        i = round(i / (1000**3), 1)
        print(i, "GB")
    elif i > (1000**4):
        i = round(i / (1000**4), 1)
        print (i, "terabytes")
        
#######Question2####
def add_article(s):
    ''' (string) --> (string) This function takes in a country's name and adds an article to that country's name depending on whether the country's name is masculine, feminine or plural '''
    if s == "Belize" or s == "Cambodge" or s == "Mexique" or s=="Mozambique" or s == "Zaire" or s=="Zimbabwe":
        print ("le", s)
    elif s[0] in 'aeiouAEIOU':
        print ("l'"+s)
    elif s[len(s)- 1] == "e":
        print ("la",s)
    elif s == "Etats-Uni" or s == "Pay-Bas":
        print ("les",s)
    else:
        print("le",s)
        
#######Question3####
def factorial(n):
    ''' (Integer) --> (Integer) This function asks the user for a number as an input and gives him the factorial of that function as an output.'''
    z = []
    y = []
    f = 1
    if n == 0:
        print (1)
    else:
        for i in range(0,n-1):
            z.append(i)
            h = n-z[i]
            y.append(h)
        for i in range (0, len(y)):
            f = f*y[i] 
        print (f)
        
#######Question4####
def special_count(l):
    ''' (list) --> (int) This function tells you how many numbers in a given list are special, or divisible by 4 and not 100; unless the number is divisible by both 100 and 400 as well. '''
    counter = 0
    for i in range(0, len(l)):
        z = l[i]
        if z >= 0 and z%4 == 0 and not(z % 100 == 0 and z % 400 != 0):
            counter = counter + 1
    print (counter)
    
#######Question5####
def vote():
    '''(Empty) --> (String) The user enters a list of votes and the function tells him/her whether or not the vote passes and with what majority '''
    user_input = input("Enter the yes, no, abstained votes one by one and then press enter:")
    user_input = user_input.strip().lower()
    positive = user_input.count('y')
    negative = user_input.count('no')
    total = negative + positive
    percentage = ((positive/total)*100)
    if percentage == 100:
        print("Proposal passes unanimously")
    elif percentage >= ((2/3)*100):
        print ("Proposal passes with super majority")
    elif percentage >= 50:
        print ("Proposal passes with simple majority")
    else:
        print ("Proposal fails")
        
#######Question6####
#Question6a
def stats_v1(n):
    '''(Integer) --> (Integer, Float) This function takes in a number from the user creates a list of random integers with that number of elements and states the minimum and averge of that set of numbers(This function stores the set of numbers in a list)'''
    total = 0
    z = []
    for i in range (0,n):
        r = random.randint(-100,100)
        z.append(r)
        total = total + r
    print ("The minimum and the average of the following numbers:\n", z, "\n" ,"are", min(z), "and", (total/n))
    
#Question 6b
def stats_v2(n):
    '''(Integer) --> (Integer, Float) This function takes in a number from the user creates a list of random integers with that number of elements and states the minimum and averge of that set of numbers(This function does not store the set of numbers in a list.)'''
    print ("The minimum and the average of the following numbers is:")
    total = 0
    minimum = 100
    for i in range (0,n):
        m = random.randint(-100,100)
        print (m, end = " ")
        total = total + m
        if m < minimum:
            minimum = m
        else:
            minimum = minimum
    average = round((total/n), 2)
    print("\n is", minimum, "and", average)
    
#######Question7####
def emphasize(s):
    ''' (string) --> (string) This function takes string s an input and returns a string with a blank space inserted between every pair of consecutive characters in s.'''
    for i in range(0,len(s)):
        if s[i] < s[len(s)-1]:
            print(s[i] + " ", end = " ")
        else:
            print (s[i], end = " ")
            
#######Question8####
def crypto(s):
    '''(string) --> (string) This function takes in a string from the user and reorders the given string in the order: last, first, second_to_last, second, third_from_the_back, third ….'''
    x = round((len(s))/2)
    if len(s) == 0 or len(s) == 1:
        print(s)
    else:
        for i in range (0, x):
           print(s[(len(s)-1)-i], end = "")
           print(s[i], end = "")
           
#######Question9####
def stranger_things(l1,l2):
    '''(List, List) --> (Boolean) This function compares two given lists to see if their even ranked elements (including zero) are equal and if their odd ranked elements are different.'''
    if len(l1) == len(l2):
         for i in range (0, len(l1)):
             if i%2 == 0 and l1[i] != l2[i]:
                 return False
             elif i%2 != 0 and l1[i] == l2[i]:
                 return False
         return True
    else:
        return False
