###########
# IMPORTS #
###########

# STANDARD LIBRARY
import os
import sys

# THIRD PARTY DEPENDENCIES
from flask_restplus import Resource
from flask_restplus import Api
from flask import Flask

# INTERNAL DEPENDENCIES
sys.path.append('.')
import analyzer

###########
# GLOBALS #
###########

# META FLAGS
__author__ = ['Cosmia', 'Bryce']
__version__ = '0.1'

# CONSTANTS

##################
# INITIALIZATION #
##################

# FLASK INITIALIZATION
app = Flask(__name__)
api = Api(app, title='Arrow API')

# DATABASE INITIALIZATION



#############
# FUNCTIONS #
#############

def http_response(code, message=None):
    response = {'code': code}
    if message:
        response['messsage'] = message
    if 200 <= code < 300:
        response['status'] = 'success'
    elif 300 <= code < 400:
        response['status'] = 'error'
    elif 500 <= code < 600:
        response['status'] = 'failure'
    

#########
# USERS #
#########

users = api.namespace('Users')

@users.route('/<string:username>')
class User(Resource):

    def get(self):
        return 'Bob'

    def put(self):
        return http_response(200)

############
# ANALYSIS #
############

analysis = api.namespace('Users')

if __name__ == '__main__':
    app.run(debug=True)
