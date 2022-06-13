from tracemalloc import start
from turtle import Screen, Turtle
import time
import random

MOVE_DISTANCE = 20

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

starting_positions = [(0,0),(-20,0),(-40,0)]
segments = []

class Snake():
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.speed("fastest")
    
    def create_snake(self):
        for position in starting_positions:
            new_segment = Turtle("square")
            new_segment.color("White")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
            
    def move(self):
        
        
        
        for seg_num in range(len(self.segments) - 1,0,-1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)
    
        
        
    def up(self):
        if int(self.head.heading()) != 270:
            self.head.setheading(90)
            
    def down(self):
        if int(self.head.heading()) != 90:
            self.head.setheading(270)
            
    def left(self):
        if int(self.head.heading()) != 0:
            self.head.setheading(180)
            
    def right(self):
        if int(self.head.heading()) != 180:
            self.head.setheading(0)
            
    def grow(self):
        for i in range(2):
            new_segment = Turtle("square")
            new_segment.color("White")
            new_segment.penup()
            new_segment.speed('fastest')
            position = self.segments[-1].position()
            new_segment.goto(position)
            self.segments.append(new_segment)
            
    def reset(self):
        for segment in self.segments:
            segment.goto(2000,2000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        
    
    
        
        
        
            


class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('red')
        self.speed('fastest')
        random_x = random.randint(-380,380)
        random_y = random.randint(-280,280)
        self.penup()
        self.goto(random_x,random_y)
    
    def refresh(self):
        random_x = random.randint(-380,380)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)
        

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        
        with open('data.txt') as data:
            self.high_score = int(data.read())
        
        self.color('Green')
        self.hideturtle()
        self.penup()
        self.goto(0,250)
        self.write(f"Score: {self.score}   High Score: {self.high_score}", align = "center", font =('Arial', 24, 'normal'))
        
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.high_score}", align = "center", font =('Arial', 24, 'normal'))
        
    
    def reset(self):
        if self.score > self.high_score:
            with open('data.txt', mode = 'w') as data:
                data.write(str(self.score))
            self.high_score = self.score
            
        self.score = 0
        self.update_score()
        
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over!", align = "center", font =('Arial', 24, 'normal'))
    
    def increase_score(self):
        self.score += 1
        self.update_score()
        
        
    
        
    
        
        
        
    
    
        
        
        
snake = Snake()
food = Food()
score = Scoreboard()



screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

        

        
        
    
screen.update()
game_is_on = True

while game_is_on:  
    snake.move()
    time.sleep(0.06)
    screen.update()
    
    
    # Detect collision with food
    if snake.head.distance(food) < 15:
        print("nom nom nom")
        food.refresh()
        snake.grow()
        food.forward(0)
        score.increase_score()
        score.update_score()
    
    if snake.head.xcor() > 395 or snake.head.xcor() < -395 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        score.reset()
        snake.reset()
    
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()
            
    
    
        
    
    

















screen.exitonclick()


