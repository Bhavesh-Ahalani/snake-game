from turtle import Turtle

WIDTH, HEIGHT = 590, 590


class Border(Turtle):
    def __init__(self):
        super(Border, self).__init__()
        self.min_x = -WIDTH / 2
        self.max_x = WIDTH / 2
        self.min_y = -HEIGHT / 2
        self.max_y = HEIGHT / 2
        self.penup()
        self.hideturtle()
        self.goto(x=self.min_x, y=self.min_y)
        self.pendown()
        self.color("white")
        self.goto(x=self.min_x, y=self.max_y)
        self.goto(x=self.max_x, y=self.max_y)
        self.goto(x=self.max_x, y=self.min_y)
        self.goto(x=self.min_x, y=self.min_y)
