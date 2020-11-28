def new_func():
    def new_func_2():
        print("New func 2")
    return new_func_2()
new_func()
