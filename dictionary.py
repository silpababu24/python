car={
    "brand":"maruthi",
    "model":"mustang",
    "yr":1997,
}

print(car)
print(car["yr"])
print(len(car))

thisdict=dict(batch="A" ,strength=52)
print(thisdict)

x=car.get("model")
print(x)

y=car.keys()
print(y)

z=car.values()
print(z)

a=car.items()
print(a)

car["yr"]="1887"
print(car)

car.update({"yr":2000})
print(car)

car["price"]=3000000
print(car)

car.pop("yr")
print(car)

car.popitem()
print(car)

del car["model"]
print(car)

car.clear()
print(car)

student={"name":"anu", "age":24}
stud=student.copy()
print(stud)

for x in student:
    print(x)

for x in student.values():
    print(x)
    
for x,y in student.items():
    print(x,y)


family={
    "child":{"name":"anu",
             "age":10
             },
     "child1":{"name":"vinu",
               "age":15
     },
            
      "child2":{"name":"manu",
                "age":13}   
     }

print(family)


dict={0:10,
      1:20
      }
dict.update({2:30})
print(dict)



dic={
    "name":"anu",
    "height":"150",
    "weight":"50"
 }     



for x,y in dic.items():
   print(x,y)




d1={1: 10, 2: 20}
d2={3:20,  5:20}
d3={6:20,  9:20}
d4={}
for x in (d1,d2,d3):
    d4.update(x)
print(d4)    





