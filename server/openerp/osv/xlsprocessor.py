import xlrd
import xlwt
import osv

def get_pure_string(string):
    strp1 = ''
    try:
        step_1 = str(string).split("u'")[1]
        step_1 = step_1.replace("'","")
        if (step_1 == ''):
            step_1='Null'
    except Exception:
        step_1 = str(string).split(":")[1]
    return step_1


def process_xls(read_file,write_file,sheet_name,approx_row,lst_kies,default,name_field):
    #raise osv.except_osv(('Inside Processor'),(lst_kies))
    style_str = 'font: name Calibri, bold 1, height 220;pattern: pattern solid, fore_color 71;align: horiz CENTER,vert CENTER;borders: top thin, bottom thin, left thin, right thin'
    xls_file = read_file
    sd={}
    lst_row = []
    lst_formulae = []
    workbook = xlrd.open_workbook(xls_file)
    for s in workbook.sheets():
        sd[s.name]=s

    for key in sorted(sd.iterkeys()):
        sheet = sd[key]
        num_rows = sheet.nrows - 1
        curr_row = -1
        while curr_row < num_rows:
            curr_row += 1
            row = sheet.row(curr_row)
            lst_row.append(get_pure_string(row[0]))
            lst_formulae.append(get_pure_string(row[1]))
    for formule in lst_formulae:
        if (formule!='none'):
            var_formule_index = lst_formulae.index(formule)
            var_coros_column_name = lst_row[var_formule_index]
            #print var_coros_column_name +'  '+formule
    xls_file_to_write = write_file
    xls_sheet_name = sheet_name
    no_of_columns = 0
    no_of_employee = approx_row
    no_of_row = no_of_employee+1

    write_book = xlwt.Workbook() 
    write_sheet = write_book.add_sheet(xls_sheet_name)

    for row in range(0,no_of_row):
	#num_key = row
	print 'row  is ---'+str(row)
        for column in range (0,len(lst_row)):
            if (row < 1):
                write_sheet.col(column).width = 256 * 20
                write_sheet.write(row,column,lst_row[column],xlwt.easyxf(style_str))
            elif(row > 0):
                formule = lst_formulae[column]
                if(formule!='none'):
		    if '@'in formule:
			formule = formule.replace('@','')
			write_sheet.col(column).width = 256 * 20
			p_dict = lst_kies[row-1]
			if(formule == 'default'):
				#print default+'@@@@@@@@@@@@@@@@@@@@@@@@@@'
				write_sheet.write(row,column,default)
			elif(formule == 'name'):
                            for elem_kie in p_dict:
                                print 'Found One'
				if(elem_kie == formule):
				    #print str(p_dict[elem_kie])+'<<<<<<<<<'
                                    write_sheet.write(row,column,name_field +' of '+p_dict[elem_kie])
                        else:
				for elem_kie in p_dict:
					print 'Found One'
					if(elem_kie == formule):
						kfgd = p_dict[elem_kie]
						#print p_dict[elem_kie],'<------------------------------------------'
						try:
							write_sheet.write(row,column,p_dict[elem_kie])
						except:
							write_sheet.write(row,column,p_dict[elem_kie][1])

		    else:
                    	formule = formule.replace('#',str(row+1))
                    	write_sheet.col(column).width = 256 * 20
                    	write_sheet.write(row,column,xlwt.Formula(formule))
                                  
    write_book.save(xls_file_to_write)
    return lst_row

#process_xls('keybook.xls','Salary.xls','sheet1',30)

