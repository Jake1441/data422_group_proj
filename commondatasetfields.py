import csv

def load_dataset(f_name):
    with open(f_name, newline='') as csvfile:
        field_reader = csv.reader(csvfile, delimiter=',')
        row1 = next(field_reader)
        return row1

f_name = "Crash_Analysis_System_(CAS)_data.csv"
CAS = load_dataset(f_name)

f_name = "NZTA_Highway_Information.csv"
NZTAH = load_dataset(f_name)

fields = []

for data in CAS:
    if data in NZTAH:
        fields.append(data)

print(fields)

# common fields
# ['\ufeffX', 'Y', 'OBJECTID']