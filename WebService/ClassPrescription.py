class classPresciption:
    def add(self, Id,userId,animalId,diseaseId,weight,doseId):
        self.id = Id
        self.userId = userId
        self.animalId = animalId
        self.diseaseId = diseaseId
        self.weight = weight
        self.doseId = doseId

    def getInfo(self):
        print(self.id + " " + self.userId + " " + self.animalId + " " +
              self.diseaseId + " " + self.weight + " " + self.doseId)
