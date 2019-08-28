# Here we'll create a blueprint for an `OurClass` object, but now using 
# an inputted name for the name attribute and the location attribute. 
# `OurClass` also accepts an optional size attribute.  
class OurClass(): 
    
    def __init__(self, name, location, size=0): 
        self.name = name
        self.location = location
        self.size = size

