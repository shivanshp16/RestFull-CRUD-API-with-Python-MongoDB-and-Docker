# RestFull-CRUD-API-with-Python-MongoDB-and-Docker
A project that uses Python Flask and pymongo to complete CRUD operations and is deployed on Docker. It is made as an assignment and uses data with 5000 entries as default collection. 
---
# `How to deploy the project on Docker`
---
 * Open the command promt or terminal.
 * Change Directory to the project directory.
 * Note : Docker Daemon must be running for next steps.
 * Run command `docker-compose build`, this will build the containers and prepare them to run the project.
 * Run command `docker-compose up`, this will start the process and containers.
 * In case of any error, check logs with `docker logs <Container Name>`
 * Use Postman or Curl to test the APIs with `http://localhost:5000/mongodb` as request URL.
---
# `Running project with only MongoDB on Docker`
---
 * Open the command promt or terminal.
 * Note : Docker Daemon must be running for next steps.
 * Run command `docker create -it --name MongoContainer -p 5000:27017 mongo`, this will make a container MongoContainer and pulling image mongo on given port.
 * Run command `docker start MongoContainer` to start it.
 * Change Client in python code to `mongodb://localhost:27017/` one. Do note there's two of them and you have to change both of them.
 * You can see the MongoDB database and collections and access them through MongoDB Campass, just paste `mongodb://localhost:27017/` in connection string.
 * Use Postman or Curl to test the APIs with `http://localhost:5000/mongodb` as request URL.
---
# `API methods with Fucntions`
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
# `
