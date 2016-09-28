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
from conectarDB import *

def safeToDB():
    insertToDisease()
    inserToAnimal()
    inserToDoses()
    inserToMedicine()
    inserToPrescription()
    inserToUser()
    deleteAnimalFromDB()
    deleteDoseFromDB()
    deleteMedicineFromDB()
    deleteUserFromDB()
    deleteDiseaseFromDB()
    deletePrescriptionFromDB()
    cancel()

def cancel():
    deleteAllFromLists()
    loadToUser()
    loadToAnimal()
    loadToDisease()
    loadToDoses()
    loadToMedicine()
    loadToPrescription()


def deleteAllFromLists():
        listAnimals.clear()
        listPrescriptions.clear()
        listMedicines.clear()
        listDiseases.clear()
        listUsers.clear()
        listDoses.clear()

def deleteAnimalFromDB():
    animals = list(map(lambda x: x.id, listAnimals))
    deleteAnimal(animals)

def deleteDiseaseFromDB():
    diseases = list(map(lambda x: x.id, listDiseases))
    deleteAnimal(diseases)

def deleteDoseFromDB():
    doses = list(map(lambda x: x.id, listDoses))
    deleteAnimal(doses)

def deleteMedicineFromDB():
    medicines = list(map(lambda x: x.id, listMedicines))
    deleteAnimal(medicines)

def deletePrescriptionFromDB():
    prescriptions = list(map(lambda x: x.id, listPrescriptions))
    deleteAnimal(prescriptions)

def deleteUserFromDB():
    users = list(map(lambda x: x.id, listUsers))
    deleteAnimal(users)


def saveCurerntUser(accountType, id):
    userType.append(" ")
    userType[0]=accountType
    userType[1]=id

def addData(clase,*args):
    clase.add(*args)

def deleteData(lista,id):
    lists = list(filter(lambda x: x.id != id,lista))
    lista.clear()
    for element in lists:
        lista.append(element)

def saveObjectToUpdate(lista,id):
    lists = list(filter(lambda x: x.id == id, lista))
    objectToUpdate.append(0)
    objectToUpdate[0]=lists[0]

def getDataFromList(lists,count):
    while True:
        yield lists[count]

def getDataFromListAnimals():
    count = 0
    while len(listAnimals)>= count:
        if count >= len(listAnimals):
            print("Es el Final")
        else:
            yield listAnimals[count]
        count += 1


def getDataFromListMedisines():
    count = 0
    while len(listMedicines) >= count:
        if count >= len(listMedicines):
            print("Es el Final")
        else:

            yield listMedicines[count]
        count += 1

def getDataFromListPrescriptions():
    count = 0
    while len(listPrescriptions)>= count:
        data = []
        if count >= len(listPrescriptions):
            print("Es el Final")
        else:
            data.append(listPrescriptions[count])
            user = list(filter(lambda x: x.id == data[0].userId,listUsers))
            data.append(user[0])
            animal = list(filter(lambda x: x.id == data[0].animalId, listAnimals))
            data.append(animal[0])
            disease = list(filter(lambda x: x.id == data[0].diseaseId, listDiseases))
            data.append(disease[0])
            dose = list(filter(lambda x: x.id == data[0].doseId, listDoses))
            data.append(dose[0])
            medicine = list(filter(lambda x: x.id == dose[0].medicineId, listMedicines))
            data.append(medicine[0])

            yield data
        count += 1

def getDataDosisXAnimal():
    count = 0
    while len(listAnimals)>= count:
        data = []
        if count >= len(listAnimals):
            print("Es el Final")
        else:
            data.append(listAnimals[count])
            dose = list(filter(lambda x: x.animalId == data[0].id, listDoses))
            medicine = list(filter(lambda x: x.id == dose[0].medicineId, listMedicines))
            count2=0
            while count2<len(dose):
                info = [dose[count2],medicine[count2]]
                data.append(info)
                count2+=1
            yield data
        count += 1

def getDataDosisXDisease():
    count = 0
    while len(listDiseases) >= count:
        data = []
        if count >= len(listDiseases):
            print("Es el Final")
        else:
            data.append(listDiseases[count])
            dose = list(filter(lambda x: x.diseaseId == data[0].id, listDoses))
            medicine = list(filter(lambda x: x.id == dose[0].medicineId, listMedicines))
            count2 = 0
            while count2 < len(dose):
                info = [dose[count2], medicine[count2]]
                data.append(info)
                count2 += 1
            yield data
        count += 1


def addDataList(lists, object):
    lists.append(object)

def getRecomendedDose(lista, weight, animalId,diseaseId):
    lists = list(filter(lambda x: x.weightRange.split("-")[0] <= weight
                    and x.weightRange.split("-")[1]>= weight
                    and x.animalId == animalId
                    and x.diseaseId == diseaseId, lista))
    print(len(lists))
    if len(lists)>= 1:
        return lists[0].id
    else:
        return 0

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


def loadToUser():
    mylist = loadUsers()
    for i in mylist:
        user = classUser()
        parameters = [str(i[0]), str(i[1]), str(i[2]), str(i[3]), str(i[4])]
        addData(user, *parameters)
        addDataList(listUsers, user)

    print("Users")
    for element in listUsers:
        element.getInfo()


def loadToAnimal():
    mylist = loadAnimals()
    for i in mylist:
        animal = classAnimal()
        parameters = [str(i[0]),str(i[1]),str(i[2]),str(i[3])]
        addData(animal, *parameters)
        addDataList(listAnimals,animal)
    print("Animals")
    for element in listAnimals:
        element.getInfo()

def loadToDisease():
    mylist = loadDiseases()
    for i in mylist:
        diseases = classDisease()
        parameters = [str(i[0]), str(i[1]),str(i[2]), str(i[3])]
        addData(diseases, *parameters)
        addDataList(listDiseases, diseases)
    print("Disease")
    for element in listDiseases:
        element.getInfo()

def loadToMedicine():
    mylist = loadMedicine()
    for i in mylist:
        medicine = classMedicine()
        parameters = [str(i[0]), str(i[1]),str(i[2]), str(i[3])]
        addData(medicine, *parameters)
        addDataList(listMedicines, medicine)

    print("Medicene")
    for element in listMedicines:
        element.getInfo()

def loadToDoses():
    mylist = loadDoses()
    for i in mylist:
        dose = classDose()
        parameters = [str(i[0]), str(i[1]),str(i[2]), str(i[3]), str(i[4]), str(i[5])]
        addData(dose, *parameters)
        addDataList(listDoses, dose)

    print("Doses")
    for element in listDoses:
        element.getInfo()

def loadToPrescription():
    mylist = loadPrescription()
    for i in mylist:
        prescription = classPresciption()
        parameters = [str(i[0]), str(i[1]),str(i[2]), str(i[3]), str(i[4]), str(i[5])]
        addData(prescription, *parameters)
        addDataList(listPrescriptions, prescription)

    print("Prescription")
    for element in listPrescriptions:
        element.getInfo()


def inserToAnimal():
    for element in listAnimals:
        idAnimal = int(element.id)
        nombre = str(element.name)
        descrip =str(element.description)
        foto = str(element.photo)
        parameter = [idAnimal,nombre,descrip,foto]
        insertAnimal(*parameter)

def insertToDisease():
    for element in listDiseases:
        idenfermedad = int(element.id)
        nombreEnferme = str(element.name)
        descripEnferme =str(element.description)
        fotoEnferme = str(element.photo)
        parameter = [idenfermedad, nombreEnferme, descripEnferme, fotoEnferme]
        insertDisease(*parameter)

def inserToMedicine():
    for element in listMedicines:
        idmedicame = int(element.id)
        nombreMedicame = str(element.name)
        descripMedicame =str(element.description)
        fotoMedicame = str(element.photo)
        parameter = [idmedicame, nombreMedicame, descripMedicame, fotoMedicame]
        insertMedicine(*parameter)

def inserToUser():
    for element in listUsers:
        idUsuario = int(element.id)
        passUsuario = str(element.password)
        nameUsuario =str(element.name)
        permisoUsuario = str(element.accountType)
        fotoUsuario = str(element.photo)
        parameter = [idUsuario, passUsuario, nameUsuario, permisoUsuario,fotoUsuario]
        insertUser(*parameter)

def inserToDoses():
    for element in listDoses:
        idDosis = int(element.id)
        idAnimalDosis = int(element.animalId)
        idmedicameDosis =int(element.medicineId)
        idenfermedadDosis = int(element.diseaseId)
        rangoPesoDosis = str(element.weightRange)
        dosis = str(element.dose)
        parameter = [idDosis, idAnimalDosis, idmedicameDosis, idenfermedadDosis, rangoPesoDosis,dosis]
        insertDoses(*parameter)

def inserToPrescription():
    for element in listPrescriptions:
        idPrescripcion = int(element.id)
        idUsuarioPrescripcion = int(element.userId)
        idAnimalPrescripcion =int(element.animalId)
        idenfermedadPrescripcion = int(element.diseaseId)
        pesoPrescripcion = str(element.weight)
        idDosisPrescripcion = int(element.doseId)
        parameter = [idPrescripcion, idUsuarioPrescripcion, idAnimalPrescripcion, idenfermedadPrescripcion, pesoPrescripcion,idDosisPrescripcion]
        insertPrescription(*parameter)