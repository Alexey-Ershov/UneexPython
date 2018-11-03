def parseAndSort(words):
    punct_chars = {'.', '?', '!', ':', ';', ',', '-', '(', ')', '"'}

    i = 0
    was_cut = False
    list_len = len(words)
    while i < list_len:
        if not was_cut:
            words[i] = words[i].lower()

        else:
            was_cut = False

        word = words[i]
        for index, char in enumerate(word):
            if char in punct_chars:
                if char == '.' and word[index + 1:index + 3] == '..':
                    char = '...'
                    tail_index = index + 3

                else:
                    tail_index = index + 1

                head = word[:index]
                if head:
                    words.append(head)

                tail = word[tail_index:]
                if tail:
                    words[i] = tail
                    words.append(char)
                    was_cut = True
                    break

                else:
                    words[i] = char
                    if tail_index - index == 3:
                        break

        if was_cut:
            continue

        else:
            i += 1

    words.sort()
    return words


words_from_first_string = input().split()
words_from_second_string = input().split()

print(parseAndSort(words_from_first_string) == 
        parseAndSort(words_from_second_string))
