from dotenv import load_dotenv
import os
import pandas as pd
from databricks import sql

# Load environment variables from .env file
load_dotenv()

def load_csv_to_databricks(csv_file_path, table_name, columns_definition):
    """
    Load data from a CSV file into a Databricks table using environment variables.
    """
    print("Starting load_csv_to_databricks function...")

    # Retrieve environment variables
    server_hostname = os.getenv('SERVER_HOSTNAME')
    http_path = os.getenv('HTTP_PATH')
    access_token = os.getenv('DATABRICKS_KEY')
    print(f"Environment variables loaded: SERVER_HOSTNAME={server_hostname}, \
          HTTP_PATH={http_path}")

    # Load CSV file using pandas
    print(f"Loading CSV file from path: {csv_file_path}")
    df = pd.read_csv(csv_file_path)
    print(f"CSV file loaded. Number of rows: {len(df)}")

    # Connect to Databricks SQL
    print("Connecting to Databricks SQL...")
    with sql.connect(server_hostname=server_hostname,
                     http_path=http_path,
                     access_token=access_token) as connection:
        print("Connection established.")
        cursor = connection.cursor()
        # cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
        print(f"Creating table {table_name} if it does not exist...")
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name}\
                        ({columns_definition});")
        print(f"Table {table_name} is ready.")
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        row_count = cursor.fetchone()[0]
        print(f"Current row count in {table_name}: {row_count}")
        # Create table if not exists
        if row_count == 0:
        # Insert data into the table
            print("Inserting data into the table...")
            for _, row in df.iterrows():
                placeholders = (_,) + tuple(row)
                cursor.execute(f"INSERT INTO {table_name} VALUES {placeholders}")
                if _ % 100 == 0:
                    print(f"Inserted {_} rows...")

            print(f"Data from {csv_file_path} has been successfully \
                  inserted into the table '{table_name}'.")
        return "Data inserted successfully"

def execute_complex_query():
    """
    Execute a complex SQL query involving joins, aggregation, and sorting on Databricks.
    """
    # Retrieve environment variables
    server_hostname = os.getenv('SERVER_HOSTNAME')
    http_path = os.getenv('HTTP_PATH')
    access_token = os.getenv('DATABRICKS_KEY')

    # Connect to Databricks SQL
    with sql.connect(server_hostname=server_hostname,
                     http_path=http_path,
                     access_token=access_token) as connection:
        cursor = connection.cursor()

        # Complex SQL query with JOIN, GROUP BY, HAVING, and ORDER BY
        query = """
            SELECT 
                r.restaurant,
                r.country,
                r.rank,
                COUNT(rv.review_score) AS total_reviews,
                AVG(rv.review_score) AS average_review_score,
                MIN(rv.review_score) AS min_review_score,
                MAX(rv.review_score) AS max_review_score
            FROM WorldsBestRestaurants r
            LEFT JOIN RestaurantReviews rv ON r.restaurant = rv.restaurant
            WHERE rv.review_year BETWEEN 2021 AND 2022
            GROUP BY r.restaurant, r.country, r.rank
            HAVING total_reviews > 1
            ORDER BY average_review_score DESC, r.rank ASC
        """

        # Execute the query
        cursor.execute(query)

        # Fetch all the results
        result = cursor.fetchall()

        # Display the results
        for row in result:
            print(row)
    return "Query executed successfully"