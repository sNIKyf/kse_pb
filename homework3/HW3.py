print(sum([1, 5, 78, 2, 4]))


print(min([1, 5, 78, 2, 4]))


a3=[1, 5, 78, 2, 4]
a3.reverse()
print(a3)


a4=[]
for i in a3:
    if i % 2 ==1:
        a4.append(i)
print(a4)


a5=[1, 5, 78, 2, 4]
b5=[]
for i in a5:
    i*=5
    b5.append(i)
print(b5)


a6=[1, 5, 78, 2, 4]
b6=[]
x6=4
for i in a6:
    if i > x6:
        b6.append(i)
print(b6)



a7=[1, -5, 78, 2, 4]
b7=0
c7=0
for i in a7:
    if i > 0:
        b7+=i
        c7+=1
print(b7/c7)



a8=[1, -5, 78, 2, 4]
x8=2
b8=[]
for i in a8:
    if i < x8:
        b8.append(i)
print(max(b8))



a9=[1, -5, 78, 2, 4]
y9= 2
b9=0
for i in a8:
    if i % y9==0:
        b9+=i
print(b9)



a10=[1, -5, 78, 2, 4]
b10=[]
for i in a8:
    b10.append(i**2)
print(b10)



a11=[1, -5, 78, 2, 4]
b11=[]
for i in a8:
    if i > 0:
        b11.append(i)
print(b11)



a12=["hello", "cringe", "gyatt", "horn", "horror", "hebrew"]
b12=[]
for i in a12:
    if i.startswith("he"):
        b12.append(i)
print(b12)



a13=[1, -5, 78, 2, 4]
n13=2
b13=sum(a13[0 : n13+1])
print(b13)



a14=["hello", "cringe", "gyatt", "horn", "dud", "hebrew"]
b14=[]
for i in a14:
    if i == i[::-1]:
        b14.append(i)
print(b14)




a15=[1, -5, 78, 2, 4]
x15=2
b15=[]
for i in a15:
    if i%x15 == 0:
        b15.append(True)
    else:
        b15.append(False)
print(b15)




a16=[1, -5, 78, 2, 4]
b16=[]
x16=2
y16=4
for i in a16:
    if i % x16 ==0 and i % y16 !=0:
        b16.append(i)
print(b16)



a17=[[2, 4, 5,],[6, 7, 8],[9, 10 ,3],[5, 5, 5],[2, 9, 10]]
b17=[]
for i in a17:
    for j in i:
        b17.append(j)
print(b17)




a18="ghfygher jerhgkjer tot hgfkhj dakek"
print(a18)
x18=int(input("Input the first index"))
y18=int(input("Input the second index"))
b18=a18[x18:y18]
c18=b18.upper()
print(a18[:x18]+c18+a18[y18:])



import collections
a19=[1, -5, 78, 2, 4, 5, 5, 6, 4, 0]
b19=collections.Counter(a19)
c19=sorted(a19, key=b19.get, reverse=True)
d19=sorted(c19, reverse=True)
print(d19)



a20=[1, -5, 78, 2, 4, 5, 5, 6, 4, 0]
b20=[5, 10, 98, -20, -3, 0, 2, 9, 2, -2]
c20=[]
if sum(a20) < sum(b20) and len(a20)==len(b20):
    c20=a20 + b20
print(c20)



a21={"positive": [1, 2, 3, 6, 19, 20], "negative": [-3, -8, -10, -30, -2]}
b21=input("input a key")
for key, value in a21.items():
    if key == b21:
        c21=sum(value)
print(c21)




a22=[5, 10, 98, -20, -3, 0, 2, 9, 2, -2]
b22=0
for i in a22:
    if i>0:
        a22[b22]="positive"
    elif i<0:
        a22[b22]="negative"
    else:
        a22[b22]="zero"
    b22+=1
print(a22)



a23=["hello", "cringe", "gyatt", "horn", "dud", "hebrew"]
x23=4
c23=0
for i in a23:
    if len(i)>4:
        c23+=1
print(c23)




a24=["hello", "cringe", "gyatt", "horn", "dud", "hebrew"]
b24=["google", "zero", "mark", "alternate"]
c24=0
d24=[]
for i in a24:
    c24=0
    for j in b24:
        if c24==0:
            d24.append(i + j)
            c24+=1
print(d24)



a25=[5, 10, 98, -20, -3, 0, 2, 9, 2, -2]
x25=4
y25=2
c25=0
for i in a25:
    if i>x25:
        a25[c25]*=y25
    c25+=1
print(a25)



        









