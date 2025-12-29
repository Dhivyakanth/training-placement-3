a=int(input("Enter number: "))
b=a
c=len(str(a))
s=sum(int(d)**c for d in str(n))
if s==a:
    print(f"{a} is armstrong")
else:
    print(f"{a} is not armstrong")
