from openerp.osv import fields, osv


class reference_lead_wizard(osv.TransientModel):
    _name = "reference.lead.wizard"
    _columns = {
            'lead_ids': fields.one2many('reference.lead.class', 'wizard_id', string='Leads'),
        }


    def default_get(self, cr, uid, fields, context=None):
        if context == None:
            context = {}
        lead_ids = context.get('active_ids', [])
        wiz_id = context.get('active_id', None)
        res = []
        leads = self.pool.get('rb.crm.lead').browse(cr, uid, lead_ids, context=context)
        for lead in leads:
            res.append((0, 0, {
                'wizard_id': wiz_id,
                'lead_id': lead.id,
                'lead_subject': lead.name,
            }))
        return {'lead_ids': res}


    def change_team_button(self, cr, uid, id, context=None):
        wizard = self.browse(cr, uid, id, context=context)[0]
        #need_reload = any(uid == user.user_id.id for lead in wizard.lead_ids)
        line_ids = [lead.id for lead in wizard.lead_ids]

        self.pool.get('reference.lead.class').change_team_button(cr, uid, line_ids, context=context)
        # don't keep temporary password copies in the database longer than necessary
        #self.pool.get('reference.lead.class').write(cr, uid, line_ids, {'new_sales_team': False,'team_lead_id':False}, context=context)

        #if need_reload:
        #    return {
        #        'type': 'ir.actions.client',
        #        'tag': 'reload'
        #    }

        return {'type': 'ir.actions.act_window_close'}


class reference_lead_class(osv.TransientModel):
    _name = "reference.lead.class"

    def get_universal_salesteam(self, cr, uid, context=None):
	    object_sales_team = self.pool.get("rb.sales.team")
	    options = []
	    active_team_ids = object_sales_team.search(cr, 1, [('active','=',True)])
	    result_set = object_sales_team.read(cr, 1,active_team_ids, ['id','name'], context)
	    for result in result_set:
		    name = result['name']
		    id = result ['id']
		    option = (id,name)
		    options.append(option)
	    return options

    def onchange_sl_team(self,cr,uid,ids,sales_team_id,context=None):
        #print "Sales Team Id IS ************************************************************"+str(sales_team_id)
        try:
            t_var = self.pool.get('rb.sales.team').browse(cr, 1, sales_team_id,context=context)['team_lead_group']
            val = {'hidden_tl_id':int(t_var),'team_lead_id':False}
            
        except:
            val = {'hidden_tl_id':False,'team_lead_id':False}
        return {'value': val}    
        #print "Sales Team Id IS ************************************************************"+str(t_var)
        
##    def get_universal_campaign(self, cr, uid, context=None):
##        object_campaign = self.pool.get("rb.campaign.crm")
##        options = []
##        active_campaign_ids = object_campaign.search(cr, 1, [('active','=',True)])
##        result_set = object_campaign.read(cr, 1,active_campaign_ids, ['id','name'], context)
##        for result in result_set:
##            	name = result['name']
##		id = result ['id']
##		option = (id,name)
##		options.append(option)
##	return options


    _columns = {
        'wizard_id': fields.many2one('reference.lead.wizard', string='Wizard', required=True),
        'lead_id': fields.many2one('rb.crm.lead', string='Lead', required=True),
        'lead_subject': fields.char('Lead Subject', readonly=True),
        'new_sales_team': fields.selection(get_universal_salesteam,'Select Team',required=True),
        'hidden_tl_id' : fields.integer('TL id holder',invisible=True),
        'team_lead_id' : fields.many2one('rb.tl.team','TL Group',domain="[('id','=',hidden_tl_id)]",required=True),
        
       
    }
    _defaults = {
        #'new_sales_team': [('',0)],
    }

    def change_team_button(self, cr, uid, ids, context=None):
        for lead in self.browse(cr, uid, ids, context=context):
            #raise osv.except_osv(('warning'),(lead.team_lead_id.id))
            print str(int(lead.new_sales_team))+"----------------------------------------"
            print str(lead.team_lead_id.id)+"----------------------------------------"
            #print 
            self.pool.get('rb.crm.lead').write(cr, uid, lead.lead_id.id, {'sale_team_name': int(lead.new_sales_team),'team_lead':lead.team_lead_id.id,'lead_ref_stat':True,'tsr_change_flag':True})
	    self.pool.get('lead.referral.log').create(cr, 1,{'ref_by':uid,'ref_lead_id':lead.lead_id.id,'ref_sales_team':lead.new_sales_team,'ref_tl_group':lead.team_lead_id.id},context = context)





                                                            #***** TSR MENU ENTRY*******#



class reference_lead_tsr_wizard(osv.TransientModel):
    _name = "reference.lead.tsr.wizard"
    _columns = {
            'lead_ids': fields.one2many('reference.lead.tsr.class', 'wizard_id', string='Leads'),
        }


    def default_get(self, cr, uid, fields, context=None):
        if context == None:
            context = {}
        lead_ids = context.get('active_ids', [])
        wiz_id = context.get('active_id', None)
        res = []
        leads = self.pool.get('rb.crm.lead').browse(cr, uid, lead_ids, context=context)
        for lead in leads:
            res.append((0, 0, {
                'wizard_id': wiz_id,
                'lead_id': lead.id,
                'lead_subject': lead.name,
                'lead_sale_team' : lead.sale_team_name.id,
                'lead_ref_st' : lead.lead_ref_stat,
                'tsr_cg_flag' : lead.tsr_change_flag,
            }))
        return {'lead_ids': res}


    def change_tl_campaign_button(self, cr, uid, id, context=None):
        wizard = self.browse(cr, uid, id, context=context)[0]
        #need_reload = any(uid == user.user_id.id for lead in wizard.lead_ids)
        line_ids = [lead.id for lead in wizard.lead_ids]

        self.pool.get('reference.lead.tsr.class').change_tl_campaign_button(cr, uid, line_ids, context=context)
        # don't keep temporary password copies in the database longer than necessary
        #self.pool.get('reference.lead.tsr.class').write(cr, uid, line_ids, {'campaign_team': False,'sales_team_r':False}, context=context)

        #if need_reload:
        #    return {
        #        'type': 'ir.actions.client',
        #        'tag': 'reload'
        #    }

        return {'type': 'ir.actions.act_window_close'}


class reference_lead_tsr_class(osv.TransientModel):
    _name = "reference.lead.tsr.class"

    #def team_based_tsr(self, cr, uid, context=None):
        


    _columns = {
        'wizard_id': fields.many2one('reference.lead.tsr.wizard', string='Wizard', required=True),
        'lead_id': fields.many2one('rb.crm.lead', string='Lead', required=True),
        'lead_subject': fields.char('Lead Subject', readonly=True),
        'new_campaign': fields.many2one('rb.campaign.crm','Campaign' ,required=True),
        'new_tl' : fields.many2one('res.users', 'Tsr', domain="[('sales_team.id','=',lead_sale_team)]",required=True),
        'lead_sale_team' : fields.many2one('rb.sales.team','Sales Team',readonly=True),
        'lead_ref_st' : fields.boolean('Contain ref stat',invisible=True),
        'tsr_cg_flag' : fields.boolean('Tsr update flag',invisible=True)
    }
    _defaults = {
        #'new_sales_team': [('',0)],
    }

    def change_tl_campaign_button(self, cr, uid, ids, context=None):
        #raise osv.except_osv(('warning'),(self.browse(cr, uid, ids, context=context)[0].lead_ref_st))
        if (self.browse(cr, uid, ids, context=context)[0].tsr_cg_flag != True):
            raise osv.except_osv(("What are you doing!!!!!"),('You are not supposed to change the TSR of this lead'))
        for lead in self.browse(cr, uid, ids, context=context):
            self.pool.get('rb.crm.lead').write(cr, 1, lead.lead_id.id, {'campaign_team':lead.new_campaign.id,'sales_team_r':lead.new_tl.id,'tsr_change_flag':False,'lead_ref_stat':False})            

            self.pool.get('lead.referral.tsr.log').create(cr, 1,{'ref_by':uid,'ref_lead_id':lead.lead_id.id,'ref_campaign':lead.new_campaign.id,'ref_tsr':lead.new_tl.id},context = context)


			






	
