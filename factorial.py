# to print factorial of a number

a = int(input("Enter a number"))
fact=1
if a <0:
   print("factorial does not exist")
elif a == 0:
   print("factorial is 1")
else:
   for i in range (1, a+1):
      fact = fact*i
   print(fact)
