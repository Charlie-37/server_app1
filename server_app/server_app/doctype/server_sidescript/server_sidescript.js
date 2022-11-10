// Copyright (c) 2022, Sunil  and contributors
// For license information, please see license.txt

frappe.ui.form.on('Server_SideScript', {


 //*-------------- Frappe frm Call to pass Python Function to JS function---------**//

// 	validate: function(frm){
// 		frm.call({
// 			doc:frm.doc,
// 			method:'frm_call',
// 			args: {
// 				msg:'Hello World'
// 			},
// 			freeze : true,
// 			freeze_message : 'Loading Frm Call',

// 			callback: function(r){
// 				// frappe.msgprint(r.message)
// 			}
// 		});
// 	}

enable: function(frm){
	let row = frm.add_child('family_members',{
		mname : 'Jay',
		relation : 'Brother'
	});

    frm.refresh_field('family_members')
}


 });
