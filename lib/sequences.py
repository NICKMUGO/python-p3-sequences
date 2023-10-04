#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        return print([])
    elif length == 1:
        return print([0])
    elif length == 2:
        return print([0, 1])
    else:
        fibonacci_sequence = [0, 1]
        while len(fibonacci_sequence) < length:
            next_num = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_num)
        return print(fibonacci_sequence)
print_fibonacci(9)
