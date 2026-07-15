number=[10,20,30,40]
print(number[0])
print(number[1])
print(number[2])
print(number[3])# -1 nu kudutha last index sa point panum

#list edit panna
number[0]=50
print(number)

#list lenth find panna
print(len(number))

#existing list la insert panna.insert use panna index kudukanum confirm
number.insert(1,70)
print(number)

#list la last la insert panna append use pannanum
number.append(80)
print(number)

# remove panna
number.remove(50)
print(number)

#dupilicate value list acept pannum
number.append(80)
print(number)

#oru value oda index find panna
number.index(30)
print(number.index(30))

# antha index sa oru variable la save panni use pannalam
ind=number.index(30)
print(ind)

#nan kudukura value list la eruka ila ya nu find panna in use panuvom it give the result in true ir false
print(40 in number)

#epo enaku antha value eruntha update pannu ila na vendam na if else use pannalam 

if(40 in number):
    ind=number.index(40)
    number[ind]=60
    print(number)
else:
    print("The number not in a list")