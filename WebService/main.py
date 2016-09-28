'''
Programed by GABRIEL PEREZ AND CRISTIAN ALVARADO
LENGUAJES DE PROGRAMACION PARADIGMA FUNCIONAL
'''

from flask import Flask, render_template, request, url_for, redirect
from Logic import *
from Globals import *
func = getDataFromListAnimals()
func1 = getDataFromListMedisines()
func2 = getDataFromListPrescriptions()
func4 = getDataDosisXAnimal()
func3 = getDataDosisXDisease()

app = Flask(__name__)
@app.route('/profileAdmin/',methods=["POST","GET"])
def profileAdmin():
    if len(userType) ==0:
        return redirect(url_for('loginPage'))
    try:
        if request.method == "POST":
            if request.form['action'] == 'Guardar Cambios':
                safeToDB()
            elif request.form['action'] == 'Cancelar Cambios':
                cancel()
            elif request.form['action'] == 'Listar Animales':
                count = 0
                while count <=4:
                    returned = func.__next__().getInfo()
                    if returned != "":
                        print(returned)
                    count += 1
            elif request.form['action'] == 'Listar Medicinas':
                count = 0
                while count <=4:
                    returned = func1.__next__().getInfo()
                    if returned != "":
                        print(returned)
                    count += 1

            elif request.form['action'] == 'Listar Prescripciones':
                count = 0
                while count <=4:
                    returned = func2.__next__()

                    print("\nPrescripcion: "+returned[0].id+" peso: "+returned[0].weight+
                               "\n    usuario: "+returned[1].name+
                               "\n    animal: "+returned[2].name+" descripcion: "+returned[2].description+
                               "\n   enfermedad: "+returned[3].name+" descripcion: "+returned[3].description+
                               "\n    dosis: "+returned[4].dose+
                               "\n    medicina: "+returned[5].name+" descripcion: "+returned[5].description)
                    count += 1
            elif request.form['action'] == 'Listar dosis x enfermedad':
                count = 0
                while count <=4:
                    returned = func3.__next__()
                    print("\nEnfermedad: "+returned[0].name+" descripcion: "+returned[0].description)
                    count2 = 1
                    while count2 <= len(returned):
                        print("    dosis: "+returned[count2][0].dose+
                            "\n    medicina: "+returned[count2][1].name+" descripcion: "+returned[count2][1].description)
                        count2 +=2

                    count += 1

            elif request.form['action'] == 'Listar dosis x animal':
                count = 0
                while count <=4:
                    returned = func4.__next__()
                    print("\nAnimal: "+returned[0].name+" descripcion: "+returned[0].description)
                    count2 = 1
                    while count2 <= len(returned):
                        print("    dosis: " + returned[count2][0].dose +
                            "\n    medicina: " + returned[count2][1].name + " descripcion: " + returned[count2][1].description)
                        count2 += 2

                    count += 1


        return render_template("profileAdmin.html")
    except:
        return render_template("profileAdmin.html")
    return render_template("profileAdmin.html")


@app.route('/deleteUser/',methods=["POST","GET"])
def deleteUser():
    error = ""
    try:
        if request.method == "POST":
            attempment_id= request.form['id']
            if validateData(listUsers,attempment_id) == 0:
                error = "Usuario no existe"
                return render_template("deleteUser.html", error= error)
            deleteData(listUsers,attempment_id)
            return  redirect(url_for('profileAdmin'))

        return render_template("deleteUser.html")
    except:
        return render_template("deleteUser.html", error=error)

@app.route('/deleteAnimal/',methods=["POST","GET"])
def deleteAnimal():
    error = ""
    try:
        if request.method == "POST":
            attempment_id= request.form['id']
            if validateData(listAnimals,attempment_id) == 0:
                error = "Animal no existe"
                return render_template("deleteAnimal.html", error= error)
            deleteData(listAnimals,attempment_id)
            if userType[0] == "admin":
                showData()
                return redirect(url_for('profileAdmin'))
            else:
                return redirect(url_for('profileUser'))
        return render_template("deleteAnimal.html")
    except:
        return render_template("deleteAnimal.html", error=error)



@app.route('/deleteDisease/',methods=["POST","GET"])
def deleteDisease():
    error = ""
    try:
        if request.method == "POST":
            attempment_id= request.form['id']
            if validateData(listDiseases,attempment_id) == 0:
                error = "Enfermedad no existe"
                return render_template("deleteDisease.html", error= error)
            deleteData(listDiseases,attempment_id)
            if userType[0] == "admin":
                return redirect(url_for('profileAdmin'))
            else:
                return redirect(url_for('profileUser'))
        return render_template("deleteDisease.html")
    except:
        return render_template("deleteDisease.html", error=error)


@app.route('/deleteDose/',methods=["POST","GET"])
def deleteDose():
    error = ""
    try:
        if request.method == "POST":
            attempment_id= request.form['id']
            if validateData(listDoses,attempment_id) == 0:
                error = "Dosis no existe"
                return render_template("deleteDose.html", error= error)
            deleteData(listDoses,attempment_id)
            if userType[0] == "admin":
                return redirect(url_for('profileAdmin'))
            else:
                return redirect(url_for('profileUser'))
        return render_template("deleteDose.html")
    except:
        return render_template("deleteDose.html", error=error)

@app.route('/deleteMedicine/',methods=["POST","GET"])
def deleteMedicine():
    error = ""
    try:
        if request.method == "POST":
            attempment_id= request.form['id']
            if validateData(listMedicines,attempment_id) == 0:
                error = "Medicina no existe"
                return render_template("deleteMedicine.html", error= error)
            deleteData(listMedicines,attempment_id)
            if userType[0] == "admin":
                return redirect(url_for('profileAdmin'))
            else:
                return redirect(url_for('profileUser'))
        return render_template("deleteMedicine.html")
    except:
        return render_template("deleteMedicine.html", error=error)

@app.route('/deletePrescription/',methods=["POST","GET"])
def deletePrescription():
    error = ""
    try:
        if request.method == "POST":
            attempment_id= request.form['id']
            if validateData(listPrescriptions,attempment_id) == 0:
                error = "Prescripcion no existe"
                return render_template("deletePrescription.html", error= error)
            deleteData(listPrescriptions,attempment_id)
            if userType[0] == "admin":
                return redirect(url_for('profileAdmin'))
            else:
                return redirect(url_for('profileUser'))
        return render_template("deletePrescription.html")
    except:
        return render_template("deletePrescription.html", error=error)

@app.route('/searchAnimalToUpdate/',methods=["POST","GET"])
def searchAnimalToUpdate():
    error = ""
    try:
        if request.method == "POST":
            attempment_id= request.form['id']
            if validateData(listAnimals,attempment_id) == 0:
                error = "Animal no existe"
                return render_template("searchAnimalToUpdate.html", error= error)
            saveObjectToUpdate(listAnimals,attempment_id)
            return redirect(url_for('updateAnimal'))
        return render_template("searchAnimalToUpdate.html")
    except:
        return render_template("searchAnimalToUpdate.html", error=error)


@app.route('/updateAnimal/',methods=["POST","GET"])
def updateAnimal():
    error = ''
    try:
        if request.method == "POST":
            attempment_id = request.form['id']
            attempment_name = request.form['name']
            attempment_description = request.form['description']
            attempment_photo = request.form['photo']
            parameters = [attempment_id,attempment_name, attempment_description,attempment_photo]
            deleteData(listAnimals, attempment_id)
            animal = classAnimal()
            addData(animal, *parameters)
            addDataList(listAnimals, animal)
            if userType[0] == "admin":
                return redirect(url_for('profileAdmin'))
            else:
                return redirect(url_for('profileUser'))
        return render_template("updateAnimal.html", originalId = objectToUpdate[0].id,
                               originalName = objectToUpdate[0].name,
                               originalDescription = objectToUpdate[0].description,
                               originalPhoto = objectToUpdate[0].photo)
    except:
        return render_template("updateAnimal.html", error=error)

@app.route('/searchDiseaseToUpdate/',methods=["POST","GET"])
def searchDiseaseToUpdate():
    error = ""
    try:
        if request.method == "POST":
            attempment_id= request.form['id']
            if validateData(listAnimals,attempment_id) == 0:
                error = "Enfermedad no existe"
                return render_template("searchDiseaseToUpdate.html", error= error)
            saveObjectToUpdate(listDiseases,attempment_id)
            return redirect(url_for('updateDisease'))
        return render_template("searchDiseaseToUpdate.html")
    except:
        return render_template("searchDiseaseToUpdate.html", error=error)


@app.route('/updateDisease/',methods=["POST","GET"])
def updateDisease():
    error = ''
    try:
        if request.method == "POST":
            attempment_id = request.form['id']
            attempment_name = request.form['name']
            attempment_description = request.form['description']
            attempment_photo = request.form['photo']
            parameters = [attempment_id, attempment_name, attempment_description, attempment_photo]
            deleteData(listDiseases,attempment_id)
            disease = classDisease()
            addData(disease, *parameters)
            addDataList(listDiseases, disease)
            if userType[0] == "admin":
                return redirect(url_for('profileAdmin'))
            else:
                return redirect(url_for('profileUser'))
        return render_template("updateDisease.html", originalId = objectToUpdate[0].id,
                               originalName = objectToUpdate[0].name,
                               originalDescription = objectToUpdate[0].description,
                               originalPhoto = objectToUpdate[0].photo)
    except:
        return render_template("updateDisease.html", error=error)


@app.route('/searchDoseToUpdate/',methods=["POST","GET"])
def searchDoseToUpdate():
    error = ""
    try:
        if request.method == "POST":
            attempment_id= request.form['id']
            if validateData(listDoses,attempment_id) == 0:
                error = "Dosis no existe"
                return render_template("searchDoseToUpdate.html", error= error)
            saveObjectToUpdate(listDoses,attempment_id)
            return redirect(url_for('updateDose'))
        return render_template("searchDoseToUpdate.html")
    except:
        return render_template("searchDoseToUpdate.html", error=error)


@app.route('/updateDose/',methods=["POST","GET"])
def updateDose():
    error = ""
    try:

        if request.method == "POST":
            attempment_id = request.form['id']
            attempment_idAnimal = request.form['idAnimal']
            attempment_idMedicine = request.form['idMedicine']
            attempment_idDisease = request.form['idDisease']
            attempment_weightRnage = request.form['weightRange']
            attempment_dose = request.form['dose']

            parameters = [attempment_id, attempment_idAnimal, attempment_idMedicine,
                          attempment_idDisease, attempment_weightRnage, attempment_dose]
            if validateData(listUsers, attempment_idMedicine) == 0:
                error = "Medicamento no existe"
                return render_template("updateDose.html",originalId=objectToUpdate[0].id ,
                        originalIdAnimal= objectToUpdate[0].animalId,
                        originalIdMedicine= objectToUpdate[0].medicineId,
                        originalIdDisease= objectToUpdate[0].diseaseId,
                        originalrangoPeso= objectToUpdate[0].weightRange,
                        originalDose= objectToUpdate[0].dose,
                        error = error)
            if validateData(listAnimals, attempment_idAnimal) == 0:
                error = "Animal no existe"
                return render_template("updateDose.html",originalId=objectToUpdate[0].id ,
                        originalIdAnimal= objectToUpdate[0].animalId,
                        originalIdMedicine= objectToUpdate[0].medicineId,
                        originalIdDisease= objectToUpdate[0].diseaseId,
                        originalrangoPeso= objectToUpdate[0].weightRange,
                        originalDose= objectToUpdate[0].dose,
                        error = error)
            if validateData(listDiseases, attempment_idDisease) == 0:
                error = "Enfermedad no existe"
                return render_template("updateDose.html",originalId=objectToUpdate[0].id ,
                        originalIdAnimal= objectToUpdate[0].animalId,
                        originalIdMedicine= objectToUpdate[0].medicineId,
                        originalIdDisease= objectToUpdate[0].diseaseId,
                        originalrangoPeso= objectToUpdate[0].weightRange,
                        originalDose= objectToUpdate[0].dose,
                        error = error)
            deleteData(listDoses,attempment_id)
            dose = classDose()
            addData(dose, *parameters)
            addDataList(listDoses, dose)
            showData()
            if userType[0] == "admin":
                return redirect(url_for('profileAdmin'))
            else:
                return redirect(url_for('profileUser'))
        return render_template("updateDose.html",originalId=objectToUpdate[0].id ,
                    originalIdAnimal= objectToUpdate[0].animalId,
                    originalIdMedicine= objectToUpdate[0].medicineId,
                    originalIdDisease= objectToUpdate[0].diseaseId,
                    originalrangoPeso= objectToUpdate[0].weightRange,
                    originalDose= objectToUpdate[0].dose,
                    error = error)

    except:
        return render_template("updateDose.html", error=error)


@app.route('/searchMedicineToUpdate/',methods=["POST","GET"])
def searchMedicineToUpdate():
    error = ""
    try:
        if request.method == "POST":
            attempment_id= request.form['id']
            if validateData(listMedicines,attempment_id) == 0:
                error = "Medicina no existe"
                return render_template("searchMedicineToUpdate.html", error= error)
            saveObjectToUpdate(listMedicines,attempment_id)
            return redirect(url_for('updateMedicine'))
        return render_template("searchMedicineToUpdate.html")
    except:
        return render_template("searchMedicineToUpdate.html", error=error)


@app.route('/updateMedicine/',methods=["POST","GET"])
def updateMedicine():
    error = ''
    try:
        if request.method == "POST":
            attempment_id = request.form['id']
            attempment_name = request.form['name']
            attempment_description = request.form['description']
            attempment_photo = request.form['photo']
            parameters = [attempment_id, attempment_name, attempment_description, attempment_photo]
            deleteData(listMedicines,attempment_id)
            medicine = classMedicine()
            addData(medicine, *parameters)
            addDataList(listMedicines, medicine)
            if userType[0] == "admin":
                return redirect(url_for('profileAdmin'))
            else:
                return redirect(url_for('profileUser'))
            return render_template("updateMedicine.html", originalId = objectToUpdate[0].id,
                               originalName = objectToUpdate[0].name,
                               originalDescription = objectToUpdate[0].description,
                               originalPhoto = objectToUpdate[0].photo)
    except:
        return render_template("updateMedicine.html", error=error)


@app.route('/searchPrescriptionToUpdate/',methods=["POST","GET"])
def searchPrescriptionToUpdate():
    error = ""
    try:
        if request.method == "POST":
            attempment_id= request.form['id']
            if validateData(listPrescriptions,attempment_id) == 0:
                error = "Prescripcion no existe"
                return render_template("searchPrescriptionToUpdate.html", error= error)
            saveObjectToUpdate(listPrescriptions,attempment_id)
            return redirect(url_for('updatePrescription'))
        return render_template("searchPrescriptionToUpdate.html")
    except:
        return render_template("searchPrescriptionToUpdate.html", error=error)


@app.route('/updatePrescription/',methods=["POST","GET"])
def updatePrescription():
    error = ""
    try:
        if request.method == "POST":
            attempment_id = request.form['id']
            attempment_idUser = request.form['idUser']
            attempment_idAnimal = request.form['idAnimal']
            attempment_idDisease = request.form['idDisease']
            attempment_weight = request.form['weight']

            if validateData(listAnimals,attempment_idAnimal) == 0:
                error = "Animal no existe"
                return render_template("updatePrescription.html", originalId=objectToUpdate[0].id,
                                     originaluserId=objectToUpdate[0].userId,
                                     originalAnimalId=objectToUpdate[0].animalId,
                                     originalDiseaseId=objectToUpdate[0].diseaseId,
                                     originalWeight=objectToUpdate[0].weight,
                                     originalDoseId=objectToUpdate[0].doseId,
                                     error = error)
            if validateData(listDiseases,attempment_idDisease) == 0:
                error = "Enfermedad no existe"
                return render_template("updatePrescription.html", originalId=objectToUpdate[0].id,
                                     originaluserId=objectToUpdate[0].userId,
                                     originalAnimalId=objectToUpdate[0].animalId,
                                     originalDiseaseId=objectToUpdate[0].diseaseId,
                                     originalWeight=objectToUpdate[0].weight,
                                     originalDoseId=objectToUpdate[0].doseId,
                                     error = error)
            if len(listDoses) == 0:
                error = "No Hay Dosis"
                return render_template("updatePrescription.html", originalId=objectToUpdate[0].id,
                                       originaluserId=objectToUpdate[0].userId,
                                       originalAnimalId=objectToUpdate[0].animalId,
                                       originalDiseaseId=objectToUpdate[0].diseaseId,
                                       originalWeight=objectToUpdate[0].weight,
                                       originalDoseId=objectToUpdate[0].doseId,
                                       error=error)
            attempment_dose = getRecomendedDose(listDoses,attempment_weight, attempment_idAnimal,attempment_idDisease)
            if attempment_dose == 0:
                error = "No Hay Dosis recomendada"
                return render_template("updatePrescription.html", originalId=objectToUpdate[0].id,
                                       originaluserId=objectToUpdate[0].userId,
                                       originalAnimalId=objectToUpdate[0].animalId,
                                       originalDiseaseId=objectToUpdate[0].diseaseId,
                                       originalWeight=objectToUpdate[0].weight,
                                       originalDoseId=objectToUpdate[0].doseId,
                                       error=error)

            parameters = [attempment_id, attempment_idUser, attempment_idAnimal,
                          attempment_idDisease, attempment_weight, attempment_dose]

            deleteData(listPrescriptions,attempment_id)
            prescription = classPresciption()
            addData(prescription, *parameters)
            addDataList(listPrescriptions, prescription)
            if userType[0] == "admin":
                return redirect(url_for('profileAdmin'))

            else:
                return redirect(url_for('profileUser'))

        return render_template("updatePrescription.html", originalId=objectToUpdate[0].id,
                                     originaluserId=objectToUpdate[0].userId,
                                     originalAnimalId=objectToUpdate[0].animalId,
                                     originalDiseaseId=objectToUpdate[0].diseaseId,
                                     originalWeight=objectToUpdate[0].weight,
                                     originalDoseId=objectToUpdate[0].doseId,
                                     error = error)
    except:
        return render_template("updatePrescription.html", originalId=objectToUpdate[0].id,
                                     originaluserId=objectToUpdate[0].userId,
                                     originalAnimalId=objectToUpdate[0].animalId,
                                     originalDiseaseId=objectToUpdate[0].diseaseId,
                                     originalWeight=objectToUpdate[0].weight,
                                     originalDoseId=objectToUpdate[0].doseId,
                                     error = error)





@app.route('/searchUserToUpdate/',methods=["POST","GET"])
def searchUserToUpdate():
    error = ""
    try:
        if request.method == "POST":
            attempment_id= request.form['id']
            if validateData(listUsers,attempment_id) == 0:
                error = "Usuario no existe"
                return render_template("searchUserToUpdate.html", error= error)
            saveObjectToUpdate(listUsers,attempment_id)
            return redirect(url_for('updateUser'))
        return render_template("searchUserToUpdate.html")
    except:
        return render_template("searchUserToUpdate.html", error=error)

@app.route('/updateUser/',methods=["POST","GET"])
def updateUser():
    showData()
    error = ""
    try:
        if request.method == "POST":
            attempment_id= request.form['id']
            attempment_password = request.form['password']
            attempment_name = request.form['name']
            attempment_accountType = request.form['accountType']
            attempment_photo = request.form['photo']
            parameters = [attempment_id, attempment_password,attempment_name, attempment_accountType, attempment_photo]
            deleteData(listUsers,attempment_id)
            user = classUser()
            addData(user,*parameters)
            addDataList(listUsers, user)
            showData()
            return redirect(url_for('profileAdmin'))

        return render_template("updateUser.html", originalId = objectToUpdate[0].id,
                               originalPassword = objectToUpdate[0].password,
                               originalName = objectToUpdate[0].name,
                               originalAccountType = objectToUpdate[0].accountType,
                               originalPhoto=objectToUpdate[0].photo)
    except:
        return render_template("updateUser.html", error=error)


@app.route('/createUser/',methods=["POST","GET"])
def createUser():
    showData()
    error = ""
    try:
        if request.method == "POST":
            attempment_id= request.form['id']
            attempment_password = request.form['password']
            attempment_name = request.form['name']
            attempment_accountType = request.form['accountType']
            attempment_photo = request.form['photo']
            parameters = [attempment_id, attempment_password,attempment_name, attempment_accountType, attempment_photo]
            if validateData(listUsers,attempment_id) == 1:
                error = "Usuario ya existe"
                return render_template("addUser.html", error= error)
            user = classUser()
            addData(user,*parameters)
            addDataList(listUsers, user)
            return redirect(url_for('profileAdmin'))

        return render_template("addUser.html")
    except:
        return render_template("addUser.html", error=error)


@app.route('/createPrescription/',methods=["POST","GET"])
def createPrescription():
    error = ""
    try:
        if request.method == "POST":
            attempment_id = request.form['id']
            attempment_idUser = request.form['idUser']
            attempment_idAnimal = request.form['idAnimal']
            attempment_idDisease = request.form['idDisease']
            attempment_weight = request.form['weight']

            if validateData(listUsers,attempment_idUser) == 0:
                error = "Usuario no existe"
                return render_template("addPrescription.html", error=error)
            if validateData(listAnimals,attempment_idAnimal) == 0:
                error = "Animal no existe"
                return render_template("addPrescription.html", error=error)
            if validateData(listDiseases,attempment_idDisease) == 0:
                error = "Enfermedad no existe"
                return render_template("addPrescription.html", error=error)
            if len(listDoses) == 0:
                error = "No Hay Dosis"
                return render_template("addPrescription.html", error=error)
            attempment_dose = getRecomendedDose(listDoses,attempment_weight, attempment_idAnimal,attempment_idDisease)


            if attempment_dose == 0:
                error = "No Hay Dosis recomendada"
                return render_template("addPrescription.html", error=error)
            parameters = [attempment_id, attempment_idUser, attempment_idAnimal,
                          attempment_idDisease, attempment_weight, attempment_dose]
            prescription = classPresciption()
            addData(prescription, *parameters)
            addDataList(listPrescriptions, prescription)
            if userType[0]=="admin":
                return redirect(url_for('profileAdmin'))

            else:
                return redirect(url_for('profileUser'))

        return render_template("addPrescription.html",originalUserId=userType[1])
    except:
        return render_template("addPrescription.html", error=error)





@app.route('/addAnimal/',methods=["POST","GET"])
def addAnimal():
    error = ''
    try:
        if request.method == "POST":
            attempment_id = request.form['id']
            attempment_name = request.form['name']
            attempment_description = request.form['description']
            attempment_photo = request.form['photo']
            parameters = [attempment_id,attempment_name, attempment_description,attempment_photo]
            if validateData(listAnimals,attempment_id) == 1:
                error = "Animal ya existe"
                return render_template("addAnimal.html", error=error)
            animal = classAnimal()
            addData(animal, *parameters)
            addDataList(listAnimals, animal)
            if userType[0]=="admin":
                return redirect(url_for('profileAdmin'))

            else:
                return redirect(url_for('profileUser'))

        return render_template("addAnimal.html")
    except:
        return render_template("addAnimal.html", error=error)

@app.route('/addDisease/',methods=["POST","GET"])
def addDisease():
    error = ''
    try:
        if request.method == "POST":
            attempment_id = request.form['id']
            attempment_name = request.form['name']
            attempment_description = request.form['description']
            attempment_photo = request.form['photo']
            parameters = [attempment_id, attempment_name, attempment_description, attempment_photo]
            if validateData(listDiseases,attempment_id) == 1:
                error = "Enfermedad ya existe"
                return render_template("addDisease.html", error=error)
            disease = classDisease()
            addData(disease, *parameters)
            addDataList(listDiseases, disease)
            if userType[0]=="admin":
                return redirect(url_for('profileAdmin'))

            else:
                return redirect(url_for('profileUser'))

        return render_template("addDisease.html")
    except:
        return render_template("addDisease.html", error=error)


@app.route('/addMedicine/',methods=["POST","GET"])
def addMedicine():
    error = ''
    try:
        if request.method == "POST":
            attempment_id = request.form['id']
            attempment_name = request.form['name']
            attempment_description = request.form['description']
            attempment_photo = request.form['photo']
            parameters = [attempment_id, attempment_name, attempment_description, attempment_photo]
            if validateData(listMedicines,attempment_id) == 1:
                error = "Medicina ya existe"
                return render_template("addMedicine.html", error=error)
            medicine = classMedicine()
            addData(medicine, *parameters)
            addDataList(listMedicines, medicine)
            if userType[0]=="admin":
                return redirect(url_for('profileAdmin'))

            else:
                return redirect(url_for('profileUser'))

        return render_template("addMedicine.html")
    except:
        return render_template("addMedicine.html", error=error)

@app.route('/createDose/',methods=["POST","GET"])
def createDose():
    error = '.'
    try:
        if request.method == "POST":
            attempment_id = request.form['id']
            attempment_idAnimal = request.form['idAnimal']
            attempment_idMedicine = request.form['idMedicine']
            attempment_idDisease = request.form['idDisease']
            attempment_weightRnage = request.form['weightRange']
            attempment_dose = request.form['dose']

            parameters = [attempment_id, attempment_idAnimal, attempment_idMedicine,
                          attempment_idDisease, attempment_weightRnage, attempment_dose]
            if validateData(listUsers, attempment_idMedicine) == 0:
                error = "Medicamento no existe"
                return render_template("addDose.html", error=error)
            if validateData(listAnimals, attempment_idAnimal) == 0:
                error = "Animal no existe"
                return render_template("addDose.html", error=error)
            if validateData(listDiseases, attempment_idDisease) == 0:
                error = "Enfermedad no existe"
                return render_template("addDose.html", error=error)
            if validateData(listDoses, attempment_dose) == 1:
                error = "Dosis ya existe"
                return render_template("addDose.html", error=error)
            dose = classDose()
            addData(dose, *parameters)
            addDataList(listDoses, dose)
            if userType[0]=="admin":
                return redirect(url_for('profileAdmin'))

            else:
                return redirect(url_for('profileUser'))

        return render_template("addDose.html")
    except:
        return render_template("addDose.html", error=error)



@app.route('/profileUser/',methods=["GET","POST"])
def profileUser():
    if len(userType) ==0:
        return redirect(url_for('loginPage'))
    try:
        if request.method == "POST":
            if request.form['action'] == 'Guardar Cambios':
                insertToDisease()
                inserToAnimal()
                inserToDoses()
                inserToMedicine()
                inserToPrescription()
                inserToUser()

            elif request.form['action'] == 'Cancelar Cambios':
                deleteAllFromLists()
                loadToUser()
                loadToAnimal()
                loadToDisease()
                loadToDoses()
                loadToMedicine()
                loadToPrescription()

                return render_template("profileUser.html")
    except:
        return render_template("profileUser.html")
    return render_template("profileUser.html")


@app.route('/login/',methods=["GET","POST"])
def loginPage():

    if len(listUsers)==0:
        #defaultData()
        loadToUser()
        loadToAnimal()
        loadToDisease()
        loadToDoses()
        loadToMedicine()
        loadToPrescription()
    error = ''
    try:
        if request.method == "POST":
            attempment_username = request.form['username']
            attempment_password = request.form['password']
            parameters = [attempment_username, attempment_password]

            if getUserType(*parameters) == "admin":
                saveCurerntUser("admin",attempment_username)
                return redirect(url_for('profileAdmin'))
            if getUserType(*parameters) == "user":
                saveCurerntUser("user",attempment_username)
                return redirect(url_for('profileUser'))
            else:
                error = "Datos incorrectos por favor intente de nuevo"

        return render_template("login.html",error = error)
    except:
        return render_template("login.html", error = error)

if __name__ == "__main__":

    app.run(debug=True)
