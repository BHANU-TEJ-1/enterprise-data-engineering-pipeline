#it will be the single entry point that airflow can call
#Route requests to the appropriate reader and provide a unified interface

"""
ingestion_manager.py

Unified interface for enterprise data ingestion.
"""

from src.ingestion.csv_ingestion import read_csv
from src.ingestion.json_ingestion import read_json
from src.ingestion.xml_ingestion import read_xml
from src.ingestion.postgres_ingestion import read_table


def ingest(source_type: str, source: str):
    """
    Ingest data from a supported source.

    Parameters
    ----------
    source_type : str
        csv, json, xml or postgres

    source : str
        File path or table name.

    Returns
    -------
    pandas.DataFrame
    """

    source_type = source_type.lower()

    if source_type == "csv":
        return read_csv(source)

    if source_type == "json":
        return read_json(source)

    if source_type == "xml":
        return read_xml(source)

    if source_type == "postgres":
        return read_table(source)

    raise ValueError(f"Unsupported source type: {source_type}")