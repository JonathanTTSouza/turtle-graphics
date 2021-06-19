import colorgram

colors = colorgram.extract('Addictive---detail-of-Dam-007.jpg', 20)
colors_list = []

for color in colors:
    red = color.rgb.r
    green = color.rgb.g
    blue = color.rgb.b

    colors_list.append((red, green, blue))

print(colors_list)
