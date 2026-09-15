###in the name of god

print('We want to draw a equalitera triangle shape useing for loop with some decors.')

import turtle

def make_screen():
    screen = turtle.Screen()
    screen.bgcolor('red')
    screen.title('draw a equalitera triangle shape')
    return screen

def make_turtle():
    amirabas = turtle.Turtle()
    amirabas.fillcolor('gold')
    amirabas.pencolor('green')
    amirabas.shape('turtle')
    amirabas.speed('fastest')
    #amirabas.pensize(5)
    return amirabas

def draw_regular_shape(sides, angle, tr , fdsize):
    # Draw equalilera triangle shape
    for _ in range(sides):
        # Tell amirabas to forward 100px
        tr.forward(fdsize)

        # Tell amirabas to turn left 
        tr.left(angle)


    for _ in range(sides):
        # Tell amirabas to forward 100px
        tr.forward(fdsize)

        # Tell smirabas to turn right
        tr.right(angle)
        
    # Tell amirabas to turn left 
    tr.left(angle)

    #Mor than line
    for _ in range(sides):
        # Tell amirabas to forward 100px
        tr.forward(fdsize)

        # Tell amirabas to turn left 
        tr.left(angle)

    for _ in range(sides):
        # Tell amirabas to forward 100px
        tr.forward(fdsize)

        # Tell smirabas to turn right
        tr.right(angle)

    tr.left(angle)
    tr.left(angle)
        

def main():
    wn = make_screen()
    tess = make_turtle()
    for  sides in range(3 , 20):
        draw_regular_shape(sides=sides , angle=360/sides , tr=tess , fdsize=50)
    # wait for the user to close the window
    wn.mainloop()




### Driver Code ###

main()
