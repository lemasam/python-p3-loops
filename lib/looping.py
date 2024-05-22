#!/usr/bin/env python3

def happy_new_year():
    for i in range (10,0,-1):
        print(i)
        print("Happy New Year!")
    pass

def square_integers(int_list):
    return [num ** 2 for num in int_list]
    
list1 = [1, 2, 3, 4, 5]
list2 = [-1, -2, -3, -4, -5]

result1 = square_integers(list1)
result2 = square_integers(list2)

print("Squared integers for list1:", result1)
print("Squared integers for list2:", result2)
pass

def fizzbuzz():
    for i in range (1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    pass
