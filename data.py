import csv

file_name = r"C:\Users\user\OneDrive\Documents\Data_workbook.csv"
with open(file_name, 'r') as file_object: 
    csv_reader = csv.DictReader(file_object)

   #'''csv_reader = csv.reader(file_name) 
   #header_row = next(csv_reader)

   #for index, column in enumerate(header_row):
       #print(index, column)'''

    for rows in csv_reader:
        print(rows['First_name'], rows['Last_name'], rows['SSN'])