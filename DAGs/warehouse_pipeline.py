"""
warehouse_pipeline.py

Warehouse Layer DAG.
"""

from airflow.decorators import dag, task

from datetime import datetime

from scripts.build_warehouse import main as build_warehouse


@dag(
    dag_id="warehouse_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["enterprise", "warehouse"],
)
def warehouse_pipeline():

    @task
    def warehouse():
        build_warehouse()

    warehouse()


warehouse_pipeline()