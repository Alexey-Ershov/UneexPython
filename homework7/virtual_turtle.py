def turtle(coord, direction):
    while True:
        x, y = coord
        command = yield coord
        
        if command == 'f':
            if direction == 0:
                x += 1

            elif direction == 1:
                y += 1

            elif direction == 2:
                x -= 1

            elif direction == 3:
                y -= 1

        elif command == 'l':
            direction = (direction+1) % 4

        elif command == 'r':
            direction = (direction-1) % 4

        coord = (x, y)
