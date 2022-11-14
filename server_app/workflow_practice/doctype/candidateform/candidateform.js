// Copyright (c) 2022, Sunil  and contributors
// For license information, please see license.txt

frappe.ui.form.on('CandidateForm', {

	// validate: function(frm) {
	// 	let doc_stat = frm.doc.docstatus
	// 	console.log(frm.doc.workflow_state)


	// 	if (doc_stat == '1'){

	// 		frm.call({
	// 			doc : frm.doc,
	// 			method : 'Add_Selected_Employee',
	// 			args:{
	// 				emp:{
	// 					fname : frm.doc.fname,
	// 					last_name : frm.doc.last_name,
	// 					city : frm.doc.city,
	// 					app_position : frm.doc.app_position,
	// 					contact : frm.doc.contact,
	// 					description : frm.doc.description,
	// 				}

	// 			},
	// 			callback : function(r){
	// 				console.log(r.message)
	// 				frappe.msgprint('Sucessfully Added')
	// 			}
	// 		})

	// 	}


	// },

	// timeline_refresh: function(frm){
	// 	console.log(frm.doc.workflow_state)
	// 	console.log(frm.doc.description)

	// 	if (frm.doc.workflow_state == 'Approved'){
	// 		console.log('I will call frm.call')

	// 		frm.call({
	// 			doc : frm.doc,
	// 			method : 'Add_Selected_Employee',
	// 			args:{
	// 				emp:{
	// 					fname : frm.doc.fname,
	// 					last_name : frm.doc.last_name,
	// 					city : frm.doc.city,
	// 					app_position : frm.doc.app_position,
	// 					contact : frm.doc.contact,
	// 					description : frm.doc.description,
	// 					name : frm.doc.name,
	// 				}

	// 			},
	// 			callback : function(r){
	// 				console.log(r.message)
	// 				frappe.msgprint('Sucessfully Added')
	// 			}
	// 		})

	// 	}



	// }
});
