class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy
        return (self.x, self.y)

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return '('+str(self.x)+','+str(self.y)+')'
    
    def __lt__(self,x2):
        '''(Point, Point) --> bool
        This function takes in two points and returns
        True if the y point of the self point is greater than the y-point
        of the given point, and false otherwise'''
        return self.x < x2.x
    def __gt__(self, x2):
        '''(Point, Point) --> bool
        This function takes in two points and returns
        True if the y point of the self point is greater than the y-point
        of the given point, and false otherwise'''
        return self.y > x2.y
    

class Rectangle(Point):
    def __init__(self, p1, p2, color):
        '''(Rectangle, Point, Point, str) -> None
        Initializes rectangle points to given points'''
        self.p1 = p1
        self.p2 = p2
        self.color = color
    def __repr__(self):
        '''(Rectangle)--> str
        This function returns a string identifying the self Rectangle'''
        return 'Rectangle (' + str(self.p1) + ',' + str(self.p2) + ',' + str(self.color) + ')'
    def get_color(self):
        '''(Rectangle) -> str
        This function returns the color of the given rectangle'''
        return (self.color)
    def get_bottom_left(self):
        '''(Rectangle) --> Point
        This function returns the coordinates of the lower-left most points
        of a rectangle'''
        if self.p1 < self.p2 and self.p1 < self.p2:
            return self.p1
        else:
            return self.p2
    def get_top_right(self):
        '''(Rectangle) --> Point
        This function returns the coordinates of the upper-right most points
        of a rectangle'''
        if self.p1 > self.p2:
            return self.p1
        else:
            return self.p2
    def reset_color(self, color):
        ''' (Rectangle, color) -> None
        This function changes the color of the considered rectangle to
        the inputted rectangle'''
        self.color = color
    def get_color(self):
        ''' (Rectangle) --> str
        This function returns the color of a given rectangle'''
        return self.color
    def move(self, dx, dy):
        ''' (Rectangle, int, int) --> Rectangle
        This function takes in a rectangle and two integers and moves
        the points of rectangles by the given values.'''
        self.p1 = self.p1.move(dx,dy)
        self.p2 = self.p2.move(dx,dy)
        return self
    def __str__(self):
        '''(Rectangle) --> str
        This function returns the identity of the given rectangle'''
        return ('I am a blue rectangle with a bottom left corner at ' + self.get_bottom_left().__str__() + ' and a top left corner at ' + self.get_top_right().__str__())
    def __eq__(self, x2):
        ''' (Rectangle, Rectangle) --> Bool
        This function returns True if both of the points of both of the rectangles are
        equal and False otherwise.'''
        return (self.p1 == x2.p1 and self.p2 == x2.p2 and self.color == x2.color)
    def get_perimeter(self):
        '''(Rectangle) --> int
        This function takes in a rectangle and returns the length of the
        perimeter created by the endpoints of the rectangle'''
        return 2*(self.get_top_right().x - self.get_bottom_left().x) + 2*(self.get_top_right().y - self.get_bottom_left().y )
    def get_area(self):
        '''(Rectangle) --> int
        This function returns the value of the area created by the given rectangle'''
        return (self.get_top_right().y - self.get_bottom_left().y) * (self.get_top_right().x - self.get_bottom_left().x)
    def contains(self, x, y):
        ''' (Rectangle, int, int) --> True/None
        This function takes in a rectangle and an x and y coordinate
        and returns true if the point created by those two coordinates belonged
        in the given rectangle'''
        self.x = x
        self.y = y
        if self.get_bottom_left().x <= self.x <= self.get_top_right().x and self.get_bottom_left().y <= self.y <= self.get_top_right().y:
            return True
        else:
            return None
    def intersects(self, r):
        ''' (Rectangle, Rectangle) --> True/None
        This function takes in two rectangles and returns True if the sides of both rectangles intersect
        and None otherwise'''
        self.r = r
        if self.get_bottom_left().x <= self.r.get_bottom_left().x <= self.get_top_right().x and self.r.get_bottom_left().y <= self.get_top_right().y <= self.r.get_top_right().y:
            return True
        else:
            return None
class Canvas:
    def __init__(self):
        '''(Canvas)--> None
        This function initializes a canvas'''
        self.c = []
    def __repr__(self):
        '''(Canvas) --> str
        This function returns the identity of the given canvas'''
        return str(self.c)
    def __len__(self):
        '''(Canvas) --> int
        This function takes in a canvas and returns the number of rectangles
        in that chosen canvas'''
        return len(self.c)
    def add_one_rectangle(self, r1):
        '''(Canvas) --> None
        This function appends a rectangle to canvas'''
        self.r1 = r1
        self.c.append(self.r1)
    def count_same_color(self, color):
        '''(Canvas) --> int
        This function takes in a canvas and returns the number of rectangles
        with the same color in that given canvas'''
        c = 0
        self.color = color
        for i in self.c:
            if i.get_color() == self.color:
                c = c+1
        return c
    def total_perimeter(self):
        ''' (Canvas) --> int
        This function takes in a given a canvas and returns the perimeters
        of all the rectangles in the given canvas'''
        c = 0
        for i in self.c:
            c = i.get_perimeter() + c
        return c
    def min_enclosing_rectangle(self):
        ''' (Canvas) --> Rectangle
        This function takes in a canvas and returns a rectangle (with the least
        area) that encloses all the rectangles in the given canvas.'''
        minix = self.c[0].get_bottom_left().x
        maxix = self.c[0].get_top_right().x
        miniy = self.c[0].get_bottom_left().y
        maxiy = self.c[0].get_bottom_left().y
        for i in self.c:
            if i.get_bottom_left().x < minix:
                minix = i.get_bottom_left().x
            if i.get_bottom_left().y < miniy:
                miniy = i.get_bottom_left().y
            if i.get_top_right().x > maxix:
                maxix = i.get_top_right().x
            if i.get_top_right().y > maxiy:
                maxiy = i.get_top_right().y
        return Rectangle(Point(minix, miniy), Point(maxix, maxiy), 'red') #How do i get the point to show up in the repr command?
    def common_point(self):
        ''' (Canvas) --> bool
        This function returns True if a common point is present within
        all the rectangles in a canvas and False otherwise. '''
        for i in self.c:
            for z in self.c:
                if i.intersects(z) != True:
                    return False
        return True
            
    
    
