###########
# IMPORTS #
###########

# THIRD PARTY DEPENDENCIES
from pymongo import MongoClient

##################
# MONGO DATABASE #
##################

class Mongo:

    def __init__(self,
                 database_name='arrow-test',
                 host='localhost', 
                 port=27017):

        self.client = MongoClient(host, port)
        self.database = self.client[database_name]
        self.users = self.database['users']

    def get_user(self, username):
        return self.users.find_one({'username': username})
    
    def put_user(self, username):
        return self.users.insert_one({'username': username})
