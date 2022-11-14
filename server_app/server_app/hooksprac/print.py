import frappe


def showmsg(doc , event):
    print("\n\n\n\n\nHello World\n\n\n\n\n")
    frappe.msgprint('Hello World')

def delete_sucess(doc, event):
    print('\n\n\nHello World\n\n\n')
    frappe.msgprint('Deleted SucessFully')