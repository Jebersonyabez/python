name=["jeberson","yabez","steffi","gracia","prasanna"]

#print with index
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

# insert
name.insert(1,"jebez")
print(name)

#append
name.append("charlin")
print(name)

#length
print(len(name))

#edit
name[-1]="Edwin"
print(name)

#remove 
name.remove("Edwin")
print(name)

#find index of a value
ind=name.index("gracia")
print(ind)

#check the given value is in list or not
print("jeberson" in name)

if("steffi" in name ):
    inde=name.index("steffi")
    name[inde]="mental"
    print(name)
else:
    print("not present in list")
