#Zaid Saeed
#23/11/2016
#Student Number: 8621155

#1a
def largest_34(a):
    '''(list) --> int
    This function takes in a list and returns the
    sum of the 3rd and 4th largest values of list a'''
    a.sort()
    return (a[3] + a[4])
#1b
def largest_third(a):
    ''' () --> int
    This function takes in a list and computes the
    sum of the len(a)//3 largest integers of the list '''
    a.sort()
    f = len(a)//3
    t = a[len(a)-f:]
    z = sum(t)
    #The instructions said compute and not return

#1c
def third_at_least(a):
    '''(list) --> int/ None
    This function returns a value that appears len(a)//3 +1 times
    in a list. If such value doesn't exist, the function returns
    None.'''
    c = 1
    a = sorted(a)
    for i in range(0, len(a)-1):
        if a[i] == a[i+1]:
            c = c + 1
        if c == (len(a)//3 + 1):
            return a[i]
        if a[i] != a[i+1]:
            c = 1
    return None
#1d
def sum_tri(a,x):
    '''(list, int) --> bool
    This function takes in a list, and if there exists indices i, j
    and k (where i and j and k are not necessarily distinct)
    such that a[i]+a[j]+a[k]=x, then it returns True. Otherwise, the function
    returns False'''
    for i in range(0,len(a)):
        for j in range(0,len(a)):
            for k in range(0,len(a)):
                if a[i] + a[j] + a[k] == x:
                    return True
    return False
        
        
    
