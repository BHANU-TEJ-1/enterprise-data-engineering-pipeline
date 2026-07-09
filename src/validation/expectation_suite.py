"""
expectation_suite.py

Defines validation rules for all enterprise datasets.
"""

EXPECTATION_SUITES = {

    "customers": {
        "primary_key": "customer_id",
        "not_null": [
            "customer_id"
        ],
        "unique": [
            "customer_id"
        ]
    },

    "orders": {
        "primary_key": "order_id",
        "not_null": [
            "order_id",
            "customer_id"
        ],
        "unique": [
            "order_id"
        ]
    },

    "payments": {
        "primary_key": None,
        "not_null": [
            "order_id",
            "payment_value"
        ],
        "greater_than_zero": [
            "payment_value"
        ]
    },

    "products": {
        "primary_key": "product_id",
        "not_null": [
            "product_id"
        ],
        "unique": [
            "product_id"
        ]
    },

    "sellers": {
        "primary_key": "seller_id",
        "not_null": [
            "seller_id"
        ],
        "unique": [
            "seller_id"
        ]
    },

    "reviews": {
        "primary_key": "review_id",
        "not_null": [
            "review_id"
        ],
        "unique": [
            "review_id"
        ]
    },

    "order_items": {
        "primary_key": None,
        "not_null": [
            "order_id",
            "order_item_id"
        ]
    },

    "geolocation": {
        "primary_key": None,
        "not_null": [
            "geolocation_zip_code_prefix"
        ]
    },

    "category_translation": {
        "primary_key": None,
        "not_null": [
            "product_category_name"
        ]
    }

}