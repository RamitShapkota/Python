#setattr_getattr_hasattr
 #mainly used in database : in database row is object  and column is attribute

#syntax
#setattr(objacet, attribute_name, new_value)
#getaatr(object, attribute_name, default_value_if_need)
#hasattr(object, attribute_name) give true or false if attribute exists give true else false
"""
class Student:
    def __init__(self, name):
        self.name = name

s = Student("Ram")

setattr(s, "age", 20) # setattr() - Set a new attribute
setattr(s, "address", "pokhara")

print("Name:", getattr(s, "name"))# getattr() - Get the value of an attribute
print("Age:", getattr(s, "age"))
print("address:" , getattr(s, "address"))

print("Has name?", hasattr(s, "name"))  # hasattr() - Check if an attribute exists
print("Has address?", hasattr(s, "address"))
print("has phone?", hasattr(s, "phone"))
"""

class Employee:
    def __init__(self, details):
        # Set attributes from dictionary
        for key, value in details.items():
            setattr(self, key, value)

    def update(self):
        key = input("Enter key to update (name/department/salary): ")

        if hasattr(self, key):
            value = input("Enter new value: ")

            if key == "salary":
                value = int(value)

            setattr(self, key, value)
            print("Updated Successfully!")
        else:
            print("Invalid Key")

    def display(self):
        print("Name:", getattr(self, "name"))
        print("Department:", getattr(self, "department"))
        print("Salary:", getattr(self, "salary"))

details = {
    "name": "Dikshya",
    "department": "IT",
    "salary": 50000
}

emp = Employee(details)

print("Before Update")
emp.display()
emp.update()
print("After Update")
emp.display()