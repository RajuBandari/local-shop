from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Product(Resource):
    def get(self):
        return {
            'result': {
                'name': 'Galaxy',
                'brand': 'Samsung',
                'price': '800 CAD',
                'Features': {
                    'Camera': '20px',
                    'Memory': '4GB',
                    'CPU': '1024kb'
                }
            }
        }

    def post(self):
        return {
            "result": 'created'
        }

api.add_resource(Product, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)