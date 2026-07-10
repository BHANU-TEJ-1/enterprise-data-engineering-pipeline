"""
bronze_pipeline.py

Bronze Layer DAG.
"""

from airflow.decorators import dag, task

from datetime import datetime

from scripts.build_bronze import build_bronze


@dag(
    dag_id="bronze_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["enterprise", "bronze"],
)
def bronze_pipeline():

    @task
    def bronze():
        build_bronze()

    bronze()


bronze_pipeline()