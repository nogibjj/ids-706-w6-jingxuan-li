from mylib.lib import load_csv_to_mysql, execute_complex_query
from mysql.connector import Error
from unittest.mock import patch


def test_load_csv_to_mysql():
    # Load sample CSV into MySQL
    load_csv_to_mysql(
        csv_file_path="WorldsBestRestaurants.csv",
        host="localhost",
        user="root",
        password="Jourdan980803..",
        database="restaurants",
        table_name="WorldsBestRestaurants",
        create_table_sql="""
            CREATE TABLE IF NOT EXISTS WorldsBestRestaurants (
                year INT,
                `rank` INT,
                restaurant VARCHAR(255),
                location VARCHAR(255),
                country VARCHAR(255),
                lat DECIMAL(10, 6),
                lng DECIMAL(10, 6)
            );
        """,
        insert_sql="""
            INSERT INTO WorldsBestRestaurants \
                (year, `rank`, restaurant, location, country, lat, lng)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """,
    )

    # Load RestaurantReviews.csv
    load_csv_to_mysql(
        csv_file_path="RestaurantReviews.csv",
        host="localhost",
        user="root",
        password="Jourdan980803..",
        database="restaurants",
        table_name="RestaurantReviews",
        create_table_sql="""
            CREATE TABLE IF NOT EXISTS RestaurantReviews (
                restaurant VARCHAR(255),
                review_score DECIMAL(3, 2),
                review_year INT
            );
        """,
        insert_sql="""
            INSERT INTO RestaurantReviews (restaurant, review_score, review_year)
            VALUES (%s, %s, %s)
        """,
    )

    # Run the test to check if data is inserted successfully
    result = execute_complex_query(
        host="localhost",
        user="root",
        password="Jourdan980803..",
        database="restaurants",
    )

    # Assert the query result is not None
    assert result is not None, "The query should return results."

    # Assert the query returns at least one result
    assert len(result) > 0, "The query should return at least one row."

    assert isinstance(result[0][0], str), "Restaurant name should be a string."
    assert isinstance(result[0][1], str), "Country should be a string."
    assert isinstance(result[0][2], int), "Rank should be an integer."

    print("test_load_csv_to_mysql passed.")


def test_execute_complex_query():
    # Execute a complex SQL query and fetch the result
    result = execute_complex_query(
        host="localhost",
        user="root",
        password="Jourdan980803..",
        database="restaurants",
    )

    # Assert the result is not None
    assert result is not None, "The query should return results."

    # Assert that the query returns rows
    assert len(result) > 0, "The query should return at least one row."

    # Assert the result has the expected number of columns
    assert len(result[0]) == 7, "The result should have 7 columns."

    # Example: Assert specific fields
    for row in result:
        assert isinstance(row[0], str), "Restaurant name should be a string."
        assert isinstance(row[1], str), "Country should be a string."
        assert isinstance(row[2], int), "Rank should be an integer."
        assert row[3] > 3, "Total reviews should be greater than 3."
        assert 0 <= row[4] <= 10, "Average review score should be between 0 and 10."

    print("test_execute_complex_query passed.")


# New tests for error handling and connection closure
@patch("mysql.connector.connect", side_effect=Error("Connection failed"))
def test_load_csv_to_mysql_error_handling(mock_connect):
    # Test error handling by simulating a MySQL connection error
    result = load_csv_to_mysql(
        csv_file_path="WorldsBestRestaurants.csv",
        host="localhost",
        user="wrong_user",  # Simulated wrong credentials
        password="wrong_password",
        database="restaurants",
        table_name="WorldsBestRestaurants",
        create_table_sql="""
            CREATE TABLE IF NOT EXISTS WorldsBestRestaurants (...);
        """,
        insert_sql="""
            INSERT INTO WorldsBestRestaurants (...)
        """,
    )
    assert result is None  # Expect None when there is a connection failure

    print("test_load_csv_to_mysql_error_handling passed.")


@patch("mysql.connector.connect", side_effect=Error("Connection failed"))
def test_execute_complex_query_error_handling(mock_connect):
    # Test error handling by simulating a MySQL connection error
    result = execute_complex_query(
        host="localhost",
        user="wrong_user",  # Simulated wrong credentials
        password="wrong_password",
        database="restaurants",
    )
    assert result is None  # Expect None when there is a connection failure

    print("test_execute_complex_query_error_handling passed.")


if __name__ == "__main__":
    test_load_csv_to_mysql()
    test_execute_complex_query()
    test_load_csv_to_mysql_error_handling()
    test_execute_complex_query_error_handling()
