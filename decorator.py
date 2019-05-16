def decorator_function(func_to_decorate):
    def wrap_func(*args, **kwargs):
        print("Arguments: ", args)
        print("Arguments: ", kwargs)
        func_to_decorate(*args, **kwargs)
    return wrap_func


@decorator_function
def sum_(a, b, c = 0):
    print("sum: ", a + b + c)


if __name__ == '__main__':
    sum_(2, 3, c=5)
