words = []
numbers = []
line = input()

while line:
    words += line.split()
    line = input()

for word in words:
    if word[0] == '-' and word[1:].isdecimal():
        numbers.append(int(word))

    elif word.isdecimal():
        numbers.append(int(word))

numbers.sort()
print(numbers[-1])
