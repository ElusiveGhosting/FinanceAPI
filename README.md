# FinanceAPI using Flask-RESTful

This is API built using Flask-Restful library with cloud-based MongoDB backend for data storage. It supports CRUD( Create Read Update Delete) for users and their financial data for easy management of individual finances.



# Setup

1. Clone the repository

           $ git clone https://github.com/ElusiveGhosting/FinanceAPI.git

2. Change in the code directory

           $ cd FinanceAPI/

3. Change into "flask-restful" branch

           $ git checkout flask-restful

4. DB setup via MONGODB (Account required - Free Tier: https://cloud.mongodb.com/)

           a. Create a cluster which will host your DB
           b. Create database "myapi"
           c. Create 2 collections inside the created DB called "finance" and "user"
           d. Create access credentials
           e. Add access from anywhere for the database using the Network Access tab to prevent access getting blocked

5. Setup environment Variables to store DB credentials:

           a. Get connection string to configure environment variables by clicking on connect in Cluster Dashboard in MongoDB
           b. Connection URL will be like "mongodb+srv://<clustername>:<password>@<clustername>.redacted.mongodb.net?retryWrites=true&w=majority"
           c. Split them into 3 parts as mentioned below:
                            connectionURL1 : mongodb+srv://<clustername>:
                            MONGODB_PASSWORD : password
                            connectionURL2 : @<clustername>.redacted.mongodb.net?retryWrites=true&w=majority
           d. run export command to set environment variables used for DB connection
           e. run $ export MONGODB_PASSWORD="<password>"
           f. $ export connectionURL1="mongodb+srv://<clustername>:
           g. $ export connectionURL2="@<clustername>.equoy0q.mongodb.net/?retryWrites=true&w=majority  


6. Deployment

           $ python app.py


7. Testing Deployment :

   Postman :

          a. Import request collection to Postman by 	loading FinanceDataTracker.postman_collection.json via Postman.
             reference : https://learning.postman.com/docs/getting-started/importing-and-exporting-data/
          b. Run the request present in collection with existing/own data

   Curl :

    		  $ curl -i http://127.0.0.1:5000
    		    {"hello":"World","DB_Connection_Status":"Success"}
