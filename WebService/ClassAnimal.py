class classAnimal:

    def add(self,id,name,description,photo):
        self.id = id
        self.name = name
        self.description = description
        self.photo = photo

    def getInfo(self):
        print(self.id+" "+self.name + " " + self.description + " " + self.photo)
