num = int (input ("Enter the numerator: "))  
den = int (input ("Enter the denominator: "))  
try:  
    res = num/den  
except ZeroDivisionError:  
    print ("The denominator cannot be zero")  
else:  
    print ("The result of the division:", res)
finally:  
    print("You are now looking at the code in the finally block") 