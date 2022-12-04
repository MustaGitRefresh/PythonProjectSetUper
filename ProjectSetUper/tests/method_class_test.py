# from module_method_test_class import *
#
#
# class Sub:
#     def __init__(self):
#         self.first_one = One.first
#         self.printer()
#
#     def printer(self):
#         print("Sub")
#         self.first_one()
#
#
# sub = Sub()


class ClassAssigner:
    def __init__(self):
        self.name = []
        self.assigner()
        self.val_s = self.value_extracter()

    def assigner(self):
        self.name.append("ME First")

    def value_extracter(self):
        val = self.name
        return val

    def printer(self):
        print(self.val_s)


ca = ClassAssigner()
ca.printer()
