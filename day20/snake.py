import turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """This class stores the method and attributes of the snakes in the snake game"""

    def __init__(self):
        self.color = 'white'
        self.starting_position = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        self.MOVE_DISTANCE = 20
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in self.starting_position:
            new_segment = turtle.Turtle()
            new_segment.shape('square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def up(self):
        if self.head.heading() != UP and self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP and self.head.heading() != DOWN:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT and self.head.heading() != LEFT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != RIGHT and self.head.heading() != LEFT:
            self.head.setheading(0)

    def next_move(self):
        self.head.forward(self.MOVE_DISTANCE)

    def update(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.next_move()

    def add_segment(self, position):
        new_segment = turtle.Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position)



