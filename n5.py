import csv

def hasher(s):
    alphabet='абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
    d={l: i for i, l in enumerate(alphabet,1)}
    p=67
    n=1e9+9
    hash_value=0
    p_pow=1
    for c in s:
        hash_value=(hash_value+d[c]*p_pow)%n
        p_pow=(p_pow*p)%n
    return int(hash_value)

stu_hash=[]
with open('students.csv',encoding='utf8') as f:
    reader=csv.DictReader(f,delimiter=',',quotechar='"')
    for row in reader:
        row['id']=hasher(row['Name'])
        stu_hash.append(row)
with open('students_hash','w',encoding='utf8',newline='') as f:
    w=csv.DictWriter(f, fieldnames=['id','Name','titleProject_id','class','score'])
    w.writeheader()
    w.writerows(stu_hash)
