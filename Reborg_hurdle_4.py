def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():

    turn_left()
    move()
    turn_right() 
    move()
    turn_right()
    move()
    
def go_up():
    turn_left()
    turn_left()
    while wall_on_right() == True:
        move()
    
def go_down():
    turn_right()
    move()
    turn_right()
    while front_is_clear() is True:
        move()
    turn_left()
        
while at_goal() == False:

    while front_is_clear() is True:
        move()
    while wall_in_front() is True:
        turn_left()
        while right_is_clear() is not True:
            move()
        go_down()
    
        
    
