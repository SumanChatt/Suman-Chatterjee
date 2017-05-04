from osv import fields, osv
from openerp.osv import fields, osv
import datetime
import xlrd
import xlwt
import logging
from openerp import tools


_logger = logging.getLogger(__name__)



class rb_lead_sampling(osv.osv):


    _name = "rb.lead.sampling"

    _columns = {
        'name': fields.char('Name Of Source', size=64, required=True),
        'address':fields.text('Address Of Source',required=True),
        'location':fields.char('Location'),
        'type_source':fields.selection([('0','Residential Building'),('1','Loyalty Base'),('2','Customer Base'),('3','Cat A company'),('4','Cat B company'),('5','Cat C company'),('6','Educational Institution'),('7','Healthcare Institution'),('8','SOE/Govt Sector'),('9','MNC Company'),('10','Other Companies'),('11','Bank Customers and Others')],string='User Level',required=True),
        'expected_data':fields.integer("Expected Number Of Data"),
        'expected_percentage_high_networth':fields.float("Expected Percentage of Affluent and High Networth"),
        'expected_percentage_affluent':fields.float("Expected Percentage of Mass Affluent"),
        'expected_percentage_upper_mass':fields.float("Expected Percentage of Upper Mass"),
        'expected_percentage_lower_mass':fields.float("Expected Percentage of Mass and Lower Mass"),
        'data':fields.binary('File',filters='*.csv'),
        }
    
rb_lead_sampling()
    
class rb_lead_citi_application(osv.osv):

    _name = "rb.lead.citi.application"
    def create(self, cr, uid, val, context = None):
        obj_lead = self.pool.get('rb.crm.lead')#the class name may be incorrect please correct as per the correct one
        lead_ids = self.pool.get('rb.crm.lead').search(cr,uid,[])
        #now keep in mind since the inputs are directly from the excel file there will be a 'u assiociated
        #with every string so we have to omit the 'u first. Now for the normal inserttion i mean to say insert inside from a form
        #there wont be any 'u thing, to handle the difference we could use the try and except block right now i am
        #writting the except block only please write the tryblock just like except block withou 'u
        customer_id = val['id_card'] #i guess this is the relation between crm_lead and this table
        _logger.error(customer_id+'Customer ID----------')
        #first let us try to get the lead id  according to the customer_id
        reflected_ids = obj_lead.search(cr,uid,[('id_card_no','=',customer_id)])
        if reflected_ids: # filtering wheather this customer exists
            lead_id = reflected_ids[0] # since it return a list and there should be only one id here
            _logger.error(str(lead_id)+'Lead ID---------')
            val['related_lead']=lead_id
            # now we have lead id lets head to further process
            lead_rs = obj_lead.browse(cr, uid,int(lead_id), context) # got the full result from here including state,tsr,team just get the result as per your need for further inserttion
            # now lets head to insertation because from the if block we are sure the customer exists
            if val['date_submited_citi'] == 0:
                val['date_submited_citi'] = '1000-1-1'
            if val['dob'] == 0:
                val['dob'] = '1000-1-1'
            if val['date_submited_qa'] == 0:
                val['date_submited_qa'] = '1000-1-1'     
            create_id =  super(rb_lead_citi_application,self).create(cr,uid,val,context)
            


        
    _columns = {
        'date_submited_qa': fields.date('Date Submitted to QA'),
        'date_submited_citi':fields.date('Date Submitted to CITI'),
        'month':fields.char('Month'),
        'customer_id':fields.char('Customer ID'),
        'customer_name':fields.char('Customer Name'),
        'mobile_number':fields.char('Mobile Number'),
        'pm':fields.char('PM'),
        'status_pm':fields.char('Status PM'),
        'free_pm':fields.char('Free PM'),
        'status_free_pm':fields.char('Status Free PM'),
        'cb':fields.char('CB'),
        'status_cb':fields.char('Status CB'),
        'free_cb':fields.char('Free CB'),
        'status_free_cb':fields.char('Status Free CB'),
        'rc':fields.char('RC'),
        'status_rc':fields.char('Status RC'),
        'rc_pl':fields.char('RC_PL'),
        'status_rc_pl':fields.char('Status RC_PL'),
        'rc_10':fields.char('RC_10'),
        'status_rc_10':fields.char('Status RC_10'),
        'rc_10_pl':fields.char('RC_10_PL'),
        'status_rc_10_pl':fields.char('Status RC_10_PL'),
        'total':fields.char('Total'),
        'approved':fields.char('Approved'),
        'dsc_name':fields.char('DSC Name'),
        'tsr_name':fields.char('TSR Name'),
        'status':fields.char('Status'),
        'team_name':fields.char('Team Name'),
        'team_lead':fields.char('Team Lead'),
        'income':fields.char('Income'),
        'company_name':fields.char('Company Name'),
        'marital_status':fields.char('Marital Status'),
        'gender':fields.char('Gender'),
        'rainbow_category':fields.char('Rainbow Category'),
        'citi_category':fields.char('CITI Category'),
        'age':fields.integer('Age'),
        'occupation_type':fields.char('Occupation Type'),
        'database':fields.char('Database'),
        'id_card':fields.char('ID Card'),
        'dob': fields.date('DOB'),
        'related_lead':fields.many2one('rb.crm.lead', 'Blank reference',select=False), ## Data <================================
        }

rb_lead_citi_application
    
class rb_tsr_funnel(osv.osv):
    _name = "rb.tsr.funnel"
    _description = "Sales Funnel"
    _auto = False
    _columns = {
        'tsr' : fields.many2one('res.users','User Name'),
        'period' : fields.char('PERIOD', readonly=True),
        'calls' : fields.char('CALLS', readonly=True),
        'r1' : fields.char('R1', readonly=True),
        'r2' : fields.char('R2', readonly=True),
        'r3' : fields.char('R3', readonly=True),
        'r4' : fields.char('R4', readonly=True),
        'r5' : fields.char('R5', readonly=True),
        'r6' : fields.char('R6', readonly=True),
        'r7' : fields.char('R7', readonly=True),
        'not_connected_total' : fields.char('NOT_CONNECTED_TOTAL', readonly=True),
        'contacted' : fields.char('CONTACTED', readonly=True),
        'r8' : fields.char('R8', readonly=True),
        'r9' : fields.char('R9', readonly=True),
        'r10' : fields.char('R10', readonly=True),
        'r11' : fields.char('R11', readonly=True),
        'r12' : fields.char('R12', readonly=True),
        'r13' : fields.char('R13', readonly=True),
        'not_eligible_total' : fields.char('NOT_ELIGIBLE_TOTAL', readonly=True),
        'eligible' : fields.char('ELIGIBLE', readonly=True),
        'r14' : fields.char('R14', readonly=True),
        'r15' : fields.char('R15', readonly=True),
        'r16' : fields.char('R16', readonly=True),
        'r17' : fields.char('R17', readonly=True),
        'r18' : fields.char('R18', readonly=True),
        'r19' : fields.char('R19', readonly=True),
        'r20' : fields.char('R20', readonly=True),
        'not_interested_total' : fields.char('NOT_INTERESTED_TOTAL', readonly=True),
        'interested' : fields.char('INTERESTED', readonly=True),
        'r21' : fields.char('R21', readonly=True),
        'r22' : fields.char('R22', readonly=True),
        'r23' : fields.char('R23', readonly=True),
        'r24' : fields.char('R24', readonly=True),
        'r25' : fields.char('R25', readonly=True),
        'r26' : fields.char('R26', readonly=True),
        'r27' : fields.char('R27', readonly=True),
        'not_leads_total' : fields.char('NOT_LEADS_TOTAL', readonly=True),
        'leads' : fields.char('LEADS', readonly=True),
        'r28' : fields.char('R28', readonly=True),
        'r29' : fields.char('R29', readonly=True),
        'appointment' : fields.char('APPOINTMENT', readonly=True)
    }
   
 
    def init(self, cr):
        tools.sql.drop_view_if_exists(cr, 'rb_tsr_funnel')
        cr.execute("""
            CREATE OR REPLACE VIEW rb_tsr_funnel AS (
                select t1.tsr as id,t1.tsr as tsr
,t1.period as period
,t1.calls as calls
,t1.r1 as r1
,t1.r2 as r2
,t1.r3 as r3
,t1.r4 as r4
,t1.r5 as r5
,t1.r6 as r6
,t1.r7 as r7
,t1.not_connected_total as not_connected_total
,t1.contacted as contacted
,t1.r8 as r8
,t1.r9 as r9
,t1.r10 as r10
,t1.r11 as r11
,t1.r12 as r12
,t1.r13 as r13
,t1.not_eligible_total as not_eligible_total
,t1.eligible as eligible
,t1.r14 as r14
,t1.r15 as r15
,t1.r16 as r16
,t1.r17 as r17
,t1.r18 as r18
,t1.r19 as r19
,t1.r20 as r20
,t1.not_interested_total as not_interested_total
,t1.interested as interested
,t1.r21 as r21
,t1.r22 as r22
,t1.r23 as r23
,t1.r24 as r24
,t1.r25 as r25
,t1.r26 as r26
,t1.r27 as r27
,t1.not_leads_total as not_leads_total
,t1.leads as leads
,t1.r28 as r28
,t1.r29 as r29
,t1.appointment as appointment from 
(with rb_tsr_funnel as (
select lead_id,tsr,dss from
	(
	select *,max(tid) over (partition by lead_id) as max_id from 
		(
		select a.id lead_id,b.create_uid tsr,c.id as dss,c.rank,b.id tid,min(rank) over (partition by a.id) as min_rank from 
			(
			select distinct(s_lead_id)::integer as id from crm_save_calldetails where  s_disposition_id <> 35 
			and date(create_date) =date(now()) 
			 --and date(create_date) = date(now() - interval '1 day')
			) a,
			rb_crm_disposition_history b, 
			rb_crm_sub_disposition c 
		where a.id = b.related_lead and b.subdisposition_code = c.id
		) t1 
	where rank = min_rank
	) t2
where tid = max_id
)
select tsr,'Today'::text period,
	COALESCE(SUM(CASE WHEN dss not in (53) THEN 1 END),0) calls,
	COALESCE(SUM(CASE WHEN dss in (1) THEN 1 END),0) r1,
	COALESCE(SUM(CASE WHEN dss in (2) THEN 1 END),0) r2,
	COALESCE(SUM(CASE WHEN dss in (3) THEN 1 END),0) r3,
	COALESCE(SUM(CASE WHEN dss in (4) THEN 1 END),0) r4,
	COALESCE(SUM(CASE WHEN dss in (5) THEN 1 END),0) r5,
	COALESCE(SUM(CASE WHEN dss in (6) THEN 1 END),0) r6,
	COALESCE(SUM(CASE WHEN dss in (7) THEN 1 END),0) r7,
	COALESCE(SUM(CASE WHEN dss in (1,2,3,4,5,6,7) THEN 1 END),0) not_connected_total,
	COALESCE(SUM(CASE WHEN dss not in (53,1,2,3,4,5,6,7) THEN 1 END),0) contacted,
	
	COALESCE(SUM(CASE WHEN dss in (22) THEN 1 END),0) r8,
	COALESCE(SUM(CASE WHEN dss in (23) THEN 1 END),0) r9,
	COALESCE(SUM(CASE WHEN dss in (24) THEN 1 END),0) r10,
	COALESCE(SUM(CASE WHEN dss in (25) THEN 1 END),0) r11,
	COALESCE(SUM(CASE WHEN dss in (26) THEN 1 END),0) r12,
	COALESCE(SUM(CASE WHEN dss in (27) THEN 1 END),0) r13,
	COALESCE(SUM(CASE WHEN dss in (22,23,24,25,26,27) THEN 1 END),0) not_eligible_total,
	COALESCE(SUM(CASE WHEN dss not in (53,1,2,3,4,5,6,7,22,23,24,25,26,27) THEN 1 END),0) eligible,	
	COALESCE(SUM(CASE WHEN dss in (14) THEN 1 END),0) r14,
	COALESCE(SUM(CASE WHEN dss in (15) THEN 1 END),0) r15,
	COALESCE(SUM(CASE WHEN dss in (16) THEN 1 END),0) r16,
	COALESCE(SUM(CASE WHEN dss in (17) THEN 1 END),0) r17,
	COALESCE(SUM(CASE WHEN dss in (18) THEN 1 END),0) r18,
	COALESCE(SUM(CASE WHEN dss in (19) THEN 1 END),0) r19,
	COALESCE(SUM(CASE WHEN dss in (20) THEN 1 END),0) r20,
	COALESCE(SUM(CASE WHEN dss in (14,15,16,17,18,19,20) THEN 1 END),0) not_interested_total,
	COALESCE(SUM(CASE WHEN dss not in (53,1,2,3,4,5,6,7,14,15,16,17,18,19,20,22,23,24,25,26,27) THEN 1 END),0) interested,
				
	COALESCE(SUM(CASE WHEN dss in (8) THEN 1 END),0) r21,
	COALESCE(SUM(CASE WHEN dss in (9) THEN 1 END),0) r22,
	COALESCE(SUM(CASE WHEN dss in (10) THEN 1 END),0) r23,
	COALESCE(SUM(CASE WHEN dss in (11) THEN 1 END),0) r24,
	COALESCE(SUM(CASE WHEN dss in (12) THEN 1 END),0) r25,
	COALESCE(SUM(CASE WHEN dss in (13) THEN 1 END),0) r26,
	COALESCE(SUM(CASE WHEN dss in (29) THEN 1 END),0) r27,
	COALESCE(SUM(CASE WHEN dss in (8,9,10,11,12,13,29) THEN 1 END),0) not_leads_total,
	COALESCE(SUM(CASE WHEN dss not in (53,1,2,3,4,5,6,7,22,23,24,25,26,27,14,15,16,17,18,19,20,8,9,10,11,12,13,29) THEN 1 END),0) leads,
	COALESCE(SUM(CASE WHEN dss in (28) THEN 1 END),0)  r28,
	COALESCE(SUM(CASE WHEN dss in (28) THEN 1 END),0) r29,	
	COALESCE(SUM(CASE WHEN dss not in (53,1,2,3,4,5,6,7,22,23,24,25,26,27,14,15,16,17,18,19,20,8,9,10,11,12,13,28,29) THEN 1 END),0) appointment
	
from rb_tsr_funnel group by tsr) t1 GROUP BY t1.tsr
,t1.period
,t1.calls
,t1.r1
,t1.r2
,t1.r3
,t1.r4
,t1.r5
,t1.r6
,t1.r7
,t1.not_connected_total
,t1.contacted
,t1.r8
,t1.r9
,t1.r10
,t1.r11
,t1.r12
,t1.r13
,t1.not_eligible_total
,t1.eligible
,t1.r14
,t1.r15
,t1.r16
,t1.r17
,t1.r18
,t1.r19
,t1.r20
,t1.not_interested_total
,t1.interested
,t1.r21
,t1.r22
,t1.r23
,t1.r24
,t1.r25
,t1.r26
,t1.r27
,t1.not_leads_total
,t1.leads
,t1.r28
,t1.r29
,t1.appointment

            )
        """)
 
rb_tsr_funnel()


class rb_tsr_yesterday_funnel(osv.osv):
    _name = "rb.tsr.yesterday.funnel"
    _description = "Sales Funnel Yesterday"
    _auto = False
    _columns = {
        'tsr' : fields.many2one('res.users','User Name'),
        'period' : fields.char('PERIOD', readonly=True),
        'calls' : fields.char('CALLS', readonly=True),
        'r1' : fields.char('R1', readonly=True),
        'r2' : fields.char('R2', readonly=True),
        'r3' : fields.char('R3', readonly=True),
        'r4' : fields.char('R4', readonly=True),
        'r5' : fields.char('R5', readonly=True),
        'r6' : fields.char('R6', readonly=True),
        'r7' : fields.char('R7', readonly=True),
        'not_connected_total' : fields.char('NOT_CONNECTED_TOTAL', readonly=True),
        'contacted' : fields.char('CONTACTED', readonly=True),
        'r8' : fields.char('R8', readonly=True),
        'r9' : fields.char('R9', readonly=True),
        'r10' : fields.char('R10', readonly=True),
        'r11' : fields.char('R11', readonly=True),
        'r12' : fields.char('R12', readonly=True),
        'r13' : fields.char('R13', readonly=True),
        'not_eligible_total' : fields.char('NOT_ELIGIBLE_TOTAL', readonly=True),
        'eligible' : fields.char('ELIGIBLE', readonly=True),
        'r14' : fields.char('R14', readonly=True),
        'r15' : fields.char('R15', readonly=True),
        'r16' : fields.char('R16', readonly=True),
        'r17' : fields.char('R17', readonly=True),
        'r18' : fields.char('R18', readonly=True),
        'r19' : fields.char('R19', readonly=True),
        'r20' : fields.char('R20', readonly=True),
        'not_interested_total' : fields.char('NOT_INTERESTED_TOTAL', readonly=True),
        'interested' : fields.char('INTERESTED', readonly=True),
        'r21' : fields.char('R21', readonly=True),
        'r22' : fields.char('R22', readonly=True),
        'r23' : fields.char('R23', readonly=True),
        'r24' : fields.char('R24', readonly=True),
        'r25' : fields.char('R25', readonly=True),
        'r26' : fields.char('R26', readonly=True),
        'r27' : fields.char('R27', readonly=True),
        'not_leads_total' : fields.char('NOT_LEADS_TOTAL', readonly=True),
        'leads' : fields.char('LEADS', readonly=True),
        'r28' : fields.char('R28', readonly=True),
        'r29' : fields.char('R29', readonly=True),
        'appointment' : fields.char('APPOINTMENT', readonly=True)
    }
   
 
    def init(self, cr):
        tools.sql.drop_view_if_exists(cr, 'rb_tsr_yesterday_funnel')
        cr.execute("""
            CREATE OR REPLACE VIEW rb_tsr_yesterday_funnel AS (
                select t1.tsr as id,t1.tsr as tsr
,t1.period as period
,t1.calls as calls
,t1.r1 as r1
,t1.r2 as r2
,t1.r3 as r3
,t1.r4 as r4
,t1.r5 as r5
,t1.r6 as r6
,t1.r7 as r7
,t1.not_connected_total as not_connected_total
,t1.contacted as contacted
,t1.r8 as r8
,t1.r9 as r9
,t1.r10 as r10
,t1.r11 as r11
,t1.r12 as r12
,t1.r13 as r13
,t1.not_eligible_total as not_eligible_total
,t1.eligible as eligible
,t1.r14 as r14
,t1.r15 as r15
,t1.r16 as r16
,t1.r17 as r17
,t1.r18 as r18
,t1.r19 as r19
,t1.r20 as r20
,t1.not_interested_total as not_interested_total
,t1.interested as interested
,t1.r21 as r21
,t1.r22 as r22
,t1.r23 as r23
,t1.r24 as r24
,t1.r25 as r25
,t1.r26 as r26
,t1.r27 as r27
,t1.not_leads_total as not_leads_total
,t1.leads as leads
,t1.r28 as r28
,t1.r29 as r29
,t1.appointment as appointment from 
(with rb_tsr_yesterday_funnel as (
select lead_id,tsr,dss from
	(
	select *,max(tid) over (partition by lead_id) as max_id from 
		(
		select a.id lead_id,b.create_uid tsr,c.id as dss,c.rank,b.id tid,min(rank) over (partition by a.id) as min_rank from 
			(
			select distinct(s_lead_id)::integer as id from crm_save_calldetails where  s_disposition_id <> 35 
			--and date(create_date) =date(now()) 
			and date(create_date) = date(now() - interval '1 day')
			) a,
			rb_crm_disposition_history b, 
			rb_crm_sub_disposition c 
		where a.id = b.related_lead and b.subdisposition_code = c.id
		) t1 
	where rank = min_rank
	) t2
where tid = max_id
)
select tsr,'Yesterday'::text period,
	COALESCE(SUM(CASE WHEN dss not in (53) THEN 1 END),0) calls,
	COALESCE(SUM(CASE WHEN dss in (1) THEN 1 END),0) r1,
	COALESCE(SUM(CASE WHEN dss in (2) THEN 1 END),0) r2,
	COALESCE(SUM(CASE WHEN dss in (3) THEN 1 END),0) r3,
	COALESCE(SUM(CASE WHEN dss in (4) THEN 1 END),0) r4,
	COALESCE(SUM(CASE WHEN dss in (5) THEN 1 END),0) r5,
	COALESCE(SUM(CASE WHEN dss in (6) THEN 1 END),0) r6,
	COALESCE(SUM(CASE WHEN dss in (7) THEN 1 END),0) r7,
	COALESCE(SUM(CASE WHEN dss in (1,2,3,4,5,6,7) THEN 1 END),0) not_connected_total,
	COALESCE(SUM(CASE WHEN dss not in (53,1,2,3,4,5,6,7) THEN 1 END),0) contacted,
	
	COALESCE(SUM(CASE WHEN dss in (22) THEN 1 END),0) r8,
	COALESCE(SUM(CASE WHEN dss in (23) THEN 1 END),0) r9,
	COALESCE(SUM(CASE WHEN dss in (24) THEN 1 END),0) r10,
	COALESCE(SUM(CASE WHEN dss in (25) THEN 1 END),0) r11,
	COALESCE(SUM(CASE WHEN dss in (26) THEN 1 END),0) r12,
	COALESCE(SUM(CASE WHEN dss in (27) THEN 1 END),0) r13,
	COALESCE(SUM(CASE WHEN dss in (22,23,24,25,26,27) THEN 1 END),0) not_eligible_total,
	COALESCE(SUM(CASE WHEN dss not in (53,1,2,3,4,5,6,7,22,23,24,25,26,27) THEN 1 END),0) eligible,	
	COALESCE(SUM(CASE WHEN dss in (14) THEN 1 END),0) r14,
	COALESCE(SUM(CASE WHEN dss in (15) THEN 1 END),0) r15,
	COALESCE(SUM(CASE WHEN dss in (16) THEN 1 END),0) r16,
	COALESCE(SUM(CASE WHEN dss in (17) THEN 1 END),0) r17,
	COALESCE(SUM(CASE WHEN dss in (18) THEN 1 END),0) r18,
	COALESCE(SUM(CASE WHEN dss in (19) THEN 1 END),0) r19,
	COALESCE(SUM(CASE WHEN dss in (20) THEN 1 END),0) r20,
	COALESCE(SUM(CASE WHEN dss in (14,15,16,17,18,19,20) THEN 1 END),0) not_interested_total,
	COALESCE(SUM(CASE WHEN dss not in (53,1,2,3,4,5,6,7,14,15,16,17,18,19,20,22,23,24,25,26,27) THEN 1 END),0) interested,
				
	COALESCE(SUM(CASE WHEN dss in (8) THEN 1 END),0) r21,
	COALESCE(SUM(CASE WHEN dss in (9) THEN 1 END),0) r22,
	COALESCE(SUM(CASE WHEN dss in (10) THEN 1 END),0) r23,
	COALESCE(SUM(CASE WHEN dss in (11) THEN 1 END),0) r24,
	COALESCE(SUM(CASE WHEN dss in (12) THEN 1 END),0) r25,
	COALESCE(SUM(CASE WHEN dss in (13) THEN 1 END),0) r26,
	COALESCE(SUM(CASE WHEN dss in (29) THEN 1 END),0) r27,
	COALESCE(SUM(CASE WHEN dss in (8,9,10,11,12,13,29) THEN 1 END),0) not_leads_total,
	COALESCE(SUM(CASE WHEN dss not in (53,1,2,3,4,5,6,7,22,23,24,25,26,27,14,15,16,17,18,19,20,8,9,10,11,12,13,29) THEN 1 END),0) leads,
	COALESCE(SUM(CASE WHEN dss in (28) THEN 1 END),0)  r28,
	COALESCE(SUM(CASE WHEN dss in (28) THEN 1 END),0) r29,	
	COALESCE(SUM(CASE WHEN dss not in (53,1,2,3,4,5,6,7,22,23,24,25,26,27,14,15,16,17,18,19,20,8,9,10,11,12,13,28,29) THEN 1 END),0) appointment
	
from rb_tsr_yesterday_funnel group by tsr) t1 GROUP BY t1.tsr
,t1.period
,t1.calls
,t1.r1
,t1.r2
,t1.r3
,t1.r4
,t1.r5
,t1.r6
,t1.r7
,t1.not_connected_total
,t1.contacted
,t1.r8
,t1.r9
,t1.r10
,t1.r11
,t1.r12
,t1.r13
,t1.not_eligible_total
,t1.eligible
,t1.r14
,t1.r15
,t1.r16
,t1.r17
,t1.r18
,t1.r19
,t1.r20
,t1.not_interested_total
,t1.interested
,t1.r21
,t1.r22
,t1.r23
,t1.r24
,t1.r25
,t1.r26
,t1.r27
,t1.not_leads_total
,t1.leads
,t1.r28
,t1.r29
,t1.appointment

            )
        """)
 
rb_tsr_yesterday_funnel()