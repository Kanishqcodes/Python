# Write a program to check if a number is a single digit number, double digit number, .... up to five digit number

num=int(input("Enter your number:"))

if num >= 0 and num <= 9:
    print("it is a single digit number")
elif num >= 10 and num <= 99:
    print("it is a double digit number")
elif num >= 100 and num <= 999:
    print("it is a triple digit number")
elif num >= 1000 and num <= 9999:
    print("it is a four digit number")
elif num >= 10000 and num <= 99999:
    print("it is a five digit number")
else:
    print("Its not a number that meets the question needs \n pls check the number and try again")