a=input("Введіть число:")
if int(a)%2==0:
  print("Парне")
else:
  print("Непарне")

a=float(input("Введіть середній бал:"))
if a>=90:
  print("Відмінник")
elif a<=89 and a>=75:
  print("Молодець")
else:
  print("Старайся більше")

a=0
for i in range(10, 101, 5):
  a=i+i*0.2
  print(f"Ціна без ПДВ: {i} грн -> з ПДВ: {a} грн")

print("Введіть три різних числа")
a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
  print(a)
elif b>a and b>c:
  print(b)
elif c>b and c>a:
  print(c)
else:
  print("Ви ввели не різні числа")

a=1000
b=0
while a<5000:
  a+=300
  b+=1
  print(f"Місяць {b}, накопичено {a}")

a=int(input("Введіть рік:"))
if (a%4==0 and a%100!=0) or a%400==0:
  print("Високосний")
else:
  print("Звичайний рік")

for i in range(1, 21):
  if i%4==0:
    continue
  else:
    print(i)

a=10000
b=0
m=0
while a>b:
  a+=a*0.02
  b+=1200
  m+=1
print(m)

sum=0
while True:
  a=float(input("Введіть ваш місячний дохід або '0' для виходу:"))
  if a==0:
    break
  elif a<0:
    print("Дохід не може бути відʼємним")
    continue
  else:
    sum+=a
    print(f"Ваш дохід збережено:{sum}")
    continue
  break