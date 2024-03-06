class Animal:
    def speak(self):
        return "..."
    
class Cat(Animal):
    def speak(self):
        return "Meoww"
    
class Dog(Animal):
    def speak(self):
        return "Gug Gug"
    
class Duck(Animal):
    def speak(self):
        return "Kwek Kwek"
    
print(Cat().speak())
print(Dog().speak())
print(Duck().speak())