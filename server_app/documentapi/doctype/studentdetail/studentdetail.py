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

	## 6. Frappe.get_meta()

		# # meta = frappe.get_meta('StudentDetail')
		# # x = meta.has_field('contact')
		# # y = meta.get_custom_fields() #Not working
		# # print(f'yolo ; {y}')


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


	# //*---------------------**-----------------------//


	# 8. doc.get_doc_before_save

		# doc = frappe.get_doc('StudentDetail','Prasad', as_dict=1)

		# # frappe.msgprint(f'here {doc.sclass}')

		# old_doc = doc.get_doc_before_save()  #Not working

		# if old_doc.sclass != doc.sclass:
		# 	frappe.msgprint('Doc changed')

		# else:
		# 	frappe.msgprint('not changed')


	# //*---------------------**-----------------------//


	# # 9.doc.check_permision()

	# 	doc = frappe.get_doc('StudentDetail','Prasad', as_dict=1)
	# 	x = doc.check_permission(permtype='read')

	# 	frappe.msgprint(f'permission is {x}')


	# //*---------------------**-----------------------//


	# #10 doc.get_title()

	# 	frappe.msgprint(f'Title is {doc.get_title()}')

	# # 11 doc.get_url()

	# 	frappe.msgprint(f'Url is : {doc.get_url()}')


	# //*---------------------**-----------------------//

	# # 12 doc.add_comment()

	# 	doc.add_comment('Comment',text='sample Comment')
	# 	doc.add_comment('Edit',text='Value Changed in form')

	# //*---------------------**-----------------------//

	# # 13 doc.add_tags()

	# 	doc.add_tag('Python Developer')
	# 	doc.add_tag('Angular Developer')
	# 	doc.add_tag('Student')

	# # 14 doc.get_tags()

	# 	frappe.msgprint(f'tags are : {doc.get_tags()}')

	# //*---------------------**-----------------------//


	# #15 doc.run_method()

	# 	doc.run_method('loops')

	# 	def loops():
	# 		for i in range(5):
	# 			frappe.msgprint('Run Method')




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

		# 8. Frappe.db.delete()

		# if frappe.db.exists('StudentDetail','Maht'):

		# 	frappe.db.delete('StudentDetail',filters={'last_name':'Maht'})
		# 	frappe.db.commit()

		# //*---------------------**-----------------------//


		# 9. Frappe.db.describe()

		# frappe.db.describe('StudentDetail')


		# # Out[27]: 
		# # (('name', 'varchar(140)', 'NO', 'PRI', None, ''),
		# # ('creation', 'datetime(6)', 'YES', '', None, ''),
		# # ('modified', 'datetime(6)', 'YES', 'MUL', None, ''),
		# # ('modified_by', 'varchar(140)', 'YES', '', None, ''),
		# # ('owner', 'varchar(140)', 'YES', '', None, ''),
		# # ('docstatus', 'int(1)', 'NO', '', '0', ''),
		# # ('parent', 'varchar(140)', 'YES', 'MUL', None, ''),
		# # ('parentfield', 'varchar(140)', 'YES', '', None, ''),
		# # ('parenttype', 'varchar(140)', 'YES', '', None, ''),
		# # ('idx', 'int(8)', 'NO', '', '0', ''),
		# # ('rnum', 'varchar(140)', 'YES', '', None, ''),
		# # ('enable', 'int(1)', 'NO', '', '0', ''),
		# # ('first_name', 'varchar(140)', 'YES', '', None, ''),
		# # ('last_name', 'varchar(140)', 'YES', '', None, ''),
		# # ('sphotos', 'text', 'YES', '', None, ''),
		# # ('contact', 'varchar(140)', 'YES', '', None, ''),
		# # ('date_of_birth', 'date', 'YES', '', None, ''),
		# # ('sclass', 'int(11)', 'NO', '', '0', ''),
		# # ('route', 'varchar(140)', 'YES', '', None, ''),
		# # ('amended_from', 'varchar(140)', 'YES', '', None, ''),
		# # ('_user_tags', 'text', 'YES', '', None, ''),
		# # ('_comments', 'text', 'YES', '', None, ''),
		# # ('_assign', 'text', 'YES', '', None, ''),
		# # ('_liked_by', 'text', 'YES', '', None, ''))

		# //*---------------------**-----------------------//

		


		pass
		








