list=[]
len=int(input("enter the length of the list :"))
print("enter the number to the list")
for i in range(len):
 temp=int(input())
 if temp>=100:
    list.append('over')
 else:
    list.append(i)
print("list",list)
