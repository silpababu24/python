veg=("onion","potatto","carrot","tomato","beetroot","cabbage")
print(veg)
print(len(veg))
print(type(veg))
print(veg[1])
print(veg[:3])
print(veg[1:4])
print(veg[3:6])
ABC=list(veg)
print(type(ABC))
ABC[3]="pappaya"
print(ABC)
x=tuple(ABC)
print(x)


fruits=("apple","orange","grapes","orange")
print(type(fruits))
x=list(fruits)
x.insert(2,"banana")
print(x)
x.insert(0,"banana")
print(x)
x.append("carrot")
print(x)
x.remove("grapes")
print(x)
x.pop(2)
print(x)

v=("onion","carrot","potattp")
(green,black,red)=v
print(green)
print(black)
print(red)


z=("morning","evening","noon","night","morning","morning")
print(z)
print(type(z))
x=list(z)
print(type(x))
print(z[-4])
a=z.count("morning")
print(a)


z=[(10,20,30),(20,40,50)]
s=[(10,20,80),(20,40,80)]

print(z)
for i in range (len(z)):
    new=list(z[i])
    new[-2] = 80
    z[i]= tuple(new)
print(z)

L1=(1,2,3,4,9)
L2=(6,7,8)
a=list(L1)
print(type(a))
b=list(L2)
print(type(b))

a[3]=6
print(a)
a[4]=7
print(a)

L3=(1,2,3,6,7,)
y=list(L3)
print(type(y))
y.append(4)
print(y)

y.append(9)
print(y)

L3=tuple(y)
print(type(L3))
print(L3)



n=[(10,20,40),(40,50,60),(70,80,90)]
m=[(10,20,100),(40,50,100),(70,80,100)]


print(n)
for i in range (len(n)):
    new=list(n[i])
    new[2] = 100
    n[i]= tuple(new)
print(n)