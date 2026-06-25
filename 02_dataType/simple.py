name = "ramit"
print(id(name))

name = name.upper()
print(id(name)) #string is immutable


# list................................................

list1 = [10, 20, 30, 40, 50, "ram"]
#access, modify, delete, insert

#update
list1[0] = "hari"
print(list1)

#delete
list1.pop(0)
print(list1)

list1.remove("ram") #it remove from index

#insert
list1.append(90) #insert value at the end

list1.insert(1, 90) #insert value based on the index value

print(list1)


#touple...............................................
t1 = (1, 2, 3,1) #immutable
print(type(t1))
print(t1[0])

# t1[0] = "Ramit"  error occure

# t1 = 1, 2, 3   this is also touple in touple small baracket is optiional
# t1 = (1) this is integer not toupe
#t1 = (1, ) this is touple becasue there is , after number


#dictionary..............................................

student = {
    "name": "Ram",
    "address": "kathmandu",
    "mobile": "98054"
} | {
    #merge two dictionary
}
#key must be unique but if we write duplicate key error doesnot occur 

student["name"] = "Ramit" #update

print(student["name"])

name = student.get("name1", "custom default value")  #by default none 

student.pop("name") #delete value

student["roll"] = 5 #insert value, in dict modify and insert is same thing if key find then modify value ,if key doesnot find insert value

print(student)



#set ..............................................
s1 = {10, 10, "ram", 30, 10, 10} #doesnot have index
l1= [10, 10, 10] #it allows duplicate but set remove duplicate value
print(s1)
print(l1)

s1.add(25) #insert value in set
print(s1)