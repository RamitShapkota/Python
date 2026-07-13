class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address
    
    def DisplayInfo(self):
        print(f"name is {self.name} and address is {self.address}")

class Developer(Employee):
    def __init__(self, name, address, language):
        self.language = language
        super().__init__(name, address)
    
    def DisplayInfo(self):
        return super().DisplayInfo()


d1 = Developer("Ram", "Dhading", "Js")
d1.DisplayInfo()
print(d1.name)