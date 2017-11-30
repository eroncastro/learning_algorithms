def get_fib(position):
    if position == 0:
        return 0

    return (1 if position == 1 or position == 2
            else get_fib(position-1) + get_fib(position-2))