class Employee:

    name = None
    age = None
    phone = None
    address = None
    eid = None

    def __init__(self, name, age, phone, address, eid):
        self.name = name
        self.age = age
        self.phone = phone
        self.address = address
        self.eid = eid



emp1 = Employee("shelly", 28, "1234567895", "GNN", "12345")
print(emp1.name)
print(emp1.age)
print(emp1.phone)
print(emp1.address)
print(emp1.eid)


