def characterLocation(commands):
    # 関数を完成させてください
    direction = {
        "N":{"x":0,"y":1},
        "E":{"x":1,"y":0},
        "W":{"x":-1,"y":0},
        "S":{"x":0,"y":-1}
    }

    player_position = [0,0]

    for command in commands:
        if(command == "N" or command == "E" or command == "W" or command == "S"):
            player_position[0] += direction[command]["x"]
            player_position[1] += direction[command]["y"]

    return player_position