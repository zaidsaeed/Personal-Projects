def h_check(m): #checks from right to left
    '''(2D List) --> 1Dlist/ 2D list
    This function takes in a matrix as input
    and returns four numbers if there is an
    arithmetic progression in any of the matrix's rows.
    If no arithmetic progression is detected horizontally, then
    the inputted list is returned for further examinning.'''
    l = []
    if len(m[0]) < 5:
        return m
    for s in range(0,len(m)):
        for i in range(0, len(m[s])-4):
            s1 = m[s][i+4] - m[s][i+3]
            s2 = m[s][i+3] - m[s][i+2]
            s3 = m[s][i+2] - m[s][i+1]
            s4 = m[s][i+1] - m[s][i]
            if s1 == s2 == s3 == s4:
                for j in range(0,4):
                    l.append([s , m[s].index(m[s][j+i])])
                return (l)
    return m

def h_check_1(m): #checks for an arithmetic progression from right to left
    '''(2D List) --> 1Dlist/ 2D list
    This function takes in a matrix as input
    and returns the position of four numbers if there is an
    arithmetic progression in any of the matrix's rows.
    If no arithmetic progression is detected horizontally, then
    the inputted list is returned for further examinning.'''
    l = []
    if len(m[0]) < 5:
        return m
    for s in range(0,len(m)):
        for i in range(0,len(m[s])-4):
            s1 = m[s][i] - m[s][i+1]
            s2 = m[s][i+1] - m[s][i+2]
            s3 = m[s][i+2] - m[s][i+3]
            s4 = m[s][i+3] - m[s][i+4]
            if s1 == s2 == s3 == s4:
                for j in range(0,4):
                    l.append([s , m[s].index(m[s][j+i])])
                return (l)
    return m

def v_check(m): #checks from down to up
    '''(2D List) --> 1Dlist/ 2D list
    This function takes in a matrix as input
    and returns four numbers if there is an
    arithmetic progression in any of the matrix's columns.
    If no arithmetic progression is detected horizontally, then
    the inputted list is returned for further examinning.'''
    if len(m) < 5:
        return m
    l = []
    row = len(m)
    column = len(m[0])
    for i in range(0,column):
        for j in range(0,row-4):
            s1 = m[j+4][i] - m[j+3][i]
            s2 = m[j+3][i] - m[j+2][i]
            s3 = m[j+2][i] - m[j+1][i]
            s4 = m[j+1][i] - m[j][i]
            if s1 == s2 == s3 == s4:
                for s in range(0,4):
                    l.append([s+j, m[s+j].index(m[s+j][i])])
                return l
    return m

def v_check_1(m): #checks from top to bottom
    '''(2D List) --> 1Dlist/ 2D list
    This function takes in a matrix as input
    and returns the position of four numbers if there is an
    arithmetic progression in any of the matrix's columns.
    If no arithmetic progression is detected horizontally, then
    the inputted list is returned for further examinning.'''
    if len(m) < 5:
        return m
    l = []
    row = len(m)
    column = len(m[0])
    for i in range(0,column):
        for j in range(0,row-4):
            s1 = m[j][i] - m[j+1][i]
            s2 = m[j+1][i] - m[j+2][i]
            s3 = m[j+2][i] - m[j+3][i]
            s4 = m[j+3][i] - m[j+4][i]
            if s1 == s2 == s3 == s4:
                for s in range(0,4):
                    l.append([s+j, m[s+j].index(m[s+j][i])])
                return l
    return m

def d1_check(m): #checks from down to up
    '''(2D List) --> 1Dlist/ 2D list
    This function takes in a matrix as input
    and returns the position of four numbers if there is an
    arithmetic progression in the matrix's diagonal from left to right.
    If no arithmetic progression is detected diagonally (left to right), then
    the inputted list is returned for further examinning.'''
    if len(m) or len(m[0]) < 5:
        return m
    l = []
    h = []
    row = len(m)
    column = len(m[0])
    for i in range(0, row-4):
        for j in range(0,column-4):
            s1= m[i+4][j+4] - m[i+3][j+3]
            s2= m[i+3][j+3] - m[i+2][j+2]
            s3= m[i+2][j+2] - m[i+1][j+1]
            s4= m[i+1][j+1] - m[i+0][j+0]
            if s1 == s2 == s3 == s4:
                for s in range(0,4):
                    l.append([i+s,j+s])
                return l
    return m
def d1_check_1(m):
    if len(m) or len(m[0]) < 5:
        return m
    l = []
    h = []
    row = len(m)
    column = len(m[0])
    for i in range(0, row-4):
        for j in range(0,column-4):
            s1= m[i][j] - m[i+1][j+1]
            s2= m[i+1][j+1] - m[i+2][j+2]
            s3= m[i+2][j+2] - m[i+3][j+3]
            s4= m[i+3][j+3] - m[i+4][j+4]
            if s1 == s2 == s3:
                for s in range(0,4):
                    l.append([i+s,j+s])
                return l
    return m

def d2_check(m): #checks from down to up
    '''(2D List) ---> 1D list/ 2D list
    The user enters a 2D list of at least length 5. Then the function takes in
    the list and checks if there is an arithmetic sequence within the elements of the
    list from left to right. If an arithmetic sequence is found, the position of the arithmetic sequence is returned.
    If an arithmetic sequence is not found, then the inputted
    list is returned as is.    
    '''
    if len(m) or len(m[0]) < 5:
        return m
    h = []
    l = []
    row = len(m)
    column = len(m[0])
    for i in range(0, row-4):
        for j in range(1,row-3):
            if i + (row-j) == (row-1):
                s1 = m[i+4][row-(j+4)] - m[i+3][row-(j+3)]
                s2 = m[i+3][row-(j+3)] - m[i+2][row-(j+2)]
                s3 = m[i+2][row-(j+2)] - m[i+1][row-(j+1)]
                s4 = m[i+1][row-(j+1)] - m[0][row-(j)]
            if s1 == s2 == s3 == s4:
                for item in range(0,4):
                    l.append([i+item,-j-item])
                return l
    return m

def ap4(m): #Function compiler
    '''
    (2D list) -> 1D/2D List
    The user enters a 2D list and this function tries to
    find if there is an arithmetic progression first
    horizontally, second verically, third diagonally (left to right),
    fourth diagonally (right to left).
    '''
    s = h_check(m)
    if s ==m:
        s = h_check_1(m)
    if s == m:
        s = v_check(m)
    if s==m:
        s= v_check_1(m)
    if s == m:
        s = d1_check(m)
    if s == m:
        s = d2_check(m)
    if s == m:
        return ([])
    return s
    
        
                
                
