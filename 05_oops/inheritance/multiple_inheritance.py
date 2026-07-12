class Employee:
    def __init__(self):
        self.user = "Ramit"
        self.address = "Dhading"

class EmailSend:
    def send_email(self,email):
        self.email = email

class Developer(Employee, EmailSend):
    pass

d1 = Developer()
print(f"name is {d1.user} and address is {d1.address}")
d1.send_email("ramit@gmail.com")
print(d1.email)