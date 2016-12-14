#Assignment 3
#Date:30/10/2016
#Zaid Saeed
#Student Number: 8621155

#Question3
def two_length_run(l):
    '''(list)-> intger
    A run is when the same integer is repeated consecutivly. This function returns to the user the length of the longest run in his/her inputted list.
    eg)Please input a list of numbers separated by commas: 6,6,7,1,1,1,1,4,1
    4
    '''
    i = 0
    z = 1
    run = []
    try:
        while i < (len(l)-1):
            if l[i] == l[i+1]:
                z = z + 1
            elif l[i] != l[i+1]:
                z = 1
            run.append(z)
            i = i + 1       
        return max(run)
    except:
        return 0

s = input("Please input a list of numbers separated by commas: ")
try:
    l = list(eval(s))
except:
    l = 0
print (two_length_run(l))
