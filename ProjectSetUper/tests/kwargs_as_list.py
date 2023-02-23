def kwarg_er(**kwargs):
    content = None
    if kwargs:
        content = kwargs.values()
        a, b = content
        print("Content got")
    else:
        print("No value given")


kwarg_er(a=2, b=2)
