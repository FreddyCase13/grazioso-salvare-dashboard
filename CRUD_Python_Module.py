
from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
       # USER = 'aacuser' 
       # PASS = 'LincolnMikala!3' 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        
        # Build the Mongo URI using the provided credentials
        mongo_uri = "mongodb://%s:%s@%s:%d" % (username, password, HOST, PORT)
        
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient(mongo_uri)
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
    """
        Returns the next available record number.
        referencing https://www.mongodb.com/docs/languages/python/pymongo-driver/current/crud/query/count/
    """
    def get_next_record_number(self):
        count = self.collection.count_documents({})
        return count + 1
        
    # Complete this create method to implement the C in CRUD. 
    """
        Insert a new document into the animals collection.
        referencing https://www.mongodb.com/docs/languages/python/pymongo-driver/current/crud/insert/
    """
    def create(self, data):
        if data is not None:
            #if works, returns True
            try:
                result = self.database.animals.insert_one(data)  # data should be dictionary    
                return True
            #returns False if not true
            except:
                return False
        else: 
            raise Exception("Nothing to save, because data parameter is empty") 

    # Create method to implement the R in CRUD.
    """
        Read documents from the animals collection using find().
        referencing https://www.mongodb.com/docs/languages/python/pymongo-driver/current/crud/query/find/
    """
    def read(self, query):
        if query is not None:
            cursor = self.database.animals.find(query)
            #return result is in a list
            return list(cursor)
        else:
            #returns empty list when unsucessful
            return[]
        
    # Update method to implement the U in CRUD.
    """
        Update document(s) in the animals collection using update_many().
        referencing https://www.mongodb.com/docs/languages/python/pymongo-driver/current/crud/update/
    """
    def update(self, query, new_values):
        if query is not None:
            try:
                # apply $set to modify matching documents
                result = self.collection.update_many(query, {"$set": new_values})
                # return number of modified documents
                return result.modified_count
            except Exception:
                # return 0 when update fails
                return 0
        else:
            raise Exception("Query parameter is empty")
        
        
    # Delete method to implement the D in CRUD.
    """
        Delete document(s) from the animals collection using delete_many().
        referencing https://www.mongodb.com/docs/languages/python/pymongo-driver/current/crud/delete/
    """
    def delete(self, query):
        if query is not None:
            try:
                # delete all documents matching the query
                result = self.collection.delete_many(query)
                # return number of deleted documents
                return result.deleted_count
            except Exception:
                # return 0 when delete fails
                return 0
        else:
            raise Exception("Query parameter is empty")

