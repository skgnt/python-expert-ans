import turtle



def sikaku(tt:turtle.Turtle, x:int, y:int):
    tt.forward(x)
    tt.right(90)
    tt.forward(y)
    tt.right(90)
    tt.forward(x)
    tt.right(90)
    tt.forward(y)
    tt.right(90)



a=turtle.Turtle()

sikaku(a, 100, 100)
turtle.done()
