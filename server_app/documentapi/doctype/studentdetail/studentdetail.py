# Copyright (c) 2022, Sunil  and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator

class StudentDetail(WebsiteGenerator):

	# Document API Practice

	# def validate(self):

	# 	# 1. Frapp.get_doc
	# 	# doc = frappe.get_doc('StudentDetail','Sunil')
	# 	# lname = doc.last_name
	# 	# frappe.msgprint(f'last name is {lname}')


	# 	# # inserting value to another doc
	# 	# doc2 = frappe.get_doc({
	# 	# 	'doctype' : 'Server_SideScript',
	# 	# 	'fname' : 'Harshali'

	# 	# })
	# 	# doc2.insert()

	# //*---------------------**-----------------------//

	# 	# 2. Frappe.get_last_doc

	# 	# doc = frappe.get_last_doc('Server_SideScript')
	# 	# fname = doc.fname
	# 	# frappe.msgprint(f'first name is {fname}')


	# //*---------------------**-----------------------//


	# 	# # 3. Frappe.new_doc

	# 	# doc = frappe.new_doc('Server_SideScript')
	# 	# doc.fname='Akshay'
	# 	# doc.last_name = 'Singh'
	# 	# doc.insert()
	# 	# doc.save('submit')


	# //*---------------------**-----------------------//


	# 	# # 4. FRappe.delete_doc

	# 	# doc = frappe.delete_doc('Server_SideScript','Harshali')


	# //*---------------------**-----------------------//

	# 	# # 5. frappe.rename_doc

	# 	# doc = frappe.rename_doc('Server_SideScript','Akshay','Shubham')


# //*---------------------**-----------------------//


	# 	# # 6. Doc.db.set

	# 	# doc = frappe.get_doc('StudentDetail','Prasad')
	# 	# doc.db_set('last_name','Jayandar')
	# 	# doc.reload()

	# //*---------------------**-----------------------//


	# 	# 7. Doc.append()

	# 	# doc = frappe.get_doc('StudentDetail','Prasad')
	# 	# doc.append('student_subject',{
	# 	# 	"subject_1" : 'Arts'
	# 	# })


# //*-------------------------------------**-----------------------------------------//

	# DataBase Api Practice

	def validate(self):

		# 1. Frappe.db.get_list

		# doc= frappe.db.get_list('StudentDetail',)
		# for i in doc:
			# frappe.msgprint(f'Name : {i}')


		# doc= frappe.db.get_list('StudentDetail', pluck ='first_name')
		# for i in doc:
		# 	frappe.msgprint(f'Name : {i}')


		# doc= frappe.db.get_list('StudentDetail',filters = {'last_name' : 'Bhave'},fields=['first_name','last_name'])
		# for i in doc:
		# 	frappe.msgprint(f'Name : {i.first_name}')


		# //*---------------------**-----------------------//


		# # 2. frappe.db.get_all

		# doc = frappe.db.get_all('StudentDetail')
		# frappe.msgprint(f'name : {doc}')

		# //*---------------------**-----------------------//

		# 3.frappe.db.get_value 

		# doc = frappe.db.get_value('StudentDetail','Sunil','last_name')
		# frappe.msgprint(f'last name {doc}')

		# doc = frappe.db.get_value('StudentDetail','Sunil',['last_name','contact'] ,as_dict=1)
		# frappe.msgprint(f'last name {doc.last_name}')
		# frappe.msgprint(f'last name {doc.contact}')


		# //*---------------------**-----------------------//

		# 4.frappe.db.set_value

		# doc = frappe.db.set_value('StudentDetail','Prasad','last_name','Omkar')

		# doc = frappe.db.set_value('StudentDetail','Prasad',{
		# 	'last_name' : 'Harbajan',
		# 	'contact' : '888888',
		# 	'sclass' : 16
		# })

		# //*---------------------**-----------------------//

		# # 5. frappe.db.exists

		# if frappe.db.exists('StudentDetail','Prasad'):
		# 	frappe.msgprint('exist')
		# else:
		# 	frappe.msgprint('not exists')

		# //*---------------------**-----------------------//


		# # 6.frappe.db.count

		# doc = frappe.db.count('StudentDetail')
		# frappe.msgprint(f'count is : {doc}')


		# //*---------------------**-----------------------//

		# 7. frappe.db.sql

		# values = {'first_name' : 'Prasad'}
		# doc = frappe.db.sql("""
		# 	select last_name from `tabStudentDetail`
		# 	where first_name = %(first_name)s""",values=values, as_dict=0)

		# frappe.msgprint(f'l name : {doc[0][0]}')


		# //*---------------------**-----------------------//

		pass
		








