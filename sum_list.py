#Creating a function that sums all the numbers in a list

def sum_list(numbers):

#initialize total to 0
    sum = 0
    for num in numbers:
        sum += num# Add each number to the sum


    return sum

    test1=[1,2,3,4,5]
    print("sum:", sum_list(test1))

    test2=[10,20,30,40,50]
    print("sum:", sum_list(test2))

    test3=[-5,10,13]
    print("sum:", sum_list(test3))