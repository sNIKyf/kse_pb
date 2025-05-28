a1="Hello, Python World!"
print(a1)


a2=int(input("Input a whole number"))
b2=int(input("Input a whole number"))
print(a2+b2, a2-b2, a2*b2, a2/b2)


a3=input("Input a string")
b3=input("Input a string")
c3=a3+" "+b3
print(c3, len(c3))


a4=int(input("Input a whole number"))
if a4%2==0:
    print("Even")
else:
    print("Odd")


for i in range(1, 11):
    print(i)


num=float(input("Input a number"))
if num>0:
    print("Positive")
elif num<0:
    print("Negative")
else:
    print("Zero")


for i in range(2, 11, 2):
    print(i)


n=int(input("Input a whole number"))
a8=0
for i in range(1, n+1):
    a8+=i
print(a8)


for i in range(10, 0, -1):
    print(i)


for i in range(1, 11):
    if i==5:
        continue
    elif i==7:
        break
    else:
        print(i)

