from eve import Eve
from eve.io.sql import SQL, ValidatorSQL
from tables import Stores, Location, DrugsAvail
from flask import request, jsonify
from flask.ext.restful import Api, Resource
from bs4 import BeautifulSoup
import urllib2, csv

app = Eve(validator=ValidatorSQL, data=SQL)
api = Api(app)
ctr = 1

#textfile = file('drugstores.txt', 'wb')
c = csv.writer(open("drugstores.csv", "wb"))

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

while (ctr <= 20):
	index_url = 'http://www.fda.gov.ph/industry-corner/drug-industry-all-registered-drugstore-manufacturer-distributor-and-trader/drugstore?start=' + str(ctr)

	drugstoreFile = urllib2.urlopen(index_url)
	drugstoreHtml = drugstoreFile.read()
	drugstoreFile.close()

	soup = BeautifulSoup(drugstoreHtml)
	drugstoreAll = soup.find_all("a")
	for links in soup.select('table.zebra a[href^=/industry-corner]'):
		print (links.get_text())
		c.writerow([links.get_text().encode('utf-8')])

	ctr = ctr + 10
print ('Writing done...\n\n\nCheck drugstores.csv')

db = app.data.driver
db.create_all()
app.run(debug=True)




