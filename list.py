
veg=["carrot","beetroot","onion","potatto"]
print(veg)
print(len(veg))
print(type(veg))
print(veg[2])
print(veg[-1])
print(veg[1:2])
print(veg[3:])
print(veg[:3])

veg[3]="beetroot"
print(veg)
veg[:2]=["carrot"]
print(veg)

veg.insert(1,"onion")
print(veg)

veg.append("cabbage")
print(veg)

fruits=["apple","orange","grapes"]
veg.extend(fruits)
print(veg)

veg.remove("onion")
print(veg)

veg.pop(2)
print(veg)

veg.clear()
print(veg)


           


