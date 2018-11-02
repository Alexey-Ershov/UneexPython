punct_chars = {'.', '?', '!', ':', ';', ',', '-', '(', ')', '"'}

words_from_first_string = input().split()

i = 0
was_cut = False
while i < len(words_from_first_string):
    if not was_cut:
        words_from_first_string[i] = words_from_first_string[i].lower()

    else:
        was_cut = False

    word = words_from_first_string[i]
    for rindex, char in enumerate(word[-1::-1]):
        if char in punct_chars:
            index = len(word) - rindex - 1
            tail = word[index + 1:]
            if tail:
                words_from_first_string.append(tail)

            head = word[:index]
            if head:
                words_from_first_string[i] = head
                words_from_first_string.append(char)
                was_cut = True
                break

            else:
                words_from_first_string[i] = char

    if was_cut:
        continue

    else:
        i += 1
