from osv import fields, osv
import time
import urllib

class announcement(osv.osv):
	_name = "announcement"
	_description = "announcement for TL"
	_columns ={
            'subject' : fields.char('Subject', size=100, required=True),
			'start_date' : fields.date('Start Date'),
			'end_date' : fields.date('End Date'),
            'messege' : fields.text('Messege'),
			'active' : fields.boolean('Active',required=True),
            }

announcement()
