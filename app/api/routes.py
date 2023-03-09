from flask import Blueprint, request
from .apiauth import basic_auth_required, token_auth_required
from ..models import  User, Workout, My_Workout
from flask_cors import cross_origin

api = Blueprint('api', __name__)


# @api.route('/api/signup', methods=["POST"])
# def signUpPageAPI():
#     data = request.json
   
       
#     username = data['username']
#     email = data['email']
#     password = data['password']
    


#     # add user to database
#     user = User(username, email, password)

#     user.saveToDB()

#     return {
#         'status': 'ok',
#         'message': "Succesffuly created an account!"
#     }

# @api.route('/api/login', methods=["POST"])
# @basic_auth_required
# def getToken():
#     user = basic_auth_required.current_user()
#     return {
#         'status': 'ok',
#         'user': user.to_dict(),
#     }
    