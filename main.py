from turtle import Screen
from player import Player
from alien import Alien
from score import Score
import time

screen = Screen()
screen.setup(width=500, height=700)
screen.bgcolor("black")
screen.title("Space Invaders")
screen.tracer(0)

player = Player()
alien = Alien()
score = Score()

screen.listen()
screen.onkey(player.move_l, "Left")
screen.onkey(player.move_r, "Right")
screen.onkey(player.fire_on, "space")
#screen.onkey(alien.fire_on, "w")

while 1:
    screen.update()
    time.sleep(0.1)
    player.update_fire()
    alien.move_aliens()
    alien.fire_on()
    alien.update_fire()

    #print(player.head.xcor())

    for each in alien.aliens:
        for i in player.fires:
            if each.distance(i) < 15:
                each.clear()            # Borra la imagen del alien
                each.hideturtle()       # Esconde la tortuga para que no se muestre más
                alien.aliens.remove(each)  # Elimina el alien de la lista
                i.clear()               # Borra la imagen del disparo
                i.hideturtle()          # Esconde la tortuga del disparo
                player.fires.remove(i)  # Elimina el disparo de la lista
                score.update_score()
    
    for each in alien.fires:
        if player.body_complete[0].distance(each) < 15 or player.body_complete[1].distance(each) < 30:
            player.impact()
            each.hideturtle()
            alien.fires.remove(each)
    


screen.exitonclick()