class Place:
    
    def __init__(self,name):
        self.name=name
        self.position = []
        self.people=[]
        
    def possibleLocation(self,pointer):
        for i in pointer:
            self.position.append(i.name)
            
    def printPeople(self):
        print()
        print(self.people)