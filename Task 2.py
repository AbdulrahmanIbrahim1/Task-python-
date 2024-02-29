""" Task 2 
Write a Python program to calculate the sum of three given numbers,
if the values are equal then return thrice of their sum."""
from numpy import *
num1 = float(input("Enter number 1 = "))
num2 = float(input("Enter number 2 = "))
num3 = float(input("Enter number 3 = "))
sum = sum([num1 , num2 , num3]) 
if(num1 == num2 == num3 ):
    print(3*sum)
else:
    print(sum)
