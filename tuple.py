# create panna
t=(200,300,400,500,600)
#Tuple la print panna
print(t)
#Tuple la index vachi acess panna
print(t[0])

# Tuple la for loop la acess panna lam because tuple la index acess undu
for n in t:
    print(n)

#Tuple la direct ta edit panna mudiyathu so first change the tuple into list then do the edit operation then again change to tuple

lst=list(t)
print(lst)
lst.append(1000)
print(lst)
t=tuple(lst)
print(t)

