# -*- coding: utf-8 -*-

import os

CSRF_ENABLED = True
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'records.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
PUBLIC_METHODS = ['GET']
IF_MATCH = False
DEBUG = True

DOMAIN = {
    'location': {
        'item_title':'location',
        'additional_lookup': {
            'url': '[0-9]+',
            'field': '_id'
        },
        'cache_control': 'max-age=10,must-revalidate',
        'cache_expires': 10,
        'resource_methods': ['GET', 'POST', 'DELETE']
        #'item_methods': ['GET', 'PUT','PATCH', 'DELETE']
    },

	'stores' : {
		'item_title':'stores',
		'additional_lookup': {
			'url':'[0-9]+',
			'field':'_id'
		},
		'cache_control':'max-age=10, must-revalidate',
		'cache_expires': 10,
		'resource_methods':['GET', 'POST', 'DELETE'],
		'item_methods': ['GET', 'PUT','PATCH', 'DELETE']
	},

    'avail': {
        'item_title':'drugs_available',
        'additional_lookup': {
            'url': '[0-9]+',
            'field': '_id'
        },
        'cache_control': 'max-age=10,must-revalidate',
        'cache_expires': 10,
        'resource_methods': ['GET', 'POST', 'DELETE'],
        'item_methods': ['GET', 'PUT', 'PATCH','DELETE']
    }
}