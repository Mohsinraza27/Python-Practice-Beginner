import cProfile

def internal_method():
    temp_var = 0
    for ind in range(10):
        temp_var += 1
    return temp_var

def external_method():
    counter = 0
    for val in range(10):
        counter += internal_method()
    print("Total iterations:", counter)
    return

cProfile.run("external_method()")