from eve import Eve
from eve.io.sql import SQL, ValidatorSQL
from tables import Stores, Location, DrugsAvail
#from flask.ext.httpauth import HTTPBasicAuth
from flask import request, jsonify
from flask.ext.restful import Api, Resource


#auth = HTTPBasicAuth()
app = Eve(validator=ValidatorSQL, data=SQL)
api = Api(app)

class InsertStore(Resource):

	def post(self):
		storename = request.form['storename']
		address = request.form['address']
		contact = request.form['contact']
		email = request.form['email']

class InsertDrugs(Resource):

	def post(self):
		generic = request.form['Generic Name']
		brand = request.form['Brand Name']
		dosage = request.form['Dosage']
		pricepc = request.form['Price/pc']
		pricebox = request.form['Price/box']

api.add_resource(InsertStore, '/stores', endpoint='stores')
api.add_resource(InsertDrugs, '/stores/<string:storename>/drugs')

db = app.data.driver
db.create_all()
app.run(debug=True)

