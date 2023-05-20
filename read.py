import pandas as pd

def read_job_csv():
    pars = pd.read_csv('test_parsing.csv')
    print(pars.head())