import colorgram

hirst_list_color = []

colors = colorgram.extract('hirst_painting.jpg', 30)


for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    hirst_list_color.append(new_color)

print(hirst_list_color)
