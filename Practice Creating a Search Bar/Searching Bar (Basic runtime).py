lines = open('NYT-bestsellers(1).txt').read().splitlines()
l = []
for i in lines:
    l.append(i.split('\t'))

#Now we have the entire txt. document as a 2-D list called l
def begin(): #if somebody clicks enter and the program continues on functioning without crashing, is that okay?
    user1 = input('What would you like to do? Enter 1, 2, 3, 4, 5, 6 or Q for answer. \n1: Look up year range \n2: Look up month/year\n3: Search for author\n4: Search for title\n5: Number of authors with at least x bestsellers\n6: List y authors with the most bestsellers\nQ: Quit\nAnswer (1,2,3, 4, 5, 6, Q or q):')
    try:
        while user1 not in ('123456Qq'):
            print('\nIf you answer is not Q or q, then it must be an integer.\nInvalid input, try again.\n')
            user = int(input('What would you like to do? Enter 1, 2, 3, 4, 5, 6 or Q for answer. \n1: Look up year range \n2: Look up month/year\n3: Search for author\n4: Search for title\n5: Number of authors with at least x bestsellers\n6: List y authors with the most bestsellers\nQ: Quit\nAnswer (1,2,3, 4, 5, 6, Q or q):'))
    except:
        while user1 not in ('1,2,3,4,5,6,Q,q'):
            print('\nIf you answer is not Q or q, then it must be an integer.\nInvalid input, try again.\n')
            user1 = int(input('What would you like to do? Enter 1, 2, 3, 4, 5, 6 or Q for answer. \n1: Look up year range \n2: Look up month/year\n3: Search for author\n4: Search for title\n5: Number of authors with at least x bestsellers\n6: List y authors with the most bestsellers\nQ: Quit\nAnswer (1,2,3, 4, 5, 6, Q or q):'))
    return user1
def calender_split_year(m):
    '''
    (str) --> int
    This function takes in a date as a string and returns the year
    of that given date.
    '''
    s = m.split('/')
    s.remove(s[0])
    s.remove(s[0])
    return int(s[0])

def calender_split_month(m):
    s = m.split('/')
    s.remove(s[1])
    s.remove(s[1])
    return int(s[0])

def option1():
    user1 =0
    user2 = 0
    while user1 < 999 or user1 > 9999 or user2 < 999 or user2 >9999:
        try:
            while user1<999 or user1>9999:
                print("Enter a 4-digit integer, please.")
                user1 = int(input('Enter beginning year:'))
            while user2<999 or user2>9999:
                print("Enter a 4-digit integer, please.")
                user2 = int(input('Enter an end year:'))
        except:
            while user1<999 or user1>9999:
                print("Enter a 4-digit integer, please.")
                user1 = int(input('Enter beginning year:'))
            while user2<999 or user2>9999:
                print("Enter a 4-digit integer, please.")
                user2 = int(input('Enter an end year:'))               
    for i in range(0,len(l)):
        s = l[i]
        t = calender_split_year(s[3])
        if t >= int(user1) and t <= int(user2):
            print (s[0] + ', by', s[1] , '('+s[3]+ ')')
        elif user1 < 1941 or user2 > 2013:
            print ("No books were found in that range.")
def option2():
    user1 =0
    user2 = 0
    while user1<1 or user1>12:
        print("Enter a 1-digit integer, please.")
        user1 = int(input('Enter month:'))
    while user2<999 or user2>9999:
        print("Enter a 4-digit integer, please.")
        user2 = int(input('Enter a year:'))
    for i in range(0, len(l)):
        s = l[i]
        t = calender_split_month(s[3])
        x = calender_split_year(s[3])
        if t == user1 and x == user2:
            print (s[0] + ', by', s[1] , '('+s[3]+ ')')

def option3():
    user1 = input('Enter an authour\'s name or (part of name:)')
    for i in range(0,len(l)):
        s = l[i]
        if user1 in s[1]:
            print(s[0] + ', by', s[1] , '('+s[3]+ ')')

def option4():
    user1 = input('Enter a tittle of part of tittle:')
    for i in range(0,len(l)):
        s =l[i]
        if user1 in s[0].lower():
            print(s[0] + ', by', s[1] , '('+s[3]+ ')')

def frequency(books):
    f = []
    for i in range(0, len(books)):
        s = books[i]
        flag = False
        for j in range(0, len(f)):
            if s[1] == f[j][0]:
                f[j][1]=f[j][1]+1
                flag=True
        if not(flag):
            f.append([s[1], 1])
    return f

def option5():
    user1 = int(input('Enter an integer bigger than zero:'))
    f = []
    for i in range(0, len(l)):
        s = l[i]
        flag = False
        for j in range(0, len(f)):
            if s[1] == f[j][0]:
                f[j][1]=f[j][1]+1
                flag=True
        if not(flag):
            f.append([s[1], 1])
    for z in range(0,len(f)):
        if f[z][1] >= user1:
            print(f[z][0], 'with', f[z][1], 'bestsellers.')

def option6():
    user1 = int(input('Enter an integer bigger than zero:'))
    f = []
    for i in range(0, len(l)):
        s = l[i]
        flag = False
        for j in range(0, len(f)):
            if s[1] == f[j][0]:
                f[j][1]=f[j][1]+1
                flag=True
        if not(flag):
            f.append([s[1], 1])
    for x in range(0, len(f)-1):
          index_of_min=x
          for s in range(x+1, len(f)):
               if(f[index_of_min][1]>f[s][1]):
                    index_of_min=s
          f[x][0],f[index_of_min][0]  = f[index_of_min][0], f[x][0]
          f[x][1], f[index_of_min][1] = f[index_of_min][1], f[x][1]
    for t in range(1,user1+1):
        print (str(t)+ '.', f[-t][0])
def play_game():
    user1 = begin()
    s = 'q'
    while user1 != s.lower().strip():
        if int(user1) ==1:
            option1()
            print()
            play_game()
        if int(user1) ==2:
            option2()
            print()
            begin()
            play_game()
        if int(user1) == 3:
            option3()
            print()
            begin()
            play_game()
        if int(user1) == 4:
            option4()
            print()
            begin()
            play_game()
        if int(user1) == 5:
            option5()
            print()
            begin()
            play_game()
        if int(user1) == 6:
            option6()
            print()
            begin()
            play_game()

play_game()
