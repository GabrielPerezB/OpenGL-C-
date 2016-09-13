from flask import Flask, render_template, flash, request, url_for, redirect

from Logic import *
from Globals import *


app = Flask(__name__)

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
            return render_template("profileAdmin.html",error = "Eliminado")
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
                return render_template("profileAdmin.html", error="Eliminado")
            else:
                return render_template("profileUser.html", error="Eliminado")
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
                return render_template("profileAdmin.html", error="Eliminado")
            else:
                return render_template("profileUser.html", error="Eliminado")
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
                return render_template("profileAdmin.html", error="Eliminado")
            else:
                return render_template("profileUser.html", error="Eliminado")
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
                return render_template("profileAdmin.html", error="Eliminado")
            else:
                return render_template("profileUser.html", error="Eliminado")
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
                return render_template("profileAdmin.html", error="Eliminado")
            else:
                return render_template("profileUser.html", error="Eliminado")
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
            if userType[0]=="admin":
                return render_template("profileAdmin.html",error = "Agregado")
            else:
                return render_template("profileUser.html",error = "Agregado")
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
            if userType[0]=="admin":
                return render_template("profileAdmin.html",error = "Modificado")
            else:
                return render_template("profileUser.html",error = "Modificado")
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
            if userType[0]=="admin":
                return render_template("profileAdmin.html",error = "Modificado")
            else:
                return render_template("profileUser.html",error = "Modificado")
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
            if userType[0]=="admin":
                return render_template("profileAdmin.html",error = "Modificado")
            else:
                return render_template("profileUser.html",error = "Modificado")
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
            attempment_dose = request.form['dose']

            parameters = [attempment_id,attempment_idUser, attempment_idAnimal,
                          attempment_idDisease,attempment_weight,attempment_dose]

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
            if validateData(listDoses,attempment_dose) == 0:
                error = "Dosis no existe"
                return render_template("updatePrescription.html", originalId=objectToUpdate[0].id,
                                     originaluserId=objectToUpdate[0].userId,
                                     originalAnimalId=objectToUpdate[0].animalId,
                                     originalDiseaseId=objectToUpdate[0].diseaseId,
                                     originalWeight=objectToUpdate[0].weight,
                                     originalDoseId=objectToUpdate[0].doseId,
                                     error = error)
            deleteData(listPrescriptions,attempment_id)
            prescription = classPresciption()
            addData(prescription, *parameters)
            addDataList(listPrescriptions, prescription)
            if userType[0]=="admin":
                return render_template("profileAdmin.html",error = "Modificado")
            else:
                return render_template("profileUser.html",error = "Modificado")
        return render_template("updatePrescription.html", originalId=objectToUpdate[0].id,
                                     originaluserId=objectToUpdate[0].userId,
                                     originalAnimalId=objectToUpdate[0].animalId,
                                     originalDiseaseId=objectToUpdate[0].diseaseId,
                                     originalWeight=objectToUpdate[0].weight,
                                     originalDoseId=objectToUpdate[0].doseId,
                                     error = error)
    except:
        return render_template("updatePrescription.html", error=error)





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
            return render_template("profileAdmin.html",error = "Modificado")
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
            return render_template("profileAdmin.html",error = "Agregado")
        return render_template("addUser.html")
    except:
        return render_template("addUser.html", error=error)


@app.route('/createPrescription/',methods=["POST","GET"])
def createPrescription():
    error = '.'
    try:
        if request.method == "POST":
            attempment_id = request.form['id']
            attempment_idUser = request.form['idUser']
            attempment_idAnimal = request.form['idAnimal']
            attempment_idDisease = request.form['idDisease']
            attempment_weight = request.form['weight']
            attempment_dose = request.form['dose']

            parameters = [attempment_id,attempment_idUser, attempment_idAnimal,
                          attempment_idDisease,attempment_weight,attempment_dose]
            if validateData(listUsers,attempment_idUser) == 0:
                error = "Usuario no existe"
                return render_template("addPrescription.html", error=error)
            if validateData(listAnimals,attempment_idAnimal) == 0:
                error = "Animal no existe"
                return render_template("addPrescription.html", error=error)
            if validateData(listDiseases,attempment_idDisease) == 0:
                error = "Enfermedad no existe"
                return render_template("addPrescription.html", error=error)
            if validateData(listDoses,attempment_dose) == 0:
                error = "Dosis no existe"
                return render_template("addPrescription.html", error=error)
            prescription = classPresciption()
            addData(prescription, *parameters)
            addDataList(listPrescriptions, prescription)
            if userType[0]=="admin":
                return render_template("profileAdmin.html",error = "Agregado")
            else:
                return render_template("profileUser.html",error = "Agregado")
        return render_template("addPrescription.html")
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
                return render_template("profileAdmin.html",error = "Agregado")
            else:
                return render_template("profileUser.html",error = "Agregado")
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
                return render_template("profileAdmin.html",error = "Agregado")
            else:
                return render_template("profileUser.html",error = "Agregado")
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
                return render_template("profileAdmin.html",error = "Agregado")
            else:
                return render_template("profileUser.html",error = "Agregado")
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
                return render_template("profileAdmin.html",error = "Agregado")
            else:
                return render_template("profileUser.html",error = "Agregado")
        return render_template("addDose.html")
    except:
        return render_template("addDose.html", error=error)




@app.route('/profileAdmin/')
def profileAdmin():
    error = ''
    try:
        if request.method == "POST":
            attempment_createUser = request.form['createUser']

            if  attempment_createUser == "createUser":
                return redirect(url_for('createUser'))

            else:
                error = "Por favor intente de nuevo"

        return render_template("profileAdmin.html")
    except:
        return render_template("profileAdmin.html",error = error)




@app.route('/profileUser/')
def profileUser():
    return render_template("profileUser.html")

@app.route('/login/',methods=["GET","POST"])
def loginPage():

    if len(listUsers)==0:
        defaultData()
    error = ''
    try:

        if request.method == "POST":
            attempment_username = request.form['username']
            attempment_password = request.form['password']
            parameters = [attempment_username, attempment_password]

            if getUserType(*parameters) == "admin":
                saveCurerntUser("admin")
                return redirect(url_for('profileAdmin'))
            if getUserType(*parameters) == "user":
                saveCurerntUser("user")
                return redirect(url_for('profileUser'))
            else:
                error = "Datos incorrectos por favor intente de nuevo"

        return render_template("login.html",error = error)
    except:
        return render_template("login.html", error = error)

if __name__ == "__main__":

    app.run(debug=True)
