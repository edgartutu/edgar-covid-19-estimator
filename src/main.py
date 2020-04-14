from flask import Flask
from flask_restful import Resource, Api
from flask_restful import Api

from estimator import estimator

app=Flask(__name__)

api = Api(app)
api.add_resource(estimator, '/api/v1/on-covid-19')

if __name__ == '__main__':
    app.run(debug=True)