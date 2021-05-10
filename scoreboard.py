from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.penup()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())

        self.color("white")
        self.goto(x=0, y=300)
        self.hideturtle()
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        return self.score

    def update_scoreboard(self):
        self.clear()
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode='w') as file:
                file.write(str(self.score))

        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)
