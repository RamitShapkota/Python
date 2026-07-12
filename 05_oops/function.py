def fun1(*args, **kwargs):
    print(args) #output => touple
    print(kwargs) #output => dict

fun1(10, 11, name1 = "ram", address = "pokhara")


class Class1:
    def sum(self, *args):
        total = 0
        for i in args:
            total += i
        print("Sum:", total)

    def display(self, **kwargs):
        for key, value in kwargs.items():
            print(key, ":", value)


obj = Class1()

obj.sum(10, 20, 30, 40)

obj.display(
    name="Ramit",
    address="Pokhara",
    age=20,
    college="Pokhara University"
)
