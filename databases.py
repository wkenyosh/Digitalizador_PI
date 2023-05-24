import pymongo
from bson import ObjectId, Int64
from pymongo import mongo_client
from PySide2.QtWidgets import (QMessageBox)

class MongoDB:
    def __init__(self, username, password, database_name):
        self.username = username
        self.password = password
        self.database_name = database_name
        self.client = None
        self.db = None
        
    def connect(self):
        self.client = pymongo.MongoClient(f"mongodb+srv://{self.username}:{self.password}@cluster0.qjb6hbe.mongodb.net/?retryWrites=true&w=majority")
        self.db = self.client[self.database_name]
        
    def close(self):
        self.client.close()
        
    def create_collection_users(self):
        collection_names = self.db.list_collection_names()
        if "users" not in collection_names:
            self.db.create_collection('users')

    def create_collection_clients(self, cpf):
        collection_names = self.db.list_collection_names()
        doc = cpf
        if cpf not in collection_names:
            self.db.create_collection(doc)

        
    def insert_user(self, name, user, password, access):
        user_doc = {'name': name, 'user': user, 'password': password, 'access': access}
        self.db['users'].insert_one(user_doc)

    def insert_client(self, num_coo, cpf, auto_ms, data_venda):
        global doc, document_id
        doc = cpf
        self.client_doc = {'numero_coo': num_coo, 'cpf': cpf, 'Auto_Ms': auto_ms, 'Data_venda': data_venda}
        result = self.db[doc].insert_one(self.client_doc)
        document_id = result.inserted_id
        print(document_id)
        return document_id
        

   
    def insert_pdf(self, pdf, tab_doc):
        # Atualizando o documento na coleção com o novo arquivo PDF
        self.id = {'_id': ObjectId(document_id)}
        self.bin = {'$set': {tab_doc: pdf}  }
        self.db[doc].update_one(self.id, self.bin)
        print(pdf)
        print(tab_doc)
        print("PDF inserido com sucesso!")
    

    def get_doc(self, NUM_coo, CPF, AUTO_ms):
        i = CPF

        if NUM_coo == "null":
            j = int(AUTO_ms)
            x = "Auto_Ms"

        if AUTO_ms == "null":
            j = int(NUM_coo)
            x = "numero_coo"
        print(j,x)
        print(i)
        self.query = {x: j}
        documento = self.db[i].find_one(self.query)
        print(documento)
       
        return documento
          
       
                 
    
    def check_user(self, user, password):
        query = {'user': user, 'password': password}
        result = self.db['users'].find_one(query)
        
        if result:
            return result['access'] 
            
        else:
            return 'sem acesso'
        
   
if __name__ == "__main__":
    mongo = MongoDB('root', 'root', 'digitalizador_pi')
    mongo.connect()
    mongo.create_collection_users()
    mongo.create_collection_clients()
    mongo.insert_user()
    mongo.insert_client()
    mongo.insert_pdf()
    mongo.get_doc()
    autenticado = mongo.check_user()
    print(autenticado)
    mongo.close()
