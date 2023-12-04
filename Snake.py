import turtle
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake_segment = turtle.Turtle("square")
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(position)
        self.segments.append(snake_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
        
    def move(self):
        for segment_number in range(len(self.segments)-1, 0, -1):
            next_x = self.segments[segment_number -1].xcor()
            next_y = self.segments[segment_number -1].ycor()
            self.segments[segment_number].goto(next_x, next_y)

        self.segments[0].forward(20)

    def up(self):
        if(self.head.heading() != 270):
            self.head.seth(90)
    
    def down(self):
         if(self.head.heading() != 90):
            self.head.seth(270)
    def left(self):
        if(self.head.heading() != 0):
            self.head.seth(180)
    def right(self):
        if(self.head.heading() != 180):
            self.head.seth(0)

    def w(self):
        if(self.head.heading() != 270):
            self.head.seth(90)
    
    def s(self):
         if(self.head.heading() != 90):
            self.head.seth(270)
    def a(self):
        if(self.head.heading() != 0):
            self.head.seth(180)
    def d(self):
        if(self.head.heading() != 180):
            self.head.seth(0)

    def reset(self):
        for segment in self.segments:
            segment.hideturtle()
            
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    