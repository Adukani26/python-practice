#Creating a function that checks if a number is even or odd

def check_even_or_odd(num):
    if num % 2 == 0: #if the reminder is 0 when divided by, 2 its even
        return "Even"

    else:
        return "Odd"

test1=36
print(f"The number of {test1} is: {check_even_or_odd(test1)}")

test2=57
print(f"The number of {test2} is: {check_even_or_odd(test2)}")