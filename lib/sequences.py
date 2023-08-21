#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_list = []
    #do not do anything if length is less than 0
    if length > 0:
    #if length is any value greater than 0, append 0 => [0]
        fibonacci_list.append(0)
    if length >= 2:
    #if length is greater than two, append 1, => [0,1]
        fibonacci_list.append(1)
        #iterate through all numbers starting at two ending at length
        #append the sum of the last number + the second to last number
        for num in range(2, length):
            fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])

    print(fibonacci_list)
        
