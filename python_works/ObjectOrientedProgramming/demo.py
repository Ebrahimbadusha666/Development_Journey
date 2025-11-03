
"""
ObjectOrientedProgramming
OOP is a programming paradiagram (style of coding) that allows us to bring real-world entities in to programming by using classes and objects.

class: plan, blueprint, design, pattern, template
object: (realword entity) 



class: plan,design pattern,blue print

object:realworld entity

"""     




class Animal:

    name:str

    color:str

    leg_count:int

    sound:str

    eat:str

    def set_name(self,name):

        self.name=name

    def walk(self):

        print(self.name," walks")

    def run(self):

        print(self.name," runs")

    def eat(self):

        print(self.name,"animal eating")


dog_instance=Animal()

dog_instance.set_name("dog")

dog_instance.walk()




