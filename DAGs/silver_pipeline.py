"""
silver_pipeline.py

Silver Layer DAG.
"""

from airflow.decorators import dag, task

from datetime import datetime

from scripts.build_silver import build_silver


@dag(
    dag_id="silver_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["enterprise", "silver"],
)
def silver_pipeline():

    @task
    def silver():
        build_silver()

    silver()


silver_pipeline()