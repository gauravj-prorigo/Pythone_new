from abc import ABC,abstractmethod
# class MysqlDatabase:
#     def connect(self):
#         print("Connect to my sql database")

# class App:
#     def __init__(self,database):
#               self.data = database

# Co = App(MysqlDatabase())
# Co.data.connect()                 

class database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MysqlDatabase(database):
    def connect(self):
        print("Connect to mysql database") 
        
class MongoDatabase(database):
    def connect(self):
        print("Connect to mongo database")


class oracalDatabase(database):
    def connect(self):
        print("Connect to oracal database")        
           
class App:
    def __init__(self,databasetyp):
        self.database = databasetyp


app1 = App(MysqlDatabase())
app2 = App(MongoDatabase())

app1.database.connect()
app2.database.connect()
        
