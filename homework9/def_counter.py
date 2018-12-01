from collections import Counter

class DefCounter(Counter):
    def __init__(self, *args, **kwds):
        self._missing = kwds.pop("missing", -1)
        super().__init__(*args, **kwds)

    def __missing__(self, key):
        return self._missing
