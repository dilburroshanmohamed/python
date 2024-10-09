n1=int(input("enter 1st number"))
n2=int(input("enter 2nd number"))
n3=int(input("enter 3rd number"))
if(n1<n3)&(n2<n3):
 print("largest number is :",n3)
elif(n1<n2)&(n3<n2):
 print("largest number is :",n2)
else:
  print("largest number is :",n1)
