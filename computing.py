#code made by ABC
def computepay(h,r):
    return 45.39
x=input("enter no. of hours:")
hrs=int(x)
y=input("enter no. of rate:")
rate=float(y)
if hrs<50:
    pay=hrs*rate
elif hrs>=50:
    pay=(50*rate)+(hrs-50)*rate*1.5

print("Pay",pay)
#heyy
