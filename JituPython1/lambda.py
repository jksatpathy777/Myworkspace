people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Chao", "house": "Ravenclaw"},
    {"name":"Draco", "house":"Slytherin"}
]


#    below code causes exception -Type error due to '<' symbol called by sort()
#people.sort()
#To avoid this exception define function & sort by 'key'
#ef f(person):
    #sort can be done on 'name' or on 'people' basis
    #return person["name"]
#    return person["house"]

#people.sort(key=f)

#we can also sort by using below code using key=lamda without the above function instead of above line
people.sort(key=lambda person:person["name"])


print(people)


