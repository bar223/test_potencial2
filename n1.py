import csv

with (open('students.csv', encoding='utf-8') as file):
    answer = list(csv.reader(file, delimiter=','))[1:]
    count_class = {}
    sum_class = {}
    for id, name, titleProject_id, level, score in answer:
        if 'Хадаров Владимир' in name:
            print(f"Ты получил: {score}, за проект - {titleProject_id}")
        count_class[level] = count_class.get(level, 0) + int(score != 'None')
        sum_class[level] = sum_class.get(level, 0) + (int(score) if score != 'None' else 0)
    for el in answer:
        if el[-1] == 'None':
            el[-1] = round(sum_class[el[-2]]/count_class[el[-2]],3)

with open('students_new.csv','w',encoding='utf-8',newline='') as file:
    w = csv.writer(file)
    w.writerow(['id','Name','titleProject_id','score'])
    w.writerows(answer)