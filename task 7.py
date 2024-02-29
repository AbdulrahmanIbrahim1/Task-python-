#task 7 : Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
from numpy import *
num1 = float(input("Enter number 1 = "))
num2 = float(input("Enter number 2 = "))
num3 = float(input("Enter number 3 = "))

if num1 == num2 or num1==num3 or num2==num3:
  sum=0
  print("sum = " ,sum)
else:
  sum = sum([num1,num2,num3])
  print("sum = ",sum)