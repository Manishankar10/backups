class Person:
    
    def __init__(self,name,Personlocation):
        self.Person_name=name
        print()
        print(self.Person_name+' is initially at {}'.format(Personlocation.name))
        self.location=Personlocation
        self.location.people.append(self.Person_name)
        
    def getLocation(self):
        return self.location
            
    def setLocation(self,to):
        self.location=to