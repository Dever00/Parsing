from HH import get as hh_get
from Yandex import extract_jobs
from save import save_j
from read import read_job_csv

hh = hh_get()
ya = extract_jobs()
job = hh + ya
save_j(job)
read_job_csv()