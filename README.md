# RestFull-CRUD-API-with-Python-MongoDB-and-Docker
A project that uses Python Flask and pymongo to complete CRUD operations and is deployed on Docker. It is made as an assignment and uses data with 5000 entries as default collection. 
---

## `How to deploy the project on Docker`
 * Open the command promt or terminal.
 * Change Directory to the project directory.
 * Note : Docker Daemon must be running for next steps.
 * Run command `docker-compose build`, this will build the containers and prepare them to run the project.
 * Run command `docker-compose up`, this will start the process and containers.
 * In case of any error, check logs with `docker logs <Container Name>`
 * Use Postman or Curl to test the APIs with `http://localhost:5000/mongodb` as request URL.
---
## `Running project with only MongoDB on Docker`
 * Open the command promt or terminal.
 * Note : Docker Daemon must be running for next steps.
 * Run command `docker pull mongo`, this will pull the image mongo from Docker Hub.
 * Run command `docker create -it --name MongoContainer -p 5000:27017 mongo`, this will make a container MongoContainer and pulling image mongo on given port.
 * Run command `docker start MongoContainer` to start it.
 * Change Client in python code to `mongodb://localhost:27017/` one. Do note there's two of them and you have to change both of them.
 * You can see the MongoDB database and collections and access them through MongoDB Campass, just paste `mongodb://localhost:27017/` in connection string.
 * Use Postman or Curl to test the APIs with `http://localhost:5000/mongodb` as request URL.
---
## `API methods with Fucntions`
| Method  | Fuction | Description |
| ------------- | ------------- | ------------- |
| GET  | Reads  | Read data from given collection and gives it as response, can use filter keyword to make constraints and count keyword to get count of rows  |
| POST  | Write  | Inserts data into given collection, can insert just one or many depending on the data |
| PUT  | Update  | Updates data in given collection, uses Filter keyword as old data and DataToBeUpdated keyword as new data  |
| Delete  | Delete | Deletes data from given collection, deletes all records that matches Filter  |
| PATCH  | Distinct/list_unique_brands | Reads distinct data from given collection, uses Filter keyword to take field input / Bonus Task - How many unique brands are present in the collection?  |
| COPY  | count_discounted_products | Bonus Task - How many products have a discount on them?  |
| HEAD  | count_high_offer_price | Bonus Task - How many products have offer price greater than 300?  |
| OPTIONS  | count_high_discount | Bonus Task - How many products have discount % greater than 30%?  |
---
## `API Inputs and Outputs`
In Postman or Curl or any other alternative.
* Step 1: Paste `http://localhost:5000/mongodb` in URL.
* Step 2: Select an API Method of choice from previous table.
* Step 3: Select Body->Raw->Json format.
* Step 4: Write valid code snippet below.
* Step 5: Click Send.
----------------------------
1.`GET Method`: Reading all data in the collection.

  - This is the default database and collection in project, the project works for different database and collection too.
 ``` 
  {
  "database": "ShivanshDB",
  "collection": "E-Commerce"
  }
  ```
  ![Image of Yaktocat](https://github.com/shivanshp16/RestFull-CRUD-API-with-Python-MongoDB-and-Docker/blob/main/Read_GET.jpg)
  
  - `GET Method` with filter constraint, will only show records where brand name is jellycat.
  ```
   {
  "database": "ShivanshDB",
  "collection": "E-Commerce",
  "Filter": {
    "brand_name": "jellycat"
  }
  }
  ```
  
  - `GET Method` with filter and count constraint, will give count of records.
  ```
   {
  "database": "ShivanshDB",
  "collection": "E-Commerce",
  "Filter": {
    "brand_name": "jellycat"
  }
  "count":""
  }
  ```
  
2.`POST Method`: Inserts data in the collection. 

  - The document keyword is required to insert data here.
  ```
  {
  "database": "ShivanshDB",
  "collection": "E-Commerce",
  "Document": {
    "name": "Playstation", 
    "brand_name": "Sony", 
    "regular_price_value": 10000, 
    "offer_price_value": 10000, 
    "currency": "INR", 
    "classification_l1": "Teen", 
    "classification_l2": "Electronic", 
    "classification_l3": "", 
    "classification_l4": "", 
    "image_url": ""
  }
  }
  ```
  
3.`PUT Method`: Updates already present data in collection
 
 - The filter keyword identifies the old data and DataToBeUpdated keyword is for new data here.
 ```
 {
  "database": "ShivanshDB",
  "collection": "E-Commerce",
  "Filter": {
    "brand_name": "Sony"
  },
  "DataToBeUpdated": {
    "name": "X Box", 
    "brand_name": "Microsoft", 
    "regular_price_value": 12000, 
    "offer_price_value": 11000
  }
  }
  ```
  
4.`Delete Method`: Updates already present data in collection

  - The filter keyword identifies the records that matches it and deletes all of them.
  ```
   {
  "database": "ShivanshDB",
  "collection": "E-Commerce",
  "Filter": {
    "brand_name": "Microsoft"
  }
  }
  ```
  
5.`PATCH Method`: Reads distint records from given field.

  - Bonus Task - How many unique brands are present in the collection?
  - Here, distinct keyword takes a field as input and returns the unique records in that field.
 

   ```
   {
  "database": "ShivanshDB",
  "collection": "E-Commerce",
  "Distinct": "brand_name"
  }
  ```
 
6.`COPY Method`: Bonus Task - How many products have a discount on them?

  - This method will work only for default collection or a collection with fields regular_price_value and offer_price_value.
  ```
   {
  "database": "ShivanshDB",
  "collection": "E-Commerce"
  }
  ```
  
  -This solution to this task could be achieved by `GET Method` too.
  ```
  {
  "database": "Shivansh",
  "collection": "E-Commerce",
  "Filter": {
    "$expr":{"$gt":["$regular_price_value", "$offer_price_value"]}
  },
  "count":""
  }
  ```
  
7.`HEAD Method`: Bonus Task - How many products have offer price greater than 300?

  - This method will work only for default collection or a collection with field offer_price_value.
  ```
   {
  "database": "ShivanshDB",
  "collection": "E-Commerce"
  }
  ```
  
  -This solution to this task could be achieved by `GET Method` too.
  ```
  {
  "database": "Shivansh",
  "collection": "E-Commerce",
  "Filter": {
    'offer_price_value' : {'$gt' : 300 }}
  },
  "count":""
  }
  ```
  
8.`OPTIONS Method`: Bonus Task - How many products have discount % greater than 30%?

  - This method will work only for default collection or a collection with field regular_price_value and offer_price_value.
  ```
   {
  "database": "ShivanshDB",
  "collection": "E-Commerce"
  }
  ```
