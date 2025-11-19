#!/usr/bin/env python3
def print_fibonacci(length):
    # Handle edge cases
    if length <= 0:
        result = []
    elif length == 1:
        result = [0]
    else:
        # Your previous list-building logic goes here...
        fib_list = [0, 1]
        for i in range(2, length):
            fib_list.append(fib_list[-1] + fib_list[-2])
        result = fib_list
        
    # FIX: Use the print function to output the list as a string
    print(result) 
    
    # Returning it might still be necessary for other tests, but printing is the fix here
    return result

    pass