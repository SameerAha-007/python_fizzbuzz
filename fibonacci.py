'''
#sum of fibonacci series
def fibonaci(n):
    if (n==0):
        return 0
    elif (n==1 or n==2):
        return 1
    else:
        return  fibonaci(n-1)+fibonaci(n - 2)
print("enter a number:",end="")
n =int(input())
print(fibonaci(n))
'''


'''
print("Enter a number:",end="")
n = int(input())
num1 = 0
num2 = 1
next_number = num2 
count = 1
print("The fibonacci series:0 ",end="")
while count <= n:
    print(next_number, end=" ")
    count += 1
    num1=num2
    num2 =next_number
    next_number = num1 + num2
print()
'''