from turtle import *
def square(x, y, width):
    """Square at position (x, y) that has a width of width. """

    penup()
    goto(x, y)
    pendown()
    setheading(0) # heading 0 is right, heading 90 is up.
    for i in range(4): # range(4) will yield 0, 1, 2, 3
        forward(width)
        left(90)

def  rectangle(x, y, width, height):
    penup()
    goto(x, y)
    pendown()
    setheading(0)  # heading 0 is right, heading 90 is up.
    for i in range(2):  
        forward(width)
        left(90)
        forward(height)
        left(90)

def  polygon(x, y, sides, length):
    penup()
    goto(x, y)
    pendown()
    setheading(0)
    for i in range(sides):
        forward(length)
        right(360/sides)


def row_Sq(x, y, count, width):
    penup()
    goto(x, y)
    pendown()
    setheading(0)
    for i in range(count):
        for i in range(4):
            forward(width)
            left(90)
        forward(width)

def main():
    """ Tests """
    while True:
        try:
            show=int(input("please choose the function number:\n1-square\n2-rectangle\n3-polygon\n4-row_Sq\n>>>"))
            if show>=1 and show<=4:
                break

        except:
            print("Try agin\n")

    if show ==1:    #for square
        square(-100,150, 100)
        square(50, 20, 100)
        Screen().exitonclick()
        print("\n(((Done☺)))")

    if show ==2:    #for rectangle
        rectangle(30, -50, 100, 200)
        rectangle(-100, -50, 100, 200)
        Screen().exitonclick()
        print("\n(((Done☺)))")

    if show==3:     #for polygon
        polygon(-100, 100, 6, 60)
        polygon(100,100, 5, 60)
        Screen().exitonclick()
        print("\n(((Done☺)))")

    if show ==4:    #for row_Sq
        row_Sq(-100, 20, 3, 75)
        row_Sq(-100, -70, 4, 75)
        Screen().exitonclick()
        print("\n(((Done☺)))")

if __name__ == "__main__":
    main()
