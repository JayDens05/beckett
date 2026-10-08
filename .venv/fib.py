
def fib1(first,second):
    while first < 100000:
        storage = first
        first = first + second
        second = storage
        print(first, " ", second)

fib1(0,1)

