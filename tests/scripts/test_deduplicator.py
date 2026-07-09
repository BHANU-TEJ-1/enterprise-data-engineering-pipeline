import pandas as pd

from src.silver.deduplicator import Deduplicator


def main():

    deduplicator = Deduplicator()

    df = pd.DataFrame(
        {
            "customer_id": [101, 101, 102, 103, 103, 104],
            "customer_name": [
                "John",
                "John",
                "Alice",
                "Bob",
                "Bob",
                "David",
            ],
            "city": [
                "New York",
                "New York",
                "London",
                "Paris",
                "Paris",
                "Tokyo",
            ],
        }
    )

    print("\nOriginal DataFrame")
    print(df)

    # -----------------------------------------
    # Test 1
    # -----------------------------------------

    first_df = deduplicator.remove_duplicates(
        df,
        subset=["customer_id"],
        keep="first",
    )

    print("\nKeep First")
    print(first_df)

    # -----------------------------------------
    # Test 2
    # -----------------------------------------

    last_df = deduplicator.remove_duplicates(
        df,
        subset=["customer_id"],
        keep="last",
    )

    print("\nKeep Last")
    print(last_df)

    # -----------------------------------------
    # Test 3
    # -----------------------------------------

    remove_all_df = deduplicator.remove_duplicates(
        df,
        subset=["customer_id"],
        keep=False,
    )

    print("\nRemove All Duplicates")
    print(remove_all_df)

    # -----------------------------------------
    # Test 4
    # -----------------------------------------

    pipeline_df = deduplicator.deduplicate(
        df,
        subset=["customer_id"],
        keep="first",
    )

    print("\nPipeline Output")
    print(pipeline_df)


if __name__ == "__main__":
    main()