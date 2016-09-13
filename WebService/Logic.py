'''
Here you can see all the methods of the program
'''
from Globals import *
from ClassAnimal import *
from ClassDisease import *
from ClassDose import *
from ClassPrescription import *
from ClassUser import *
from ClassMedicine import *


def callFunctions(function, *args):
    return function(args)

def addData(clase,*args):
    clase.add(*args)

def updateDataClass(clase, *args):
    clase.add()

def getDataFromList(lists,count):
    while True:
        yield lists[count]


def addDataList(lists, object):
    lists.append(object)



def defaultData():

    user = classUser()

    id = "123"
    passw = "123"
    name = "gabriel"
    acount = "admin"
    photo = "asd"
    parameters = [id, passw, name, acount, photo]
    if validateData(listUsers, id) == 0:
        addData(user, *parameters)
        addDataList(listUsers,user)

    user2 = classUser()
    id = "1234"
    passw = "12345"
    name = "juan"
    acount = "user"
    photo = "asd"
    parameters = [id, passw, name, acount, photo]
    if validateData(listUsers, id) == 0:
        addData(user2, *parameters)
        addDataList(listUsers,user2)

    disease = classDisease()
    parameters = ["123", "micaasd", "asd", "asd"]
    if validateData(listDiseases,  parameters[0]) == 0:
        addData(disease, *parameters)
        addDataList(listDiseases, disease)

    animal = classAnimal()
    parameters = ["123","caballo", "negro", "asd"]
    if validateData(listAnimals, parameters[0]) == 0:
        addData(animal, *parameters)
        addDataList(listAnimals,animal)

    animal2 = classAnimal()
    parameters = ["123", "caballo", "negro", "asd"]
    if validateData(listAnimals, parameters[0]) == 0:
        addData(animal2, *parameters)
        addDataList(listAnimals, animal2)


def showData():

    for element in listUsers:
        element.getInfo()

    for element in listAnimals:
        element.getInfo()

    for element in listDiseases:
        element.getInfo()

    for element in listPrescriptions:
        element.getInfo()

    for element in listDoses:
        element.getInfo()


def getUserName(id):
    for element in listUsers:
        if element.login == id:
            return element.name
    return 0

def getUserType(*args):
    for element in listUsers:
        if element.id == args[0] and element.password == args[1]:
            return element.accountType
    return 0

def validateData(lista,*args):
    list1 = list(filter(lambda x: x.id == args[0],lista))
    if len(list1) == 1:
        return 1
    return 0