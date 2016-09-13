from flask import Flask, render_template, flash, request, url_for, redirect

from Logic import *
from Globals import *


app = Flask(__name__)

@app.route('/createUser/',methods=["POST","GET"])
def createUser():
    showData()
    error = ""
    try:
        if request.method == "POST":
            attempment_id= request.form['login']
            attempment_password = request.form['password']
            attempment_name = request.form['name']
            attempment_accountType = request.form['accountType']
            attempment_photo = request.form['photo']
            parameters = [attempment_id, attempment_password,attempment_name, attempment_accountType, attempment_photo]
            if validateData(listUsers,attempment_id) == 1:
                error = "Usuario ya existe"
                return render_template("createUser.html", error= error)
            user = classUser()
            addData(user,*parameters)
            addDataList(listUsers, user)
            return render_template("profileAdmin.html")
            showData()
        return render_template("createUser.html")
    except:
        return render_template("createUser.html", error=error)





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
                return render_template("createPrescription.html", error=error)
            if validateData(listAnimals,attempment_idAnimal) == 0:
                error = "Animal no existe"
                return render_template("createPrescription.html", error=error)
            if validateData(listDiseases,attempment_idDisease) == 0:
                error = "Enfermedad no existe"
                return render_template("createPrescription.html", error=error)
            if validateData(listDoses,attempment_dose) == 0:
                error = "Dosis no existe"
                return render_template("createPrescription.html", error=error)
            prescription = classPresciption()
            addData(prescription, *parameters)
            addDataList(listPrescriptions, prescription)
            showData()
        return render_template("createPrescription.html")
    except:
        return render_template("createPrescription.html", error=error)





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
            showData()
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
            showData()
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
            showData()
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
                return render_template("createDose.html", error=error)
            if validateData(listAnimals, attempment_idAnimal) == 0:
                error = "Animal no existe"
                return render_template("createDose.html", error=error)
            if validateData(listDiseases, attempment_idDisease) == 0:
                error = "Enfermedad no existe"
                return render_template("createDose.html", error=error)
            if validateData(listDoses, attempment_dose) == 1:
                error = "Dosis ya existe"
                return render_template("createDose.html", error=error)
            dose = classDose()
            addData(dose, *parameters)
            addDataList(listDoses, dose)
            showData()
        return render_template("createDose.html")
    except:
        return render_template("createDose.html", error=error)




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

                return redirect(url_for('profileAdmin'))
            if getUserType(*parameters) == "user":
                return redirect(url_for('profileUser'))
            else:
                error = "Datos incorrectos por favor intente de nuevo"

        return render_template("login.html",error = error)
    except:
        return render_template("login.html", error = error)

if __name__ == "__main__":

    app.run(debug=True)
