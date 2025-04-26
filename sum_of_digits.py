#Creating a function that sums up the digits in a number

def sum_of_digits(n):
    total = 0 #initialize sum to 0
    while n>0:

        digit = n % 10 #to get the last digit
        total += n%10 #Add it to total
        n = n//10 #remove the last digit
        return total # return the total sum of digits

    test1= 135
    print(f"Sum of digits of {test1} is {sum_of_digits(test1)}")

    test2=55
    print(f"Sum of digits of {test2} is {sum_of_digits(test2)}")