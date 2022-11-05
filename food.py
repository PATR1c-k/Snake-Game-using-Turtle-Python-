from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.color("Blue")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        random_x = random.randint(-300, 300)
        random_y = random.randint(-300, 300)
        self.goto(x=random_x, y=random_y)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-300, 300)
        random_y = random.randint(-300, 300)
        self.goto(x=random_x, y=random_y)
