from turtle import Turtle, Screen
from fire import Fire
import time
import random
    
screen = Screen()

class Alien(Turtle):
    def __init__(self):
        super().__init__()
        self.new_y = 300
        self.new_x = -230
        self.aliens = []
        self.create_all()
        self.movement_direction = 1
        self.speed = 0.5
        self.move_distance = 2
        self.fires = []
        self.last_shot_time = 0 

    def create_all(self):
        for i in range(7):
            for j in range(10):    
                new_alien = self.create_alien()
                self.aliens.append(new_alien)
                self.new_x += 40
            self.new_x = -230 
            self.new_y -= 40
    
    def create_alien(self):
        alien = Turtle(shape="turtle")
        alien.setheading(275)
        alien.color("green")
        alien.penup()
        alien.goto(self.new_x, self.new_y)
        return alien
    
    def move_aliens(self):
        hit_edge = False
        for alien in self.aliens:
            new_x = alien.xcor() + (self.move_distance * self.movement_direction)
            alien.goto(new_x, alien.ycor())

            # Detectar si algún alien toca el borde de la pantalla
            if new_x <= -240 or new_x >= 230:  # 380 es el borde izquierdo/derecho para una pantalla de 800px
                hit_edge = True

        if hit_edge:
            self.movement_direction *= -1  # Cambia la dirección
            self.move_down()


    def move_down(self):
        for alien in self.aliens:
            new_y = alien.ycor() - 20  # Baja los aliens 20 píxeles
            alien.goto(alien.xcor(), new_y)     

    def fire_on(self):
        # Obtener el tiempo actual
        current_time = time.time()
        # Comprobar si ha pasado suficiente tiempo desde el último disparo
        if current_time - self.last_shot_time > 2:  # 0.5 segundos de espera
            new_fire = Fire(random.choice(self.aliens).position())
            new_fire2 = Fire(random.choice(self.aliens).position())
            self.fires.append(new_fire)
            self.fires.append(new_fire2)
            self.last_shot_time = current_time  # Actualizar el tiempo del último disparo

    def update_fire(self):
        for fire in self.fires:
            fire.move_down()
        self.fires = [fire for fire in self.fires if fire.ycor() > -350] 
