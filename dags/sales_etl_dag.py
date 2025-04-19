from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd
import requests
import psycopg2

default_args = {
    'owner': 'gayathri',
    'start_date': datetime(2023, 1, 1),
    'retries': 1
}

def extract():
    df = pd.read_csv('/opt/airflow/data/sales_data.csv')
    df.to_csv('/opt/airflow/data/processed_sales.csv', index=False)

def load():
    conn = psycopg2.connect("dbname='salesdb' user='airflow' password='airflow' host='localhost'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS sales (product TEXT, quantity INT, price FLOAT)")
    df = pd.read_csv('/opt/airflow/data/processed_sales.csv')
    for _, row in df.iterrows():
        cur.execute("INSERT INTO sales (product, quantity, price) VALUES (%s, %s, %s)", 
                    (row['product'], row['quantity'], row['price']))
    conn.commit()
    cur.close()
    conn.close()

with DAG('sales_etl_dag', default_args=default_args, schedule_interval='@daily', catchup=False) as dag:
    extract_task = PythonOperator(task_id='extract', python_callable=extract)
    load_task = PythonOperator(task_id='load', python_callable=load)
    extract_task >> load_task
