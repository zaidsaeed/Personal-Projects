#Assignment Question 1
def lbs2kg(w):
    '" (float) --> (float) The user inputs the given weight in pounds/n and the function converts such weight to kilograms."'
    kg = 0.453592*w
    return kg

#Assignment Question 2
def id_formater(fn, ln, appelation, city, year):
      "' This id will gather the user's information and print it in the correct order, as in an id'"
      print(appelation+ "." + ln,",", fn , "(" + city + "," + str(year) + ")")
#check spaces
 
#Assignment Question 3
def limerick_maker():
    ''' (string, string) --> (string) This function adds a person's name and city of birth into a limerick '''
    name = input("Enter your name:")
    c_o_b = input("Enter your city of birth:")
    print(name, '''had funny funny hair
With tons and tons to spare\n'''+
name+ '''\'s clippings made a wig
It was very big\nAnd caused the townsfolk of''', c_o_b, "to stare")

#Assignment Question 4
def id_formater_display():
    ''' (string, string, string, string, string) --> (string) This function concates information into an id display. '''
    fn = input("What is your first name?")
    ln = input("What is your last name?")
    appelation = input("What is your appellation?")
    city = str(input("Where were you born?"))
    year = input("What is your year of birth?")
    id_formater(fn, ln, appelation, city, year)
    
    
#Assignment Question 5
    
def l2loz(w):
    ''' (integer) --> (integer, float) When given an integer for input, this function returns an integer and a float that make up that number as well '''
    l = w//1
    o = 16*(w%1)
    print (l, o)

#Assignment Question 6
def draw_soccer_field():
    '''This function is meant to draw a virtual soccer field'''
    import turtle
    s=turtle.Screen()
    s.bgcolor("Green")
    t=turtle.Turtle()
    t.speed(1000)
    #Frame of field
    t.penup()
    t.goto(-325,200)
    t.pendown()
    t.goto(-325,-200)
    t.goto(325,-200)
    t.goto(325,200)
    t.goto(-325,200)
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.goto(0,200)
    t.goto(0,-200)
    t.goto (0,0)
    #Dot in the middle
    t.dot(25)
    #Circle in the middle of the field
    t.goto(0,-75)
    t.circle(75)
    
    # first two Corner quarter circles
    t.penup()
    t.goto(325,180)
    t.pendown()
    t.circle(20, -90)
    t.left(90)
    t.penup()
    t.goto(-325,180)
    t.pendown()
    t.circle(20,90)
    t.left(90)
    t.penup()
    t.goto(320,-200)
    t.right(90)
    t.pendown()
    t.right(180)
    
    



    #First Penalty Box
    t.penup()
    t.goto(325,125)
    t.pendown()
    t.goto(185,125)
    t.goto(185,-125)
    t.goto(325,-125)

    #Second Penalty Box
    t.penup()
    t.goto(-325,125)
    t.pendown()
    t.goto(-185,125)
    t.goto(-185,-125)
    t.goto(-325,-125)

    #First Inner Box
    t.penup()
    t.goto(325,75)
    t.pendown()
    t.goto(250,75)
    t.goto(250,-75)
    t.goto(325,-75)

    #Second Inner Box
    t.penup()
    t.goto(-325,75)
    t.pendown()
    t.goto(-250,75)
    t.goto(-250,-75)
    t.goto(-325,-75)
    t.left(90)

    t.penup()
    t.goto(-215,0)
    t.pendown()
    t.dot(15)
    t.penup()
    t.goto(215,0)
    t.pendown()
    t.dot(15)
    t.penup()
    t.goto(185,-55)
    t.pendown()
    t.circle(55,-180)
    t.penup()
    t.goto(-185,55)
    t.pendown()
    t.circle(55, -180)    

    t.penup()
    t.goto(-305,-200)
    t.pendown()
    t.left(90)
    for i in range (34):
        t.forward(1)
        t.left(3)
    t.penup()
    t.goto(305,-200)
    t.pendown()
    t.right(90)
    for i in range (36):
        t.forward(1)
        t.right(3)
    t.penup()
        
    
    
    
    
   
    

#Assignment Question 7
def median3(n,m,z):
    ''' (integer, integer, integer) --> (integer)
The user will input three integers and the machine will provide the median of those three numbers'''
    for i in (n,m,z):
        if i is max(n,m,z):
            print("This is not the median:", i)
        elif i is min(n,m,z):
            print("This is not the median:", i)
        else:
            print ("This is the median:", i)

#Assignment Question 8
def below_parabola(a,b,p,q):
    ''' (int, int, int, int) --> (Boolean) This function will tell you whether specific given
points belong on or under a specific function'''
    if q <= (a*(p**2)+ b):
        print (True)
    else:
        print (False)                  

#Assignment Question 9
def projected_grade(a1,A1,a2,A2,m,M):
    ''' (float, float,float, float, float, float) --> (float) This function is used to predict the grade of a student in a specific class.'''
    assignment1 = (a1/A1)
    assignment2 = (a2/A2)
    midterm = (m/M)
    assignment3 = ((assignment1+assignment2)/2)
    final = midterm
    complete_grade = ((((assignment1*0.05)+(assignment2*0.05)+(assignment3*0.05)+(midterm*0.35)+(final*0.5))) * 100)
    return (complete_grade)

#Assignment Question 10
def projected_grade_V2():
    ''' (float, float,float, float, float, float) --> (float) This function is used to predict the grade of a student who fails his/her midterm. Such a grade is meant to punish the student with the lowest grade possible.'''
    a1 = int(input("How many points did you get on assignment1?"))
    A1 = int(input("What was the maximum number of points for assignment number one?"))
    a2 = int(input("How many points did you get on assignment 2?"))
    A2 = int(input("What was the maximum number of points for assignment number two?"))
    m = int(input("How many points did you get on the midterm?"))
    M = int(input("What was the maximum number of possible points for the midterm?"))

    midterm_score = (m/M)*35
    final_score = (m/M)*50
    
    computed_grade = midterm_score + final_score
    
    if computed_grade < 50 and computed_grade < projected_grade(a1,A1,a2,A2,m,M):
        print((computed_grade)*(100/85))
    elif computed_grade < 50 and computed_grade > projected_grade(a1,A1,a2,A2,m,M):
        print(projected_grade(a1,A1,a2,A2,m,M))
    else:
        print(projected_grade(a1,A1,a2,A2,m,M))



#Assignment Question 11
def change_to_coins(amount):
    ''' (float) --> (int, int, int, int) '''
    amount = amount*100
    no_of_quarters = round((amount//25),2)
    amount = round(amount%25,2)
    no_of_dimes = round((amount//10),2)
    amount = round(amount%10,2)
    no_of_nickels = round((amount//5),2)
    amount = round(amount%5,2)
    no_of_pennies = round(amount,2)
    print(no_of_quarters, no_of_dimes, no_of_nickels, no_of_pennies)



