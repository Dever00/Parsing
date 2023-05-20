#Сохраняем все вакансии с двух сайтов в один CSV файл
import csv

def save_j(jobs):
    file = open('test_parsing.csv', mode='w')
    writer = csv.writer(file)
    writer.writerow(['title', 'company', 'place', 'link'])
    for job in jobs:
        writer.writerow(list(job.values()))
    
