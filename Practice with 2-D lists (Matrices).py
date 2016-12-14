def indexes(t, c):
    ''' (string, string) --> list
    This function takes in a word and list and returns the indexes
    in the given word in which the given charachter is present
    in the given word.'''
    l = []
    for i in range(0, len(t)):
        if t[i] == c:
            l.append(i)
    return l

def doubles(l):
    '''
    (list) --> string
    This function takes in a list and prints all the elements
    that are twice the integer that come before it.'''
    for i in range(0, len(l)-1):
        if 2*l[i] == l[i+1]:
            print(l[i+1])
def four_letter(l):
    '''
    (list) --> sublist
    This function takes in a list of words, and it returns
    a sublist of the words with four letters in the list.'''
    z = []
    for i in range(0,len(l)):
        if len(l[i]) == 4:
            z.append(l[i])
    return z
def inBoth(l1, l2):
    '''(list1 , list2) --> bool
    This function takes in two lists and returns True if an element
    is common in both lists, and False otherwise.'''
    for i in range(0,len(l1)):
        for j in range(0,len(l2)):
            if l1[i] == l2[j]:
                return True
        return False
def intersect(l1,l2):
    '''(list1, list2) --> list
    This function takes in two lists that contain no duplicates
    within them and returns the elements that occurr in each list'''
    z = []
    for i in range(0,len(l1)):
        for j in range(0, len(l2)):
            if l1[i] == l2[j]:
                z.append(l1[i])
    return z

def pair(l1, l2, s):
    ''' (list1, list2, int) --> int, int
    This function takes two lists and an integer
    and returns the pairs where an element is present
    in both lists each that add to the given integer'''
    for i in range(0,len(l1)):
        for j in range(0, len(l2)):
            if l1[i] + l2[j] == s:
                print(l1[i], end = ' ')
                print(l2[j])
def pairSum(l, s):
    ''' (list, integer) --> int, int
    This function takes in a list and integer and returns
    the INDEXES of the pairs of elements in the list
    that add up to the given index.'''
    for i in range(0, len(l)):
        for j in range(0, len(l)):
            if i < j and l[i] + l[j] == s:
                print (i, end = "  ")
                print (j)
def lastfirst(l):
    ''' (list) --> list
    This function takes in a list of last and first
    names, and returns a list with all the last names
    in one subliist, and all the first names in another
    sublist'''
    r = []
    first = []
    last = []
    for i in range(0, len(l)):
        t = l[i].split(',')
        first.append(t[0])
        last.append(t[1])
    r.append(first)
    r.append(last)
    return r
def subsetSum(l, i):
    '''(list, int) --> bool
    This function takes in a list and a target
    integer, it returns True if three numbers
    within the list add up to the target
    integer, and false otherwise.'''
    for t in l:
        for j in l:
            for z in l:
                if t != z != j and t + z + j  == i:
                    return True
    return False
def mystery(n):
    '''(int) ---> int
    This function takes in an integer and returns the
    number of times the number can be halved (using
    integer division) before it becomes 1'''
    counter = 0
    while n != 1:
        n = n//2
        counter = counter + 1        
    return counter
def inversions(t):
    ''' (string) --> int
    This string takes in a text and returns the number inversions
    in the inputed text.
    eg)
    inversions('ABBFHDL')
    2'''
    # this one doesn't completly work; unfortunately
    c = 0
    for i in range(0, len(t)-1):
        if t[i] > t[i+1]:
            c = c + 1
            for j in range(i+2, len(t)):
                if t[i] > t[j]:
                    c = c + 1
    return c
def sublist(l1, l2):
    ''' (l1, l2) --> Bool
    This function takes in two lists and returns
    True if l1 is a sublist of list 2.
    eg) [15, 1, 100] is a sublist of
    [20, 15, 30, 50, 1, 100] because all the elements in list
    1 appear in list 2, in the same order as list 1, but not
    consecutively.'''
    #you left off here; pick up from here plz
    c = 0
    i = 0
    while i != len(l1)-1:
        for i in range(0, len(l1)-1):
            if l1[i] in l2:
                c = c +1
                l1 = l1[i+1:]
    if c == len(l1):
        return True
    else:
        return False
