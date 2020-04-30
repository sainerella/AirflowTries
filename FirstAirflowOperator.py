import airflow

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import date, timedelta, datetime

args = {
    'owner': 'airflow'
             'depends_on_past'
}


def test_dag_python():
    print('In First Airflow Operator')


dag = DAG(
    dag_id='print_date_dag',
    schedule_interval='* * * * 5',
    start_date=datetime(2020, 4, 21),
    default_args=args,
    catchup=False
)

my_python_op = PythonOperator(task_id='test_dag_python', python_callable=test_dag_python, dag=dag)

dummy_op = DummyOperator(task_id='dummy_task', dag=dag)
