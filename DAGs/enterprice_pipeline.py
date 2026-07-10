"""
enterprise_pipeline.py

Master Enterprise ETL Pipeline

Pipeline:

CSV / JSON / XML / PostgreSQL
            │
            ▼
      Bronze Layer
            │
            ▼
      Silver Layer
            │
            ▼
   Warehouse / Gold Layer
"""

from datetime import datetime

from airflow.decorators import dag, task

from scripts.build_bronze import build_bronze
from scripts.build_silver import build_silver
from scripts.build_warehouse import build_warehouse


@dag(
    dag_id="enterprise_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["enterprise", "etl", "bronze", "silver", "gold"],
)
def enterprise_pipeline():

    @task(task_id="build_bronze")
    def bronze_task():
        build_bronze()

    @task(task_id="build_silver")
    def silver_task():
        build_silver()

    @task(task_id="build_warehouse")
    def warehouse_task():
        build_warehouse()

    bronze = bronze_task()
    silver = silver_task()
    warehouse = warehouse_task()

    bronze >> silver >> warehouse


enterprise_pipeline()