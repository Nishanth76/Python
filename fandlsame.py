def func(list):
 f=list[0]
 l=list[-1]
 if f==l:
     result=True
 else:
     result=False
 return result
number=[]
n=int(input("Enter the length of the list:"))
for i in range(n+1):
    a=int(input(f"Enter number {i+1}:"))
    number.append(a)
result=func(number)
print(result)
