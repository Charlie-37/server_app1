# Copyright (c) 2022, Sunil  and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ValCheck(Document):
	def on_submit(self):
			frappe.msgprint(f'hello {self.docstatus}')
