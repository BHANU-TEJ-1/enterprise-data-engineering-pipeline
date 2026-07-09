"""
build_warehouse.py

Build all Gold Layer tables.
"""

import pandas as pd

from src.warehouse.warehouse_manager import WarehouseManager


def build_warehouse():

    manager = WarehouseManager()

    # ---------------------------------------
    # Read Silver Layer
    # ---------------------------------------

    customers = pd.read_parquet(
        "data/silver/customers.parquet"
    )

    products = pd.read_parquet(
        "data/silver/products.parquet"
    )

    sellers = pd.read_parquet(
        "data/silver/sellers.parquet"
    )

    geolocation = pd.read_parquet(
        "data/silver/geolocation.parquet"
    )

    orders = pd.read_parquet(
        "data/silver/orders.parquet"
    )

    order_items = pd.read_parquet(
        "data/silver/order_items.parquet"
    )

    payments = pd.read_parquet(
        "data/silver/payments.parquet"
    )

    # ---------------------------------------
    # Build Dimensions
    # ---------------------------------------

    print("Building Customer Dimension...")
    manager.build_customer_dimension(customers)

    print("Building Product Dimension...")
    manager.build_product_dimension(products)

    print("Building Seller Dimension...")
    manager.build_seller_dimension(sellers)

    print("Building Geolocation Dimension...")
    manager.build_geolocation_dimension(geolocation)

    # ---------------------------------------
    # Build Fact
    # ---------------------------------------

    print("Building Sales Fact...")
    manager.build_sales_fact(
        orders,
        order_items,
        payments,
    )

    print("\nGold Layer Built Successfully.")


if __name__ == "__main__":
    build_warehouse()

