import mysql.connector

'''
Connect DB
'''
conn =mysql.connector.connect(user='root',password='root',host='localhost',database='Veterinaria')
mycursor = conn.cursor()
#mycursor.execute("CREATE DATABASE Veterinaria")
#mycursor.execute("USE Veterinaria")

'''
Consult INSERT_DB
'''

def insertAnimal(*args):
    try:
        mycursor.execute("""INSERT INTO animal (idAnimal,nombre,descripcion,foto)
         VALUES (%i,'%s','%s','%s')""" % (args[0], args[1], args[2], args[3]))
        print("Se inserto un animal")
        conn.commit()
    except:
        try:
            mycursor.execute("""UPDATE animal SET nombre='%s',descripcion='%s', foto='%s' WHERE idAnimal=%i""" % ( args[1], args[2], args[3], args[0]))
            conn.commit()
            print("Modificado")
        except:
            print("Ese datos ya esta ingresado en la DB")



def insertDisease(*args):
    try:
        mycursor.execute("""INSERT INTO enfermedad (idEnfermedad,nombre,descripcion,foto) VALUES (%i,'%s','%s','%s')""" % (args[0], args[1], args[2], args[3]))
        print("Se inserto una enfermedad")
        conn.commit()
    except:
        try:
            mycursor.execute("""UPDATE enfermedad SET nombre='%s',descripcion='%s', foto='%s' WHERE idEnfermedad=%i""" % ( args[1], args[2], args[3], args[0]))
            conn.commit()
            print("Modificado")
        except:
            print("Ese datos ya esta ingresado en la DB")



def insertMedicine(*args):
    try:
        mycursor.execute(""" INSERT INTO medicamento (idMedicamento,nombre,descripcion,foto) VALUES (%i,'%s','%s','%s')""" %(args[0], args[1], args[2], args[3]))
        print("Se inserto un medicamento")
        conn.commit()
    except:
        try:
            mycursor.execute("""UPDATE medicamento SET nombre='%s',descripcion='%s', foto='%s' WHERE idMedicamento=%i""" % ( args[1], args[2], args[3], args[0]))
            conn.commit()
            print("Modificado")
        except:
            print("Ese datos ya esta ingresado en la DB")

def insertUser(*args):

    try:
        mycursor.execute(""" INSERT INTO usuario (idUsuario,pass,name,permiso,foto) VALUES (%i,'%s','%s','%s','%s')""" %(args[0], args[1], args[2], args[3], args[4]))
        print("Se ingreso un usuario")
        conn.commit()
    except:
        try:
            mycursor.execute("""UPDATE usuario SET nombre='%s', pass = '%S', name='%s',permiso='%s', foto='%s' WHERE idUsuario=%i""" % ( args[1], args[2], args[3], args[4], args[0]))
            conn.commit()
            print("Modificado")
        except:
            print("Ese datos ya esta ingresado en la DB")


def insertDoses(*args):

    try:
        mycursor.execute(""" INSERT INTO dosis (idDosis,animal,medicamento,enfermedad,rangoPeso,dosis) VALUES (%i,%i,%i,%i,'%s','%s')""" %(args[0], args[1], args[2], args[3], args[4],args[5]))
        print("Se inserto una dosis")
        conn.commit()
    except:
        try:
            mycursor.execute("""UPDATE dosis SET animal='%s', medicamento = '%S', enfermedad='%s',rangoPeso='%s', dosis='%s' WHERE idDosis=%i""" % ( args[1], args[2], args[3], args[4], args[5], args[0]))
            conn.commit()
            print("Modificado")
        except:
            print("Ese datos ya esta ingresado en la DB")

def insertPrescription(*args):

    try:
        mycursor.execute(""" INSERT INTO prescripcion (idPrescripcion,usuario,animal,enfermedad,peso,dosis) VALUES (%i,%i,%i,%i,'%s',%i)""" %(args[0], args[1], args[2], args[3], args[4],args[5]))
        print("Se inserto una prescripcion")
        conn.commit()
    except:
        try:
            mycursor.execute("""UPDATE prescripcion SET usuario='%s', animal = '%S', enfermedad='%s',peso='%s', dosis='%s' WHERE idPrescripcion=%i""" % ( args[1], args[2], args[3], args[4], args[5], args[0]))
            conn.commit()
            print("Modificado")
        except:
            print("Ese datos ya esta ingresado en la DB")


'''
Consult SELECT_DB
'''


def loadUsers():
    try:
        mycursor.execute(""" SELECT * FROM usuario""")
        mylist = mycursor.fetchall()
        return mylist
    except:
        print("No hay Users en la DB")
def loadAnimals():
    try:
        mycursor.execute(""" SELECT * FROM animal""")
        mylist = mycursor.fetchall()
        return mylist
    except:
        print("No hay Animals en la DB")

def loadDiseases():
    try:
        mycursor.execute(""" SELECT * FROM enfermedad""")
        mylist = mycursor.fetchall()
        return mylist
    except:
        print("No hay Disease en la DB")

def loadMedicine():
    try:
        mycursor.execute(""" SELECT * FROM medicamento""")
        mylist = mycursor.fetchall()
        return mylist
    except:
        print("No hay medicinas en la DB")

def loadDoses():
    try:
        mycursor.execute(""" SELECT * FROM dosis""")
        mylist = mycursor.fetchall()
        return mylist
    except:
        print("No hay Doses en la DB")

def loadPrescription():
    try:
        mycursor.execute(""" SELECT * FROM prescripcion""")
        mylist = mycursor.fetchall()
        return mylist
    except:
        print("No hay Prescriptiones en la DB")



'''
Consult DELETE_DB

value = int(123)
mycursor.execute("DELETE FROM animal WHERE idAnimal=%i"% value)
'''
def deleteAnimal(lista):
    mycursor.execute(""" SELECT * FROM animal""")
    mylist = mycursor.fetchall()
    for i in mylist:
        found =0
        for element in lista:
            if i[0]  == element:
                found = 1
        if found == 0:
            try:
                mycursor.execute("DELETE FROM animal WHERE idAnimal=%i" % i[0])
            except:
                print("No se pudo eliminar")

def deleteDisease(lista):
    mycursor.execute(""" SELECT * FROM enfermedad""")
    mylist = mycursor.fetchall()
    for i in mylist:
        found =0
        for element in lista:
            if i[0]  == element:
                found = 1
        if found == 0:
            try:
                mycursor.execute("DELETE FROM enfermedad WHERE idEnfermedad=%i" % i[0])
            except:
                print("No se pudo eliminar")


def deleteDose(lista):
    mycursor.execute(""" SELECT * FROM dosis""")
    mylist = mycursor.fetchall()
    for i in mylist:
        found =0
        for element in lista:
            if i[0]  == element:
                found = 1
        if found == 0:
            try:
                mycursor.execute("DELETE FROM dosis WHERE idDosis=%i" % i[0])
            except:
                print("No se pudo eliminar")

def deleteMedicine(lista):
    mycursor.execute(""" SELECT * FROM medicamento""")
    mylist = mycursor.fetchall()
    for i in mylist:
        found =0
        for element in lista:
            if i[0]  == element:
                found = 1
        if found == 0:
            try:
                mycursor.execute("DELETE FROM medicamento WHERE idMedicamento=%i" % i[0])
            except:
                print("No se pudo eliminar")

def deletePrescription(lista):
    mycursor.execute(""" SELECT * FROM prescripcion""")
    mylist = mycursor.fetchall()
    for i in mylist:
        found =0
        for element in lista:
            if i[0]  == element:
                found = 1
        if found == 0:
            try:
                mycursor.execute("DELETE FROM prescripcion WHERE idPrescripcion=%i" % i[0])
            except:
                print("No se pudo eliminar")
def deleteUser(lista):
    mycursor.execute(""" SELECT * FROM usuario""")
    mylist = mycursor.fetchall()
    for i in mylist:
        found =0
        for element in lista:
            if i[0]  == element:
                found = 1
        if found == 0:
            try:
                mycursor.execute("DELETE FROM usuario WHERE idUsuario=%i" % i[0])
            except:
                print("No se pudo eliminar")

'''
Consult UPDATE_DB
'''

#mycursor.execute("UPDATE usuario SET foto = 'Fotico' WHERE id=2")




