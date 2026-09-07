class animal():
def eat(self):
print("animal eat")
class mammal(animal):
def sleep(self):
print("mammal sleep")
class dog(mammal):
def spek(self):
print("dog speak")
d1=dog()
d1.eat()
d1.sleep()
d1.speak()
