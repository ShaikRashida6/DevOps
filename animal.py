class Animal:
    def__init__(self,name,age):
       self.name=name
       self.age=age
    def display(self):
       pass
class Carnivores:
     def dog(self,name,age,shout):
         self.shout=shout
         super.__init__(name,age)
     def display(self):
        pass
a=Animal("buddy",5)
print(a.display())
a=Carnivores("bow")
print(a.display())