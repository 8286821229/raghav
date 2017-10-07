num=int(input("enter a no"))
temp=num
sum=0
while(num>0):
    rem=num%10
    sum=sum+(rem**3)
    num=num//10
if sum==temp:
    print("armstrong no")
else:
    print("not an armstrong no")
    
