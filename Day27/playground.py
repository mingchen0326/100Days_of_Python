def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


if __name__ == "__main__":
    calculate(5, add=3, multiply=5)


