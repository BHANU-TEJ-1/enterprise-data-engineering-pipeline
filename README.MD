# Enterprise Data Engineering Pipeline

![Python](https://img.shields.io/badge/Python-3.12+-blue) ![Apache
Airflow](https://img.shields.io/badge/Apache-Airflow-red)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-blue)
![Docker](https://img.shields.io/badge/Docker-2496ED)

## Overview

A production-inspired Enterprise ETL pipeline implementing the **Bronze
→ Silver → Gold Medallion Architecture** using Python, PostgreSQL,
Apache Airflow, Docker, Pandas, SQLAlchemy and Parquet.

### Features

-   Multi-source ingestion (CSV, JSON, XML, PostgreSQL)
-   Bronze, Silver and Gold architecture
-   Validation, Cleaning, Standardization
-   Deduplication & Datatype Conversion
-   SCD Type 1 & Type 2
-   Apache Airflow orchestration
-   Dockerized deployment
-   PostgreSQL integration

## Architecture

``` text
CSV   JSON   XML   PostgreSQL
  \     |      |       /
   \    |      |      /
    ---- Ingestion ----
            |
         Bronze
            |
         Silver
            |
     Warehouse/Gold
            |
         Airflow
```

## Tech Stack

-   Python
-   Pandas
-   PostgreSQL
-   SQLAlchemy
-   Apache Airflow
-   Docker
-   Git & GitHub
-   Parquet

## Project Structure

``` text
enterprise-data-engineering-pipeline/
├── config/
├── dags/
├── data/
├── docs/
├── logs/
├── scripts/
├── src/
├── tests/
├── docker-compose.yaml
├── requirements.txt
├── .gitignore
└── README.md
```

## Running

``` bash
pip install -r requirements.txt
docker compose up -d
python -m scripts.build_bronze
python -m scripts.build_silver
python -m scripts.build_warehouse
```

Trigger **enterprise_pipeline** from Airflow.

## Airflow DAGs

-   bronze_pipeline
-   silver_pipeline
-   warehouse_pipeline
-   enterprise_pipeline

## Future Enhancements

-   Incremental Loading
-   CDC
-   Apache Spark
-   Azure Data Lake
-   Snowflake
-   dbt
-   Great Expectations
-   CI/CD

## Author

**Bhanu Tej**
