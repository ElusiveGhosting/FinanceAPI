from flask import Flask,request
from flask_restful import Resource , Api
from db import mongodb_password,connectionURL1,connectionURL2,initialiseMongoClient


app= Flask(__name__)
api=Api(app)
DBClient=initialiseMongoClient(connectionURL1,mongodb_password,connectionURL2)

class User(Resource):
    def get(self,username):
        result_count=DBClient.myapi.user.count_documents({"username":username})
        if result_count !=0:
            result=DBClient.myapi.user.find_one({"username":username})
            del result["_id"]
            return {"message":"User present","details":result}
        else:
            return {"error":"User doesn't exist"},404

    def post(self,username):
        result_count=DBClient.myapi.user.count_documents({"username":username})
        if result_count ==0:
            data=request.json
            data["username"]=username
            result=DBClient.myapi.user.insert_one(data)
            return {"message":"User created","details":{"username":username}}
        else:
            return {"error":"User already exist"},404

    def put(self,username):
        result_count=DBClient.myapi.user.count_documents({"username":username})
        if result_count !=0:
            data=request.json
            result=DBClient.myapi.user.find_one_and_update( {'username': username}, {'$set': data})
            if result is not None:
                del result["_id"]
                return {"message":"User updated","old_details":result}
            else:
                return {"message":"Unable to update User from DB"},501
        else:
            return {"error":"User doesn't exist"},404


    def delete(self,username):
        result_count=DBClient.myapi.user.count_documents({"username":username})
        if result_count !=0:
            result=DBClient.myapi.user.delete_one({"username":username})
            if result.deleted_count >0:
                return {"message":"User deleted","details":{"username":username}}
            else:
                return {"message":"Unable to delete User from DB"},501
        else:
            return {"error":"User doesn't exist"},404

class Finance(Resource):
    def get(self,username):
        result_count=DBClient.myapi.user.count_documents({"username":username})
        if result_count !=0:
            data_count=DBClient.myapi.finance.count_documents({"username":username})
            if data_count ==1:
                result=DBClient.myapi.finance.find_one({"username":username})
                del result["_id"]
                return {"message":"User's Financial data retreived","details":result},200
            else:
                return {"message":"User's Financial data doesn't exist"},404
        else:
            return {"error":"User doesn't exist"},404

    def post(self,username):
        result_count=DBClient.myapi.user.count_documents({"username":username})
        if result_count == 1:
            data=request.json
            data_flag=DBClient.myapi.finance.count_documents({"username":username})
            if data_flag==1:
                Finance.put(request,username)
                return {"message":"Details already exist. Data Updated","details":{"username":username}}
            else:
                data["username"]=username
                result=DBClient.myapi.finance.insert_one(data)
                return {"message":"User's financial data created","details":{"username":username}}
        else:
            return {"error":"User doesn't exist. Please create user before adding finance data"},404

    def put(self,username):
        result_count=DBClient.myapi.finance.count_documents({"username":username})
        if result_count !=0:
            data=request.json
            result=DBClient.myapi.finance.find_one_and_update( {'username': username}, {'$set': data})
            if result is not None:
                del result["_id"]
                return {"message":"User's finance data updated","old_details":result}
            else:
                return {"message":"Unable to update User's finance data from DB"},501
        else:
            return {"error":"User finance data doesn't exist"},404

    def delete(self,username):
        result_count=DBClient.myapi.finance.count_documents({"username":username})
        if result_count !=0:
            result=DBClient.myapi.finance.delete_one({"username":username})
            if result.deleted_count >0:
                return {"message":"User's finance data deleted","details":{"username":username}}
            else:
                return {"message":"Unable to delete User from DB"},501
        else:
            return {"error":"User's finance data doesn't exist"},404



class Hello(Resource):
    def get(self):
        return {"hello":"World","DB_Connection_Status":"Success"} ,200


api.add_resource(Hello,'/')
api.add_resource(User,'/User/<string:username>')
api.add_resource(Finance,'/Finance/<string:username>')


app.run(port=5000, debug=True)
