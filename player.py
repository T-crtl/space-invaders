from turtle import Turtle
from fire import Fire
import time

class Player():
    def __init__(self):
        self.head = Turtle()
        self.body_complete = []
        self.create_player()
        self.healt = 3
        self.fires = []
        self.last_shot_time = 0 

    def create_player(self):
        # Crear la cabeza
        self.head = Turtle(shape="square")
        self.head.speed("fastest")
        self.head.color("white")
        self.head.penup()
        self.head.setheading(90)
        self.body_complete.append(self.head)
        self.head.goto(0, -300)

        # Crear el cuerpo
        body_part = Turtle(shape="square")
        body_part.speed("fastest")
        body_part.color("white")
        body_part.penup()
        body_part.shapesize(stretch_len=3, stretch_wid=1)
        body_part.goto(self.head.xcor(), self.head.ycor() - 15)
        self.body_complete.append(body_part)

    def move_l(self):
        # Mueve todas las partes del cuerpo a la izquierda
        new_x = self.body_complete[0].xcor() - 20
        self.body_complete[0].goto(new_x, self.body_complete[0].ycor())
        self.body_complete[1].goto(new_x, self.body_complete[1].ycor())

    def move_r(self):
        new_x = self.body_complete[0].xcor() + 20
        self.body_complete[0].goto(new_x, self.body_complete[0].ycor())
        self.body_complete[1].goto(new_x, self.body_complete[1].ycor())
    
    def fire_on(self):
        # Obtener el tiempo actual
        current_time = time.time()
        # Comprobar si ha pasado suficiente tiempo desde el último disparo
        if current_time - self.last_shot_time > 0.5:  # 0.5 segundos de espera
            new_fire = Fire(self.body_complete[0].position())
            self.fires.append(new_fire)
            self.last_shot_time = current_time  # Actualizar el tiempo del último disparo

    def update_fire(self):
        for fire in self.fires:
            fire.move()
        self.fires = [fire for fire in self.fires if fire.ycor() < 350]
    
    def impact(self):
        self.healt -= 1
        print(self.healt)