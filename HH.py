import requests
from bs4 import BeautifulSoup

URL = f'https://hh.ru/search/vacancy?text=python&items_on_page=100'
headers = {
    'Host' : 'hh.ru',
    'User-Agent' : 'Safari',
    'Accept' : '*/*',
    'Accept-Encoding' : 'gzip, deflate, br',
    'Connection' : 'keep-alive'}

def extract_page():
    hh_request = requests.get(URL, headers = headers)
    soup = BeautifulSoup(hh_request.text, 'html.parser')
    paginator = soup.find_all('span', {'class' : 'pager-item-not-in-short-range'})
    #забираем ссылку и номер страницы
    pages = []
    for page in paginator:
        pages.append(int(page.find('a').text))
    return pages[-1]

def extract_job_html(html):
    title = html.find('a').text
    link = html.find('a')['href']
    company = html.find('div', {'class' : 'vacancy-serp-item__meta-info-company'}).text
    company = company.strip()
    place = html.find('div', {'data-qa' : 'vacancy-serp__vacancy-address'}).text
    place = place.partition(',')[0]
    return {'title' : title, 'company' : company, 'place' : place, 'link' : link}#
    
def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        
        result = requests.get(f'{URL}&page={page}', headers = headers)
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all('div', {'class' : 'vacancy-serp-item-body'})
        
        for result in results:
            job = extract_job_html(result)
            jobs.append(job)
    return jobs


def get():
    max_page = extract_page()
    jobs = extract_jobs(max_page)
    return jobs