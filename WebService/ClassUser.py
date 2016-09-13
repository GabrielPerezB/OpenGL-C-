class classUser:
    def add(self,id,password,name,accountType,photo):
        self.id = id
        self.password = password
        self.name = name
        self.accountType = accountType
        self.photo = photo

    def getInfo(self):
        print(self.id + " " + self.password + " " + self.name + " " +self.accountType + " " + self.photo)
