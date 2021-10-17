import time


# Decorator function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + ' function took ' + str((end - start) * 1000) + ' mil sec')
        return result

    return wrapper


@timeit
def square(num):
    lst = []
    for i in num:
        lst.append(i * i)
    # The logic of the program is still intact and,
    # we can still calculate the time it took to run the whole operation.


@timeit
def cube(num):
    lst = []
    for i in num:
        lst.append(i * i * i)


if __name__ == '__main__':
    a = range(100000)
    square(a)
    cube(a)
