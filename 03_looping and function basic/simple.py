name = "ramit"

# for i in name:
#     print(i)

'''for index, value in enumerate(name, start=10): #to print wiht index
    print(index, value)'''

list1 = [10, 20, 30, 40, 50, 60, 7,5]

'''for i in list1:
    print(i)'''


#odd and even
odd = []
even = []

for i in list1:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("even:",even)
print("odd:",odd)


#if else in detailed
age = 20
if age>18:
    print("condition 1")
else:
    print("condition 2")

mark = 70
if mark>80:
    print("Grade: A+")
elif mark>=70 and mark<80:
    print("Grade: B+")
else:
    pass

#loop in dict

student = {
    "name": "ramit",
    "address": "kathmandu",
    "age": 20
}

#access both key and value pair
for key, value in student.items():
    print(key, value)

#access only keys
for key in student:
    print(key)

#access only value
for value in student.values():
    print(value)

#dict operation
info = {}
info["Name"] = "Ramit"
info["Roll"] = 3

info.pop("Name")

print(info.get("Name"))

#function....................

'''def function_name(a,b): #use snakecase to define function
    print(a,b)

function_name(10, 20)
function_name(20,30)'''

'''name = input("Enter your name:")
print(name)

age = int(input("Enter your age:"))
print(type(age))'''

def function_name(a,b):
    sum = a+b
    sub= a-b
    return sum, sub

add, diff = function_name(20,30)
result = function_name(20,30)
print(add, diff)
print(result) #give tuple

print(result[0])#tuple can be iterate 

list2 = []
list1 = [10, 20, 40, 5, 7]
def divisible_num(a):
    for i in list1:
        if i%a == 0:
            list2.append(i)

a = int(input("enter the number:"))
divisible_num(a)
print(f"divisible by {a} : {list2}")




