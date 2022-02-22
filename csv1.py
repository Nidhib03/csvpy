import csv
# field names
fields = ['Name', 'Branch', 'Year', 'CGPA']
# data rows of csv file
rows = [ ['Nik', 'COE', '2', '9.0'],['San', 'COE', '2', '9.1'],['Adi', 'IT', '2', '9.3'],['Sag', 'SE', '1', '9.5'],['Pia', 'MCE', '3', '7.8'],['Sam', 'EP', '2', '9.1']]
# name of csv file
filename = "university_records.csv"
# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    # writing the fields
    csvwriter.writerow(fields)
    # writing the data rows
    csvwriter.writerows(rows)
    

# # OR

# importing the csv module
import csv
	
# my data rows as dictionary objects
mydict =[{'branch': 'COE', 'cgpa': '9.0', 'name': 'n1', 'year': '2'},
		{'branch': 'COE', 'cgpa': '9.1', 'name': 'n2', 'year': '2'},
		{'branch': 'IT', 'cgpa': '9.3', 'name': 'n3', 'year': '2'},
		{'branch': 'SE', 'cgpa': '9.5', 'name': 'n4', 'year': '1'},
		{'branch': 'MCE', 'cgpa': '7.8', 'name': 'n5', 'year': '3'},
		{'branch': 'EP', 'cgpa': '9.1', 'name': 'n6', 'year': '2'}]
	
# field names
fields = ['name', 'branch', 'year', 'cgpa']
	
# name of csv file
filename = "university_records.csv"
	
# writing to csv file
with open(filename, 'w') as csvfile:
	# creating a csv dict writer object
	writer = csv.DictWriter(csvfile, fieldnames = fields)
		
	# writing headers (field names)
	writer.writeheader()
		
	# writing data rows
	writer.writerows(mydict)
