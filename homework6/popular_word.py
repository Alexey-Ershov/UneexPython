class PopularWord:
    def __init__(self):
        self.__popular_words = set()
        self.__popularity_count = 0
        self.__word_to_count = {}

        input_words = input().split()
        while input_words:
            self.__choose_popular(input_words)
            input_words = input().split()

        if len(self.__popular_words) == 1:
            print(self.__popular_words.pop())

        else:
            print("---")

    def __choose_popular(self, input_words):
        for word in input_words:
            if self.__word_to_count.get(word) is None:
                self.__word_to_count[word] = 1

            else:
                self.__word_to_count[word] += 1

            cur_count = self.__word_to_count[word]
            
            if cur_count > self.__popularity_count:
                self.__popularity_count = cur_count
                self.__popular_words = {word}

            elif cur_count == self.__popularity_count:
                self.__popular_words.add(word)


PopularWord()
