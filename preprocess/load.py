import os
import "../config.py"


def movie_lines(lines, dest_name):
	with open(lines,'rb') as tsv_in, open(os.path.join(config.CONFIG['PROCESSED'], dest_name), 'wb') as csv_out:
	    tsv_in = csv.reader(tsv_in, delimiter='\t')
	    csv_out = csv.writer(csv_out)
	    for row in tsv_in:
	    	try:
            	csvout.writerows(row[4])
            except:
            	pass