import csv
import string
import random

def ini(s):
    name=s.split()
    return f'{name[0]}_{name[1][0]}{name[2][0]}'
def parol():
    st=string.ascii_lowercase
    za=string.ascii_uppercase
    ci=string.digits
    par=random.choice(st)+random.choice(za)+random.choice(ci)
    for _ in range(5):
        par+=random.choice(st+za+ci)
    return par

stu_new=[]
with open('students.csv',encoding='utf8') as f:
    reader=csv.DictReader(f,delimiter=',',quotechar='"')
    for el in reader:
        el['login']=ini(el['Name'])
        el['password']=parol()
        stu_new.append(el)

with open('students_passwords.csv','w',encoding='utf8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['id','Name','titleProject_id','class','score','login','password'])
    w.writeheader()
    w.writerows(stu_new)