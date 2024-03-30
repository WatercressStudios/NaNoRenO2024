init python:
    station_info = [
        (0.8321, 0.7671),
        (0.7556, 0.7670),
        (0.6942, 0.7705)
    ]
    map_size = (6400., 4267.)
    map_pos = station_info[0]

transform map_point_transform(pos=(0.5, 0.5)):
    anchor (0.5, 0.5) pos (0.5 + (pos[0] - map_pos[0]) * map_size[0] / config.screen_width, 0.5 + (pos[1] - map_pos[1])  * map_size[1] / config.screen_height)

transform map_transform(pos=(0.5, 0.5)):
    anchor (0.5, 0.5) pos (-pos[0] + 0.25, -pos[1] + 0.25)

screen map():
    add "map_base"
    add "map_blank" at map_transform(map_pos)
    add "map_route" at map_transform(map_pos)

    for pos in station_info:
        add "map_point_line1" at map_point_transform(pos)
