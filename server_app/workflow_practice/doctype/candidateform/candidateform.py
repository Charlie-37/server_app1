# Copyright (c) 2022, Sunil  and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class CandidateForm(Document):

	# @frappe.whitelist()
	# def Add_Selected_Employee(self,emp):
	# 	# data = frappe.get_all(doctype, fields=['*'])

	# 	# return frappe.msgprint(f'val is {data[4]}')

	# 	idName = emp['name']

	# 	if not frappe.db.exists('SelectedEmployee',idName):

	# 		doc = frappe.new_doc('SelectedEmployee')
	# 		doc.fname = emp['fname']
	# 		doc.last_name= emp['last_name']
	# 		doc.city = emp['city']
	# 		doc.app_position = emp['app_position']
	# 		doc.contact = emp['contact']
	# 		doc.description = emp['description']
	# 		doc.insert()
	# 		doc.save()
	# 		doc.submit()
	# 		return 'Value Added'

	# 	else:
	# 		return 'Employee Already Exists'



		def on_submit(self):
			frappe.msgprint(f'hello {self.docstatus}')
			idName = self.name

			if not frappe.db.exists('SelectedEmployee',idName):

				doc = frappe.new_doc('SelectedEmployee')
				doc.fname = self.fname
				doc.last_name= self.last_name
				doc.city = self.city
				doc.app_position = self.app_position
				doc.contact =  self.contact
				doc.description =  self.description
				doc.insert()
				doc.save()
				doc.submit()
				return 'Value Added'

			else:
				return 'Employee Already Exists'



	










class A:
	pass



class B(A):
	pass


class C(B,A):
	pass