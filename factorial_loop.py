#Creating a function that calculates the factorial of a number using for loop

def factorial_loop(n):
    result = 1 #Start with 1

    for i in range(1, n + 1):
        result *= i# Multiply result by each number from 1 to n
        return result # return the factorial value

test1=3
print(f"Factorial of the number {test1} is {factorial_loop(test1)}")

test2=10
print(f"Factorial of the number {test2} is {factorial_loop(test2)}")