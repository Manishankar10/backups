from model.place import Place
from model.person import Person

def travel(Person,to):
    location=Person.getLocation()
    print(to.name,location.position)
    if(to.name in location.position):
        location.people.remove(Person.Person_name)
        to.people.append(Person.Person_name)
        Person.setLocation(to)
        print(to.name,end='->')
       
    else:
        print("No possibility for the kid to go there!!!",end='? ->')
##Sample Inputs:
# Home = Place('Home')
# School = Place('School')
# Playground = Place('Playground')
# TrainingCenter = Place('TrainingCenter')

# Home.possibleLocation(School,Playground,TrainingCenter)
# School.possibleLocation(Home,Playground)
# Playground.possibleLocation(Home)
# TrainingCenter.possibleLocation(Home)



Places=[]
objs=[]
n=int(input("Enter the number of locations : "))
print("Enter the locations : ")
for i in range(n):
    Places.append(input())
for i in Places:
    i=Place(i)
    objs.append(i)
for i in objs:
    list=[]
    a=int(input("Enter the Possibilities for {} : ".format(i.name)))
    while(a>0):
        b=input('Enter the Possible location: ')
        for i in objs:
            if i.name==b:
                list.append(i)
                a=a-1
    i.possibleLocation(list)

Person1= Person("Ram",objs[0])
travel(Person1,objs[1])
# travel(Person1,objs[2])
# travel(Person1,objs[0])
# travel(Person1,objs[3])
# travel(Person1,objs[2])
# objs[3].printPeople()
# travel(Person1,objs[0])
# Person2=Person("Jai",objs[0])
# travel(Person2,objs[3])
# Person3=Person("Jack",objs[0])
# travel(Person3,objs[3])
# travel(Person3,objs[0])
# objs[0].printPeople()