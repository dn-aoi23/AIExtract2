from eve.io.sql.decorators import registerSchema
from eve.io.sql.common import CommonColumns
from eve.io.sql import db



@registerSchema('stores')
class Stores(CommonColumns):
	__tablename__ = 'stores'
	storename = db.Column(db.String(80))
	address = db.Column(db.String(1000), unique=True)
	contact = db.Column(db.String(35))
	#password = db.Column(db.String(64)) #column for password
	email = db.Column(db.String(64))

@registerSchema('location')
class Location(CommonColumns):
    __tablename__ = 'location'
    area = db.Column(db.String(50))#, unique=True)

@registerSchema('avail')
class DrugsAvail(CommonColumns):
    __tablename__ = 'avail'
    generic = db.Column(db.String(50))
    brand = db.Column(db.String(50), unique=True)
    dosage = db.Column(db.String(10))
    pricepc = db.Column(db.Float)
    pricebox = db.Column(db.Float)