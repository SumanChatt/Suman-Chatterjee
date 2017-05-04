openerp.rainbow_crm = function(openerp) {

    document.oncontextmenu = document.body.oncontextmenu = function() {return false;}
    document.onselectstart = document.body.onselectstart = function() {return false;}

      var MODELS_TO_HIDE = ['rb.crm.lead'];
	  
	  var start_time;
	  var tree_view_start_time

	  var login_action_time;

	openerp.web.Login.include({
        	do_login: function(db, login, password) {
            	login_action_time = new Date();
			console.log("Login Start Date"+String(login_action_time));
            	this._super.apply(this, arguments);
        	}
    	});
    


    openerp.web.ListView.include({



		init:function(){
			var end_time = new Date();
			var self = this;
			var ret = this._super.apply(this, arguments);
			var res_model = this.dataset.model;
			if ($.inArray(res_model, MODELS_TO_HIDE) != -1) {
				if (login_action_time!==null){
					console.log("Login END TIME"+String(end_time));
					diff_login = (end_time-login_action_time)/1000;
					//console.log(end_time-login_action_time);
					
					login_create_value={ 
						"x_modle_name":MODELS_TO_HIDE[0], 
						"x_time_start":String(login_action_time), 
						"x_time_end":String(end_time),
						"x_difference":diff_login,
						"x_view":'LOGIN'
						};
					
					//new openerp.web.Model('x_rb.performance.log').get_func('create')(login_create_value);
					login_action_time = null;
				}
				
			}
			
		},















        start: function() {
	    var d2 = new Date();
	    tree_view_start_time = d2
            var self = this;
            var ret = this._super.apply(this, arguments);
            var res_model = this.dataset.model;
            if ($.inArray(res_model, MODELS_TO_HIDE) != -1) {
                
		$( document ).on( "click", ".oe_i", function() {
				var d2 = new Date();
				tree_view_start_time = d2
				//console.log(d2);
					
					
			});

            };
            return ret;
        },



        style_for: function(r) {
            var self = this;
            var ret = this._super.apply(this, arguments);
            var res_model = this.dataset.model;
            if ($.inArray(res_model, MODELS_TO_HIDE) != -1) {
		var d2 = new Date();
		//console.log("END LIST VIEW TIME"+String(d2));
                //console.log("START LIST VIEW TIME"+String(tree_view_start_time));
		//console.log(d2-tree_view_start_time);
		diff = (d2-tree_view_start_time)/1000;
		console.log(diff);
		tree_create_value={ 
			"x_modle_name":MODELS_TO_HIDE[0], 
			"x_time_start":String(tree_view_start_time), 
			"x_time_end":String(d2),
			"x_difference":diff,
			"x_view":'LIST'
		};
		if (tree_view_start_time!==null){
			//new openerp.web.Model('x_rb.performance.log').get_func('create')(tree_create_value);		
			tree_view_start_time = null;
		}		

            };
            return ret;
        },
    });













	  
	openerp.web.FormView.include({

	
        start: function(data) {
		var d2 = new Date();
		start_time = d2
		//$(document).off('click','.oe_i');
            	var self = this;
            	var ret = this._super.apply(this, arguments);
            	var res_model = this.dataset.model;
            	if ($.inArray(res_model, MODELS_TO_HIDE) != -1) {
                	console.log(d2);
			$( document ).on( "click", ".oe_i", function() {
				var d2 = new Date();
				start_time = d2
				//console.log(d2);
					
					
			});
            	};
            	return ret;
        },
    		


        load_record: function(data) {
	   var d2 = new Date();
            var self = this;
            var ret = this._super.apply(this, arguments);
            var res_model = this.dataset.model;
            if ($.inArray(res_model, MODELS_TO_HIDE) != -1) {
                //console.log("END TIME"+String(d2));
		//console.log("START TIME"+String(start_time));
		//console.log(d2-start_time);
		diff = (d2-start_time)/1000;
		form_create_value={ 
			"x_modle_name":MODELS_TO_HIDE[0], 
			"x_time_start":String(start_time), 
			"x_time_end":String(d2),
			"x_difference":diff,
			"x_view":'FORM'
		};
		//new openerp.web.Model('x_rb.performance.log').get_func('create')(form_create_value);		
		start_time = null;



            };
            return ret;
        },
    });
	
};
