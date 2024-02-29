""" task 3 
Write a Python program to get a string which is n 
(non-negative integer) copies of a given string.
 """
def repeat_string(s, n):
    return ((s+ " ") * n)
input_string = input("Enter the string: ")

copies = int(input("Enter the number of copies: "))

result = repeat_string(input_string, copies)
if copies>0 :
    print("Result:", result)
else:
    print("Enter number of copies positive")




