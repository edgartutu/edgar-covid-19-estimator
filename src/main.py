from flask import Flask
from flask_restful import Resource, Api
from flask_restful import Api

from estimator import Covid19ImpactEstimator

app=Flask(__name__)

api = Api(app)
api.add_resource(Covid19ImpactEstimator, '/api/v1/on-covid-19')

if __name__ == '__main__':
    app.run(debug=True)