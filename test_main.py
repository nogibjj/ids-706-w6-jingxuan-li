from mylib.lib import load_csv_to_databricks, execute_complex_query
from unittest.mock import patch
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def test_load_csv_to_databricks():
    # Load sample CSV into Databricks
    test1 = load_csv_to_databricks(
        csv_file_path="WorldsBestRestaurants.csv",
        table_name="WorldsBestRestaurants",
        columns_definition="""
            id INT,
            year INT,
            `rank` INT,
            restaurant STRING,
            location STRING,
            country STRING,
            lat DOUBLE,
            lng DOUBLE
        """,
    )
    assert test1 == "Data inserted successfully"

    # Load RestaurantReviews.csv
    test2 = load_csv_to_databricks(
        csv_file_path="RestaurantReviews.csv",
        table_name="RestaurantReviews",
        columns_definition="""
            id INT,
            restaurant STRING,
            review_score DOUBLE,
            review_year INT
        """,
    )
    assert test2 == "Data inserted successfully"

    print("test_load_csv_to_databricks passed.")


@patch("databricks.sql.connect")
def test_query(mock_connect):
    test3 = execute_complex_query()
    assert test3 == "Query executed successfully"


if __name__ == "__main__":
    test_load_csv_to_databricks()
    test_query()
