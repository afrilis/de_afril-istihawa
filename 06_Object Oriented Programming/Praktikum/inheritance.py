# Class Induk
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def identity(self):
        return self.first_name + " " + self.last_name

 # Class yang diwarisi   
class Employee(Person):
    def __init__(self, first_name, last_name, staff_number):
        super().__init__(first_name, last_name)
        self.staff_number = staff_number
    def identity(self):
        return super().identity() + " " + str(self.staff_number)
    
# Kita akan membuat 2 Objek dari Kelas Person dan Kelas Employee
person_afril = Person("Afril", "Istihawa")
employee_afril = Employee("Afril", "Istihawa", 19823)

# Kita akan Memanggil Method Identity dari Kelas Person 
identity_person_afril = person_afril.identity() # akan memanggil dari baris 13
print(identity_person_afril)

# Kita akan Memanggil Method Identity dari Kelas Employee
identity_employee_afril = employee_afril.identity()
print(identity_employee_afril)