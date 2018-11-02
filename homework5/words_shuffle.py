punct_chars = {'.', '?', '!', ':', ';', ',', '-', '(', ')', '"'}

words_from_first_string = input().split()

i = 0
was_cut = False
list_len = len(words_from_first_string)
while i < list_len:
    if not was_cut:
        words_from_first_string[i] = words_from_first_string[i].lower()

    else:
        was_cut = False

    word = words_from_first_string[i]
    for index, char in enumerate(word):
        if char in punct_chars:
            if char == '.' and word[index + 1:index + 3] == '..':
                char = '...'
                tail_index = index + 3

            else:
                tail_index = index + 1

            head = word[:index]
            if head:
                words_from_first_string.append(head)

            tail = word[tail_index:]
            if tail:
                words_from_first_string[i] = tail
                words_from_first_string.append(char)
                was_cut = True
                break

            else:
                words_from_first_string[i] = char
                if tail_index - index == 3:
                    break

    if was_cut:
        continue

    else:
        i += 1

print(words_from_first_string)
