class User:
    def __init__(self, username, password):
        self.uname=username
        self.password=password
        
class Buyer(User):
    def __init__(self, username, password, id, address):
        super().__init__(username, password)
        self.id=id
        self.address=address
        
    def printinfo(self):
        print("Username: "+self.uname+"\nPassword: "+self.password+"\nID: "+str(self.id)+"\nAddress: "+self.address)
        
p=Buyer("narges","1234",123,"saveh")
p.printinfo()