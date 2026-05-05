#List
string_list=[1,"Priya","Hari",5,6,]

print(len(string_list))

string_list.append("Leya")

string_list.remove("Leya")
print(string_list)

print(string_list.count("Hari"))
print(string_list.index("Hari"))

for i in range(0,10,2):
    print ("Hello")
    print(i)


#Dictionary
    people={
        "name":"Priya",
        "age" :38,
        "place":"Edison"
    }

print(people["name"])

people["license"]=True
print(people)  

del people["license"]

print(people)
