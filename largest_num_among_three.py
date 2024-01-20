while True:
    print("Enter a value:",end="")
    a=int(input())
    print("Enter b value:",end="")
    b=int(input())
    print("Enter c value:",end="")
    c=int(input())
    if a>=b and a>=c:
       print("The Largest number is a:",a)
    elif b>=a and b>=c:
        print("The Largest number is b:",b)
    else:
        print("The Largest number is c:",c)
    print(" ") 
