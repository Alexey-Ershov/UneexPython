def generator(number):
    yield -number
    yield str(number)
    
    if number < 0:
        number = -number
    
    yield (number % 100) // 10
