class classDose:
    def add(self, Id,animalId,medicineId,diseaseId,weightRange,dose):
        self.id = Id
        self.animalId = animalId
        self.medicineId = medicineId
        self.diseaseId = diseaseId
        self.weightRange = weightRange
        self.dose = dose

    def getInfo(self):
        print(self.id + " " + self.animalId + " " + self.medicineId+ " " +
              self.diseaseId+ " " + self.weightRange+ " " + self.dose)
