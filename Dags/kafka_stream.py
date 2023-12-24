from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner': 'airscholar',
    'start_date': datetime(2023, 12, 1, 10,00)

}

def stream_data_from_api():
    print('streaming data from api')
    import jason
    import requests



with DAG('user_automation',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

        stream_kafka = PythonOperator(
        task_id='stream_data_from_api',
        python_callable=stream_data_from_api,



