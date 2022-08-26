# FinanceAPI using Flask-RESTful

1. Clone the repository

           $ git clone

2. Change in the code directory

           $ cd https://github.com/ElusiveGhosting/FinanceAPI.git

3. Change into "flask-restful" branch

           $ git checkout flask-restful

4. DB setup via MONGODB (Account required - Free Tier: https://cloud.mongodb.com/)

           a. Create database "myapi"
           b. Create 2 collections inside the created DB called "finance" and "user"
           c. Create access credentials
           d. Add access from anywhere for the database using the Network Access tab to prevent access getting blocked

5. Deployment

           $ python app.py


6. Testing Deployment :

   Postman :

          a. Import request collection to Postman by 	loading FinanceDataTracker.postman_collection.json via Postman.
             reference : https://learning.postman.com/docs/getting-started/importing-and-exporting-data/
          b. Run the request present in collection with existing/own data

   Curl :

    		  $ curl -i http://127.0.0.1:5000
    		    {'hello': 'world'}
