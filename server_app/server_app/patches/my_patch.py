import frappe

def execute():
    doc = frappe.new_doc('ValCheck')    
    doc.first_name  = "Sunil Bhave"
    doc.insert()

    # //dansdkn