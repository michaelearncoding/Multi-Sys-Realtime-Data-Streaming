# import requests
# res = requests.get("https://randomuser.me/api/")
# print(res.json()['results'][0])


#from airflow.operators.python import BranchPythonOperator

import uuid
from datetime import datetime
from airflow import DAG
#from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'airscholar',
    'start_date': datetime(2023, 9, 3, 10, 00)
}

def get_data():
    import requests

    res = requests.get("https://randomuser.me/api/")
    res = res.json()
    res = res['results'][0]

    return res