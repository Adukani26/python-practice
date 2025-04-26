#Creating a function that calculates the factorial of a number using if else

def factorial_recursive(n):
    if n==1 or n==0: #factorial of 0 or 1 is 1
        return 1
    else:
        return n*factorial_recursive(n-1)

test1=3
print(f"Factorial of the number {test1} is {factorial_recursive(test1)}")

test2=9
print(f"Factorial of the number {test2} is {factorial_recursive(test2)}")