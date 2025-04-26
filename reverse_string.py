#Creating a function that reverses the order of letters in a word

def reverse_string(s):
    reversed_str ='' #Start with an empty string

    for char in s:

        reversed_str =char+reversed_str # Add current character before previous ones

        return reversed_str #return the reverse string

test1= "hello"
print(f"Reversed string of {test1} is {reverse_string(test1)}")

test2= "World"
print(f"Reversed string of {test2} is {reverse_string(test2)}")