import csv
with open('students.csv', encoding='utf8') as f:
    reader=csv.DictReader(f,delimiter=',',quotechar='"')
    data=sorted(reader,key=lambda x: (int(x['titleProject_id']) if x!='None' else 0))

id_project=input()
while id_project!='СТОП':
    fl=False
    for el in data:
        if el['titleProject_id']== id_project:
            sur,nam,pat=el['Name'].split()
            fl=True
            print(f"{id_project} Delal {sur} {nam}")
            break
    if not fl:
        print('ne naydeno')
    id_project=input()