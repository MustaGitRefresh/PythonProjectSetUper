class A:
    def __init__(self, x):
        print(x)
        self.printer(x)

    @staticmethod
    def printer(y):
        print(y)


class B(A):
    def __init__(self, path, name):
        path = path
        name = name
        super(B, self).printer(name)
        super(B, self).__init__(name)


a = B(None, 'Rahul')
