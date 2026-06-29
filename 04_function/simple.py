
def function_name(name, age):
    print(f"name is : {name}")
    print(f"age is : {age}")

name = "ramit"
age = 20
function_name(age=age,name=name) #match the variable of paramater and the variable of argument(keyword argument)\

#defult argument --> defult value must be in last position
def function_name(a,b,c=20):
    print(f"the value of a is {a} b is {b} c is {c}")
    print(a+b+c)

function_name(1, 2, 3) #in function order of argument and paramater must be match


def calculator(a, b):
    print(a+b)

result = calculator #assing functino to result variable
sum1 = result(20, 30)

