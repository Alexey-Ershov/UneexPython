import virtual_turtle

robo = virtual_turtle.turtle((0, 0), 0)
start = next(robo)

for c in "flfrffrffr":
    print(*robo.send(c))
