class animal():
def eat(self):
print("animal eat")
class animal_other():
def sleep(self):
print("animal_other sleep")
class dog(animal,animal_other):
def walk(self):
print("dogwalk")
d1=dog()
d1.eat()
d1.sleep()
d1.walk()
