from flask import Flask, request
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
# from flask_restful_swagger_3 import Api
from models.resources.user import UserRegister
from models.resources.item import Item, ItemList


app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)
jwt = JWT(app, authenticate, identity)

# SWAGGER_URL = '/api/docs'  
# API_URL = 'http://petstore.swagger.io/v2/swagger.json'  # Our API url (can of course be a local resource)
# swaggerui_blueprint = get_swaggerui_blueprint(
#     SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
#     API_URL,
#     config={  # Swagger UI config overrides
#         'app_name': "Test application"
#     },
# )
# app.register_blueprint(swaggerui_blueprint)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
if __name__ == '__main__':
    app.run(debug=True)
