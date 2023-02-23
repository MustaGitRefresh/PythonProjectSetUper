from three import Three


class One:
    def __init__(self):
        print(None)
        self.fast()
        Three().__init__()

    def fast(self):
        print(self)


one = One()
