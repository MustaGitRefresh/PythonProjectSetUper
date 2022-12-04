from module_method_test_class import *


class Sub:
    def __init__(self):
        self.first_one = One.first
        self.printer()

    def printer(self):
        print("Sub")
        self.first_one()


sub = Sub()
