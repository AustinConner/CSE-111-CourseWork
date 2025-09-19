"""
Course: CSE 111
Lesson Week: 04
File: turtle-example.py
Author: Brother Comeau
Purpose: Turtle drawing examples using functions

https://docs.racket-lang.org/racket_turtle/racket_turtle_examples_with_recursion.html

Turtle functions:
- up()                  move pen up
- goto(x, y)            move pen to (x, y)
- down()                move pen down

- fd(width)             forward movement
- bk(width)             backward movement
- right(90)             turn right
- left(90)              turn left

- fillcolor(color)      fill color
- pencolor(color)       pen color
- begin_fill()          begin fill color area
- end_fill()            finish fill color area

See "star angles.jpg"

TODO
- create function to draw a square
- create function to draw a triangle
- create function to draw a ploygon

"""

import turtle

def main():
    turtle.setup(800, 800)

    tr = turtle.Turtle()
    # fred.speed(0)

    # fred.fd(100)
    # fred.left(90)
    # fred.fd(100)
    # fred.left(90)
    # fred.fd(100)
    # fred.left(90)
    # fred.fd(100)

    scale = 300
    height = 1 * scale
    width = 1.9 * scale

    flagbox(tr, width, height)
    stripes(tr, width, height)
    starbox(tr, scale)
    stars(tr, scale)

    turtle.done()

## Set the flag size as a constant. Find ratio that will find out the size? https://usflags.design/usa/#:~:text=U.S.%20Executive%20Order%2010834%20specifies,the%20length%20of%20the%20fly.
### Flag size ratios
height_ratio = 1
width_ratio = 1.9

# draw stripes
strip_ratio = 0.0769

# draw star border box
star_box_height_ratio = 0.5385
star_box_width_ratio = 0.76

# Flag scale
flag_scale = 5


"""
Fred starts at 0,0

flag scale is X

      x
      x
y y y x y y y
      x
      x

calculate the width of the flag. Divide it by 2. we can center the flag like that.

calc the height of the flag. Div by 2. Centers the flag.

"""

def flagbox(tr, width, height):

    tr.penup()

    bottom_left_x = -width / 2
    bottom_left_y = -height / 2
    bottom_right_x = width / 2
    bottom_right_y = -height / 2
    top_left_x = -width / 2
    top_left_y = height / 2
    top_right_x = width / 2
    top_right_y = height / 2

    tr.goto(bottom_left_x, bottom_left_y)
    tr.pendown()
    tr.goto(bottom_right_x, bottom_right_y)
    tr.goto(top_right_x, top_right_y)
    tr.goto(top_left_x, top_left_y)
    tr.goto(bottom_left_x, bottom_left_y)
    tr.penup()

def stripes(tr, width, height):
    red_stripe = "#bb133e"
    white_stripe = "#ffffff"
    tr.speed(3000)
    stripe_ratio = 0.0769 * height
    stripe_count = 1
    for _ in range(13):
        # make stripe
        if stripe_count % 2 == 0:
            tr.color(white_stripe)
        else:
            tr.color(red_stripe)
        tr.begin_fill()
        tr.fd(width)
        tr.left(90)
        tr.fd(stripe_ratio)
        tr.left(90)
        tr.fd(width)
        tr.left(90)
        tr.fd(stripe_ratio)
            # tr.left(180)
            # distance += strip_ratio
        tr.end_fill()

        tr.left(180)
        tr.fd(stripe_ratio)
        tr.right(90)
        stripe_count += 1

def starbox(tr, scale):
    tr.speed(300)
    blue_stripe = "blue"
    height = 0.5385 * scale
    width = 0.76 * scale

    tr.color(blue_stripe)
    tr.begin_fill()
    tr.fd(width)
    tr.right(90)
    tr.fd(height)
    tr.right(90)
    tr.fd(width)
    tr.right(90)
    tr.fd(height)
    tr.right(90)
    tr.end_fill()

def stars(tr, scale):
    tr.speed(1)
    # size = 0.0616 * scale
    margin = scale * 0.054
    gap = 0.063 * scale
    print(margin)
    tr.fd(margin)
    tr.right(90)
    tr.fd(gap)
    make_star(tr, scale)
    for _ in range(5):
        tr.fd(margin * 2)
        make_star(tr, scale)


    tr.left(90)
    tr.fd(gap)
    tr.left(90)
    tr.fd(gap*5)

def make_star(tr, scale):
    tr.setheading(0)
    tr.speed(100)
    size = (0.0616 * scale)
    tr.color("white")
    tr.begin_fill()
    tr.pendown()
    angle = 144
    for _ in range(6):
        tr.forward(size) 
        tr.right(angle)
    tr.end_fill()
    tr.penup()  


# main()

def test():
    turtle.setup(800, 800)

    tr = turtle.Turtle()
    # fred.speed(0)

    # fred.fd(100)
    # fred.left(90)
    # fred.fd(100)
    # fred.left(90)
    # fred.fd(100)
    # fred.left(90)
    # fred.fd(100)

    scale = 200
    height = 1 * scale
    width = 1.9 * scale

    # flagbox(tr, width, height)
    # stripes(tr, width, height)
    # starbox(tr, scale)
    # stars(tr, scale)



    # --- Drawing Parameters ---
    star_size = 200  # Length of each side of the star
    angle = 144      # Angle for a 5-pointed star (360 / 5 * 2)

    # --- Drawing Logic ---
    # Move turtle to a starting position (optional, to center the star)
    # tr.penup()
    # tr.goto(-star_size / 2, star_size / 4) # Adjust starting position
    # tr.pendown()

    # Begin filling the star shape
    tr.begin_fill()

    # Loop to draw the 5 points of the star
    for _ in range(5):
        tr.forward(star_size)  # Move forward by the star_size
        tr.right(angle)      
    turtle.done()

main()