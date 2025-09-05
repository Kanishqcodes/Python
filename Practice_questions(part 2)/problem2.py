#Write a Program to Swap two Variables

# There are two methods to swap variables

print("Method 1 :")
a=10
b=20
print("value of a before swap:", a)
print("value of b before swap:",b)

temp=a
print("value of temp:",temp)

a=b
b=temp
print("value of a after swap:", a)
print("value of b after swap:",b)

print("Method 2 :")
x=60
y=70
print("value of x before swap:", x)
print("value of y before swap:",y)

x,y=y,x
print("value of x after swap:", x)
print("value of y after swap:",y)