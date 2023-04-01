class parent:     #this parent class acts like a super glass
    def __init__(self, name):
        print('Parent __init__ ', name)


class parent2:
    def __init__(self, name):
        print('Parent2 __init__', name)

class Child(parent2, parent):    #the child class is a sub-class that inherits from the super class
    def __init__(self):
        print("Child __init__ ")
        parent.__init__(self, 'Daniel')
        parent2.__init__(self, 'Freida')

child = Child()
print(Child.__mro__)  #MRO stands for method resolution order tells you which class will be executed first. And this is based on how the classes are inherited in the subclass.
