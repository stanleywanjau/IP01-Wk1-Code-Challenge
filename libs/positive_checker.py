#a function that takes three number
def positive_number(a,b,c):
  #the if function checks whether a is positive it the check if any of b or c is also positive
   if a > 0:
        return b > 0 or c > 0
        
   elif b > 0:
        return c > 0
   else:
        return False

print(positive_number(1,0,0))
print(positive_number(1,-4,-4))
print(positive_number(-1,-9,4))
print(positive_number(-25,100,12))
print(positive_number(23,-4,5))
print(positive_number(3,5,-6))
print(positive_number(-3,-5,-6))
