# -*- coding: utf-8 -*
from osv import fields, osv
from openerp.osv import fields, osv

class vfsr_referral_process(osv.osv):

    _name = "vfsr.referral.process"

    def create(self, cr, uid, values, context=None):
        new_id = super(vfsr_referral_process, self).create(cr, uid, values, context)
        srt = 'RB-REF00'+str(new_id)
        cr.execute('update vfsr_referral_process set name=%s where id=%s',(srt,new_id,))
        return new_id


    def name_get(self,cr,uid,ids,context=None):
        if context is None:
            context ={}
        res=[]
        record_name=self.browse(cr,uid,ids,context)
        for object in record_name:

                if object.name:
                    res.append((object.id,object.name+" / "+object.reef_name))
        return res

    def fun_fetch_details(self,cr,uid,ids,field,context=None):
        if (field):
            result = self.pool.get('vfsr.recruitment.process').read(cr, uid, field, ['vfsr_name','profession','locaton','mobile','name'], context)
            val = {'reef_name':result['vfsr_name'],'profession':result['profession'],'province':result['locaton'],'mobile':result['mobile'],'national_id':result['name'],}
            return {'value':val}

    def _get_team_name(self, csr, uid, context=None):
        lst = []
        csr.execute('select DISTINCT(name) from rb_sales_team')
        rows = csr.fetchall()
        #raise osv.except_osv(('warning'),(rows))
        for item in rows:
            toup = (str(item),str(item))
            lst.append(toup)
        return lst

    
    _columns = {
         'reef_name': fields.char("Name"),
         'parent':fields.many2one('vfsr.referral.process','Referrer'),
         'profession': fields.char("Profession"),
         'province' : fields.char("Location"),
         'mobile':fields.char('Mobile'),
         'national_id': fields.char('National ID'),
         'name' : fields.char("VFSR CODE"),
         'vfsr_inner_mapping': fields.many2one('vfsr.recruitment.process','Link with Existing Recruitment',domain="[('subdisposition','in',[45,47])]"),#
         #General  details
         'bank_side_id':fields.char('Bank Side-ID'),
         'date_updated':fields.datetime('Date Updated'),
         'personal_info': fields.one2many('personal.information', 'reference_id', 'Personal Information'),      #One2Many Field
         #Work Information
         'sales_team': fields.selection(_get_team_name,'Sales Team'),
         'team_leader': fields.many2one('res.users','TeamLeader'),
         'product_selection': fields.many2one('product.catagories','Product Selection'), #Permission Required
         #Qualification Information
         'reference2education': fields.one2many('vfsr.profile.education','relation2emp_profile','Education'),
	 'reference2job_profile' : fields.one2many('vfsr.profile.work.experience','rela2emp_prof','Work Experience'),
         'reference2address': fields.one2many('vfsr.profile.address','rela2emp_prof_main','Address'),
         #bank Details
         'bank_name': fields.char('Name'),
         'bank_branch':fields.char('Branch'),
         'bank_address':fields.char('Address'),
         'bank_acc_number':fields.char('Account Number'),
         'bank_ifsc':fields.char('IFSC code'),
         'bank_micr':fields.char('Micr Code'),
         'bank_branch_code':fields.char('Branch Code'),
         'bank_contact':fields.char('Contact Number'),

     }
vfsr_referral_process()

###############*********************************############################************************************************#####################






class personal_information(osv.osv):
    _name = "personal.information"
    _columns = {
                'name':fields.selection([('0','Self'),('1','Father'),('2','Mother'),('3','Sister'),('4','Wife'),('5','Siblings'),('6','Child'),('7','Reference')],"Type",size=64,),
                'mobile1':fields.char("Mobile"),
                'mobile2':fields.char("Alternative Number"),
                'email1':fields.char("Email"),
                'email2':fields.char("Alternate Email"),
                'dob':fields.char("Date OF Birth"),
                'family_book_no':fields.char("Family Book Number"), #HIDE FILTER
                'gender': fields.selection([('Male','Male'),('Female','Female')],'Gender'),#HIDE FILTER
                'married_status': fields.selection([('Married','Married'),('Single','Single')],'Marital Status'),#HIDE FILTER
                'hobby':fields.char("Hobby"),
                'signature':fields.char("Signature"),
                'reference_id' : fields.many2one('vfsr.referral.process','Link with form'),

        }
personal_information()

## Education Profile

class vfsr_profile_education(osv.osv):

	_name = "vfsr.profile.education"
	_columns = {
			'name' : fields.char('Course Name'),
			'board' : fields.char('Board'),
			'institute' : fields.char('Institute Name'),
			'ins_location' : fields.char('Institute Location'),
			'year_from': fields.integer('From'),
			'year_to': fields.integer('To'),
			'reference2subjects' : fields.one2many('vfsr.profile.education.subject','relation2education','Subjects'),
			'relation2emp_profile' : fields.many2one('vfsr.referral.process','VFSR reference Details',invisible=True)
			

		}
vfsr_profile_education()


## Class Subjects

class vfsr_profile_education_subject(osv.osv):

	_name = "vfsr.profile.education.subject"
	_columns = {
			'name': fields.char('Subject Name'),
			'total' : fields.float('Total Marks'),
			'obtain' : fields.float('Marks Obtain'),
			'relation2education' : fields.many2one('vfsr.profile.education','VFSR Education',invisible=True)
		}
	_defaults = {'total': 100.0,'obtain':0.0}

vfsr_profile_education_subject()


##Job History

class vfsr_profile_work_experience(osv.osv):
	
	_name = "vfsr.profile.work.experience"
	_columns = {
			'name': fields.char('Job Role'),
			'company_name' : fields.char('Company Name'),
			'company_address' : fields.char('Company Address'),
			'company_phone' : fields.char('Company Phone Number'),
			'year_from': fields.integer('Working From'),
			'year_to': fields.integer('Working To'),
			'reference_2_ref' : fields.one2many('vfsr.profile.work.reference','relation2exp','Company Reference'),
			'rela2emp_prof' : fields.many2one('vfsr.referral.process','VFSR reference Details',invisible=True)
			
		}
vfsr_profile_work_experience()


##Reference of previous company

class vfsr_profile_work_reference(osv.osv):

	_name = "vfsr.profile.work.reference"
	_columns = {
			'name' : fields.char('Reference Name'),
			'ref_address' : fields.char('Address'),
			'ref_cont' : fields.char('Cont. Number'),
			'ref_work' : fields.char('Company'),
			'ref_position' : fields.char('Position'),
			'relation2exp' : fields.many2one('vfsr.profile.work.experience','Work Experience',invisible=True)

		}
vfsr_profile_work_reference()


## Address

class vfsr_profile_address(osv.osv):
	
	_name = "vfsr.profile.address"
	_columns = {
			'name' : fields.selection([(1,'Permanent'),(0,'Temporary')],'Address Type'),
			'address1' : fields.char('Address1'),
			'address2' : fields.char('Address2'),
			'address3' : fields.char('Address3'),
			'ward' : fields.char('Ward'),
			'district' : fields.char('District'),
			'city' : fields.char('City'),
			'mobile' : fields.char('Mobile'),
			'rela2emp_prof_main' : fields.many2one('vfsr.referral.process','VFSR reference Details',invisible=True)
		}

vfsr_profile_address()












###############*********************************############################************************************************#####################


class inherit_batch(osv.osv):
    _inherit = 'rb.crm.batch.code'
    
    _columns = {
            'select_referrer' : fields.many2one('vfsr.referral.process','Referrer'),
        }



class inherit_vfsr_recruitment_process(osv.osv):
    _inherit = 'vfsr.recruitment.process'
    def name_get(self,cr,uid,ids,context=None):
        if context is None:
            context ={}
        res=[]
        record_name=self.browse(cr,uid,ids,context)
        for object in record_name:

                if object.name:
                    res.append((object.id,object.name+" / "+object.vfsr_name))
                else:
                    res.append((object.id,str(object.id)+" / "+object.vfsr_name))
        return res
    def write(self, cr, uid, ids, values, context = None): #NEW ADDITION
        res = super(inherit_vfsr_recruitment_process,self).write(cr, uid, ids, values, context = context)
        if (uid != 1):
            var = self.read(cr, uid,ids, ['create_uid'], context)
            #raise osv.except_osv(('warning'),(len(var)))
            #for elem in var:
            #raise osv.except_osv(('warning'),(elem['create_uid']))
            #tmp_cpr = elem['create_uid']
            #raise osv.except_osv(('warning'),(tmp_cpr,len(var)))
            #tmp_cpr = tmp_cpr[0]
            #raise osv.except_osv(('warning'),(var))
            k='Blank'
            if (type(var) is list):
                k = var[0]['create_uid'][0]
            else:
                k = var['create_uid'][0]
            if (int(k) == uid ):
            #if (int(elem[0])== int(uid) ):
                res = super(inherit_vfsr_recruitment_process,self).write(cr, uid, ids, values, context = context)
            else :
                raise osv.except_osv(('warning'),('You cannot edit This Lead'))
        return res


    _columns = {
                    'recruiters_team' : fields.many2one('vfsr.recruitment.team','Recruitment Team'),
         }

class vfsr_recruitment_team(osv.osv): #NEW ADDITION
    _name = "vfsr.recruitment.team"

    _columns = {
                'name' : fields.char('Team Name',),
                'description': fields.char('Description',),
                'team_leader' : fields.many2one('res.users','TeamLeader'),
                'team_member':fields.many2many('res.users','vfsr_recruitment_team_rel','team_id','res_users_id','Recruiters'),
                'active': fields.boolean('True'),
            }
    _defaults = {'active': True}
vfsr_recruitment_team()
