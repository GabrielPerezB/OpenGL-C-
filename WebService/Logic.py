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

def saveCurerntUser(accountType):
    userType.append(" ")
    userType[0]=accountType

def callFunctions(function, *args):
    return function(args)

def addData(clase,*args):
    clase.add(*args)

def deleteData(lista,id):
    lists = list(filter(lambda x: x.id != id,lista))
    lista.clear()
    for element in lists:
        lista.append(element)

def updateDataClass(clase, *args):
    clase.add()

def saveObjectToUpdate(lista,id):
    lists = list(filter(lambda x: x.id == id, lista))
    objectToUpdate.append(0)
    objectToUpdate[0]=lists[0]

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

    medicine = classMedicine()
    parameters = ["123", "medicina", "asd", "asd"]
    if validateData(listMedicines, parameters[0]) == 0:
        addData(medicine, *parameters)
        addDataList(listMedicines, medicine)

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

    dose = classDose()
    parameters = ["123", "123", "123", "123","55-80","700ml"]
    if validateData(listDoses, parameters[0]) == 0:
        addData(dose, *parameters)
        addDataList(listDoses, dose)

    prescription = classPresciption()
    parameters = ["123", "1234", "123", "123", "60", "123"]
    if validateData(listPrescriptions, parameters[0]) == 0:
        addData(prescription, *parameters)
        addDataList(listPrescriptions, prescription)
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
    for element in listMedicines:
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