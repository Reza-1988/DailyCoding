import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

def get_mouse_click_coor(x, y):
    print(x, y)
# listen when the mouse click and call the function and pass x and y coordinate of that click location.
turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop() # this is an alternative way of keeping our screen open


