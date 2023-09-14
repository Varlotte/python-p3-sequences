#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_list = []
    num1 = 0
    num2= 1
    next_number= 0

    for n in range(length):
        fibonacci_list.append(next_number)
        num1 = num2
        num2 = next_number
        next_number = num1 + num2
        
    print(fibonacci_list)
    