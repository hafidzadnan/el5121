pipenv install requests
import requests
requests.get('https://api.github.com')

from flask import Flask
from flask_restful import Resource, reqparse ,Api

TGS = Flask(__name__)
api = Api(TGS)

