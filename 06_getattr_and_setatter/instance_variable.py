class College:
    college_name = "EEC" #class variable : same for all object

    def __init__(self,location):  #instance variable  : change with objects
        self.location = location

    def show_details(self):
        print("College Name:", College.college_name)
        print("Location:", self.location)

c1 = College("sanepa")
c2 = College("Kalanki")
c1.show_details()
c2.show_details()
print(College.college_name) #class varibale can be accessed by classname.variablename
print(c1.location)