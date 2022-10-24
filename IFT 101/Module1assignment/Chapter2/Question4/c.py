room_length = 30
room_height = 40
room_breadth = 50

window_height = 2
window_width = 3

door_height = 3
door_width = 4

wall_area = 2*(room_length+room_breadth)*room_height - 2 * \
    (window_height*window_width) - door_height*door_width

print(wall_area)
