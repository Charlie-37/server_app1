# Copyright (c) 2022, Sunil  and Contributors
# See license.txt

import frappe
import unittest

class TestValCheck(unittest.TestCase):

	def validate(self):
			frappe.msgprint(f'hello {self.first_name}')

