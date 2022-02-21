import csv

header = ['name', 'area', 'country_code2', 'country_code3']
data = [
    ['Albania', 28748, 'AL', 'ALB'],
    ['Algeria', 2381741, 'DZ', 'DZA'],
    ['American Samoa', 199, 'AS', 'ASM'],
    ['Andorra', 468, 'AD', 'AND'],
    ['Angola', 1246700, 'AO', 'AGO']
]

with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)
    
    
with open('countries.csv', mode ='r') as f:
    csvFile = csv.reader(f)               # displaying the contents of the CSV file in list
    for lines in csvFile:
      print(lines)   
print("\n")
with open('countries.csv', mode ='r') as f:
    csvfile = csv.DictReader(f)  
    for line in csvfile:
      print(line)
    
import pandas
# csvFile = pandas.read_csv('university_records.csv', index_col = [1-2])
csvFile = pandas.read_csv('university_records.csv')
print(csvFile)