import requests
from bs4 import BeautifulSoup

URL = 'https://yandex.ru/jobs/vacancies/?text=python'

def extract_block_job(html):
    title_row = html.find_all('div', {'class' : 'lc-styled-text'})
    company = title_row[0].get_text()
    link = html.find('a')['href']
    title = title_row[-2].get_text()
    return {'title' : title, 'company' : company, 'place' : '', 'link' : link}

def extract_jobs(): 
    jobs = []
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all('span', {'class' : 'lc-jobs-vacancy-card'})

    for res in results:
        job = extract_block_job(res)
        jobs.append(job)

    return jobs

