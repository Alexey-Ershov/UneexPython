class vector:
    def __init__(self, seq):
        self.list_data = list(seq)

    def __getitem__(self, index):
        return self.list_data[index]

    def __len__(self):
        return len(self.list_data)

    def __add__(self, seq):
        return vector(self[i] + seq[i] for i in range(len(seq)))

    def __radd__(self, seq):
        return vector(self[i] + seq[i] for i in range(len(seq)))

    def __str__(self):
        string_repr = ""
        for item in self.list_data:
            string_repr += str(item) + ':'

        return string_repr[:-1]
