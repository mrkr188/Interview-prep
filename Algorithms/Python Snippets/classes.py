# Simple class
class Programmer():
    """
    This is called a docstring. This class is to create a Programmer. 
    Functions inside a class is called a method.
    Methods are automatically passed the 'self' argument. 
    Any variable prefixed with 'self.' is available to the class.
    We will also be able to access this self prefixed variables from any instance of the class.
    """
    
    def __init__(self, name, age, *known_languages):
        """
        __init__ is a special method that Python automatically calls 
        when a new instance of the class is created.
        """
        self.name = name
        self.age = age
        self.languages = set(known_languages)
        
        # Default value for a class variable
        self.concepts_revised = 0
        
    def add_new_language(self, lang):
        self.languages.add(lang)
        print (str(self.name) + " knows a new language : " + str(lang) + " !!")
        
    def revise_concept(self, concept):
        self.concepts_revised += 1
        print (str(self.name) + " just revised " + str(concept) + " !!")
    
    def languages_known(self):
        return list(self.languages)
        
    def cv(self):
        print ("Name   : " + str(self.name))
        print ("Age    : " + str(self.age))
        print ("Skills : " + str(self.languages))


# Inheritance
'''
Programmer => Parent Class
Developer  => Child Class

Child class inherits from the base class.
The classes share a IS A relationship.
So, in this case, Developer IS A Programmer.
It has available all methods and variables from the parent class.
And can define methods and variables of its own.
'''
class Developer(Programmer):
    def __init__(self, name, age, expertise, yoe, *known_languages):
        
        # Call the parent class to initialize and give the child class an instance of the parent
        super().__init__(name, age, known_languages)
        self.expertise = expertise
        self.years_of_experience = yoe
        
    def specializes_in(self):
        return self.expertise
    
    def cv(self):
        """
        This method overrides the cv() method in the parent class.
        Any method in child class with same name as a method inherited from parent class
        overrides the parent class method.
        """
        print ("Name                : " + str(self.name))
        print ("Age                 : " + str(self.age))
        print ("Skills              : " + str(self.languages))
        print ("Expertise           : " + str(self.expertise))
        print ("Years of Experience : " + str(self.years_of_experience))



Programmer('nani', 27, 'python', 'java').cv()

Developer('nani', 27, 'data', 5, 'python', 'java').cv()