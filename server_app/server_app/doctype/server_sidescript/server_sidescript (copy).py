# Copyright (c) 2022, Sunil  and contributors
# For license information, please see license.txt




import frappe
from frappe.model.document import Document

class Server_SideScript(Document):
	# def validate(self):
	# 	frappe.msgprint(f'My Name is {self.fname} {self.last_name}')
	# 	for row in self.get('family_member'):
	# 		frappe.msgprint(f'{row.idx}. The Family mamber is {row.mname} and the Relation is {row.relation}')


# //*------------Get Doc Practice************//

	# def validate(self):
	# 	# self.get_document()

	# def get_document(self):
	# 	doc = frappe.get_doc('CarDetails', self.car_details)
	# 	frappe.msgprint(f'Brand is {doc.brand}, Model is {doc.model}, Manufacture Year is {doc.model_year} And Color is {doc.color}')

	# 	for row in doc.get('family_members'):
	# 		frappe.msgprint(__(f'{row.idx}. Name is {row.mname} and relation is {row.relation}'))


# //*-------Adding New Document (Row) in a DocTYpe

	def validate(self):
		# self.new_document()
		# self.add_document()
		# self.set_value()
		# self.get_list()
		# self.get_value()

		# doc = frappe.new_doc('emp')
		# doc.append('family_members',{
		# 	'relation' : 'Brother',
		# 	'mname' : 'Rahul'
		# })

		# doc.save()
		# doc.insert()

		pass


	# def new_document(self):
	# 	doc = frappe.new_doc('CarDetails')
	# 	doc.brand = 'Suzuki'
	# 	doc.model = 'GSXR'
	# 	doc.model_year = '2022'
	# 	doc.color = 'black'
	# 	doc.insert()

	# 	document.add_child('family_members',{'mname':'Swati','relation':'Sister'})






			



	# def add_document(self):
	# 	doc = frappe.new_doc('CarDetails')
	# 	doc.brand = 'BMW'
	# 	doc.model = 'AMG'
	# 	doc.model_year = '2022'
	# 	doc.color = 'Black'
	# 	doc.insert()

	# //*--------Set/Update Value to a document and Database

	# def set_value(self):
	# 	doc = frappe.get_doc('CarDetails','Car0001')
	# 	doc.db_set('color','yellow')


	# //*-------Get a Doc List------*//

	# def get_list(self):
	# 	doc = frappe.db.get_list('CarDetails',
	# 	filters={
	# 		'color':'White'
	# 	},
	# 	fields = ['brand','model','model_year'])

	# 	for d in doc:
	# 		frappe.msgprint(f'Brand is {d.brand} , Model is {d.model} and Year {d.model_year}')


	# //*---------get a value by passing Field------*//

	# def get_value(self):
	# 	frappe.db.set_value('CarDetails','Car0003','color','White') #To Change the Value

	# 	# To Get the Value
	# 	brand,model,model_year,color = frappe.db.get_value('CarDetails','Car0003',['brand','model','model_year','color'])

	# 	frappe.msgprint(f'Brand is {brand}, Model is {model}, Color is {color} and Manufacture Year is {model_year}')





	# def validate(self):

	# 	# //*--To Check if Document Exist Or Not

	# 	# if frappe.db.exists('CarDetails','Car0017'):
	# 	# 	frappe.msgprint('Document Exists')

	# 	# else:
	# 	# 	frappe.msgprint('Document Does not Exists')


	# 	# //*---To Get the Count the Document Present

	# 	# doc_count = frappe.db.count('CarDetails',{'color':'Black'})
	# 	# frappe.msgprint(f'The DocCount is {doc_count}')

	# 	data = frappe.db.sql(''' SELECT * from `tabCarDetails` where brand='Tata'; ''',as_dict=1)

	# 	for d in data:
	# 		frappe.msgprint(f'Model is {d.model}, Color is {d.color} and Manufacture Year is {d.model_year}')


   
# //*-------------- Frappe frm Call to pass Python Function to JS function---------**//

	# @frappe.whitelist()
	# def frm_call(self,msg):
	# 	import time
	# 	time.sleep(3)
	# 	self.last_name = 'Shinde'
	# 	frappe.msgprint(msg)

    
pass
	