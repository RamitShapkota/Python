class student:
    def __init__(self, name, address):
        self.name = name
        self.address = address
    def show_details(self, age):
        print(f"my name is {self.name} and age is {age}")
        
s1 = student("Ramit", "Dhading")
s1.show_details(20)

class EmailValidator:
    def __init__(self, email):
        self.email = email

    def check(self):
          has_at = "@" in self.email
          has_lower = any(char.islower() for char in self.email)

          if has_at and has_lower:
              print(f"valid {self.email}")
          else:
              print("Invalid email")

email = input("Input your email: ")
validator = EmailValidator(email)
validator.check()