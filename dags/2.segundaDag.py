import pendulum 
from airflow import DAG 
from airflow.operators.bash import BashOperator

with DAG (
    dag_id="segunda_dag",
    description="Minha segunda Dag",
    schedule=None,
    start_date=pendulum.datetime(2026, 1,1, tz="America/Sao_Paulo"),
    catchup=False,
    tags=["curso","exemplo"]
) as dag: 
    task1 = BashOperator(task_id="tsk1", bash_command="sleep 5")
    task2 = BashOperator(
    task_id="bash_task",
    bash_command='echo "Hi from bash operator"')
    task3 = BashOperator(task_id="tsk3", bash_command="ls ")
    task4 = BashOperator(task_id="tsk4", bash_command="pwd && ls -la")

task1 >> [ task2, task3 ] >> task4 