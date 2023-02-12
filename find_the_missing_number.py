import math

a = [1, 2, 3, 4, 6, 7, 8, 9, 10]

def find_the_missing_number():
    c = int(sum(a))
    print(c)
    
    b = int(sum(range(11)))
    print(sum(range(11)))

    missing_number = b - c
    print(f"The missing_number is {missing_number}")

find_the_missing_number()