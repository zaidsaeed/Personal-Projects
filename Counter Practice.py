#Student number = 8621155
#Name : Zaid Saeed
#Assignment 3
#Question 1
def count_pos(l):
    ''' (list) --> string
    This function takes in a list and prints out the number of positive integers in said list.
    eg) Please input a list of numbers separated by commas: 1,-2,9
    There are 2 positive numbers in your list.'''
    z = 0
    try:
        for i in l:
            if i > 0:
                z = z + 1
        return z
    except:
        return 0
#main
s = input("Please input a list of numbers seperated by commas:")
try:
    l = list(eval(s))
except:
    l = 0
print("There are", count_pos(l) ,"positive numbers in your list.")
