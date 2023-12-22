


dict1={1: 10, 2: 20}
dict2={3: 10, 4: 20}
dict3={5: 10, 6: 10}
dict4={}
       

for n in (dict1,dict2,dict3):
     dict4.update(n)
print(dict4)