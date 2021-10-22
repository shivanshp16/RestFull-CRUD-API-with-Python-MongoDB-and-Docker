#Importing required packages
from flask import Flask, request, json, Response
from pymongo import MongoClient, collection
import logging as log
import json

#Intializing Flask
app = Flask(__name__)       

#A function to import the required collection
def makecollection():
    #Making a mongodb server connection
    '''client = MongoClient("mongodb://localhost:27017/")'''   #When server is hosting locally
    client = MongoClient('mongodb://mongo:27017/')             #When using docker-compose
    mydb = client["ShivanshDB"]                                #Creating a database
    coll = mydb["E-Commerce"]                                  #Creating a collection

    #Importing required data
    with open('data.json') as file:
        file_data = json.load(file)
    coll.insert_many(file_data)


class MongoAPI:
    def __init__(self, data):
        log.basicConfig(level=log.DEBUG, format='%(asctime)s %(levelname)s:\n%(message)s\n')
        '''self.client = MongoClient("mongodb://localhost:27017/")'''
        self.client = MongoClient('mongodb://mongo:27017/')  

        #Getting database and collection information from user
        database = data['database']                         
        collection = data['collection']
        cursor = self.client[database]
        self.collection = cursor[collection]
        self.data = data
    
    #Function for get method, fetches data from collection for user
    def read(self):
        log.info('Reading All Data')
        if 'Filter' in str(self.data):                      #A constraint to filter data
            filt = self.data['Filter']                      #fetching data from filter
            documents = self.collection.find(filt)          #finding data matching the filter
        else:
            documents = self.collection.find()              #To get all the data in collection
        if 'count' in str(self.data):                       #A constraint to give only count of tuples
            output=documents.count()
        else:
            output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output

    #Function for Post method, inserts data into collection
    def write(self, data):
        log.info('Writing Data')
        new_document = data['Document']                         #fetching data from document
        response = self.collection.insert_many(new_document)    #Inserting new data into collection
        output = {'Status': 'Successfully Inserted',
                  'Document_ID': str(response.inserted_id)}
        return output

    #Function for put method, updates existing data in collection uses fliter constraint
    def update(self):
        log.info('Updating Data')
        filt = self.data['Filter']                                      #fetching data meant to be updated
        updated_data = {"$set": self.data['DataToBeUpdated']}           #fetching data that'll replace old one
        response = self.collection.update_many(filt, updated_data)      #updating data in collection
        output = {'Status': 'Successfully Updated' if response.modified_count > 0 else "Nothing was updated."}
        return output

    #Function for put method, deletes existing data in collection uses fliter constraint
    def delete(self, data):
        log.info('Deleting Data')                                       
        filt = data['Filter']                                          
        response = self.collection.delete_many(filt)                    #Deleting data from collection that matches filter
        output = {'Status': 'Successfully Deleted' if response.deleted_count > 0 else "Document not found."}
        return output

    #Function for patch method, fetches distinct values
    def unique(self):
        log.info('Reading unique values')
        filt = self.data['Distinct']                                    #fetching distinct row
        documents = self.collection.distinct(filt)                      #finding unique data in collection
        return documents

    def discount(self):
        log.info('Finding count of products with discount')

#Endpoints or Routes for above functions

#route to check if server is running
@app.route('/')
def base():
    return Response(response=json.dumps({"Status": "UP"}),              #Test message
                    status=200,
                    mimetype='application/json')

#Method for read fuction, endpoint or route for GET method
@app.route('/mongodb', methods=['GET'])                                 
def mongo_read():
    data = request.json                                                                              #Getting query in json format
    if data is None or data == {}:                                                                   #Cheking if the query is valid or correct
        return Response(response=json.dumps({"Error": "Please provide connection information"}),     #Error in case query is invalid
                        status=400,                                                                  
                        mimetype='application/json')
    obj1 = MongoAPI(data)                                                                            #Making an object of MongoAPI with data as argumnent
    response = obj1.read()
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')

#Method for write fuction, endpoint or route for POST method
@app.route('/mongodb', methods=['POST'])
def mongo_write():
    data = request.json
    if data is None or data == {} or 'Document' not in data:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400,
                        mimetype='application/json')
    obj1 = MongoAPI(data)
    response = obj1.write(data)
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')

#Method for update fuction, endpoint or route for PUT method
@app.route('/mongodb', methods=['PUT'])
def mongo_update():
    data = request.json
    if data is None or data == {} or 'Filter' not in data:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400,
                        mimetype='application/json')
    obj1 = MongoAPI(data)
    response = obj1.update()
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')

#Method for delete fuction, endpoint or route for DELETE method
@app.route('/mongodb', methods=['DELETE'])
def mongo_delete():
    data = request.json
    if data is None or data == {} or 'Filter' not in data:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400,
                        mimetype='application/json')
    obj1 = MongoAPI(data)
    response = obj1.delete(data)
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')

#Method for unique fuction, endpoint or route for PATCH method
@app.route('/mongodb', methods=['PATCH'])
def mongo_distinct():
    data = request.json
    if data is None or data == {} or 'Distinct' not in data:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400,
                        mimetype='application/json')
    obj1 = MongoAPI(data)
    response = obj1.unique()
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')

if __name__ == '__main__':
    makecollection()                                #calling makecollection function to make required collection at the start of execution
    app.run(debug=True, port=5000, host='0.0.0.0')  #Exposing port and host