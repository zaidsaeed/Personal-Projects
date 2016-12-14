#Question2
def two_length_run(l):
    ''' (list) --> bool
    This function takes in a list and returns to the user if any integers stated in the list repeat one after the other.
    eg)Please input a list of numbers separated by commas: 1,2,3,3,3,4,6,5
    True'''
    try:
        for i in range(len(l)-2):
            if l[i] == l[i+1]:
                return True
        return False
    except:
        return False

s = input("Please input a list of numbers separated by commas: ")
try:
    l = list(eval(s))
except:
    l = 0
print (two_length_run(l))
