import pandas as pd
import mysql.connector
from mysql.connector import Error

def load_csv_to_mysql(csv_file_path, host, user, password, \
                      database, table_name, create_table_sql, insert_sql):
    """
    Load data from a CSV file into a MySQL database table.

    Parameters:
    csv_file_path (str): The path to the CSV file.
    host (str): MySQL server host.
    user (str): MySQL username.
    password (str): MySQL password.
    database (str): Name of the database.
    table_name (str): Name of the table to insert data into.
    create_table_sql (str): The SQL query to create the table if it doesn't exist.
    insert_sql (str): The SQL query to insert data into the table.
    """
    try:
        # Load CSV file using pandas
        df = pd.read_csv(csv_file_path)

        # Establish a connection to MySQL (without specifying the database)
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()

            # Check if the database exists, create if not
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database};")
            print(f"Database '{database}' checked/created successfully.")
            
            # Use the newly created or existing database
            cursor.execute(f"USE {database};")

            # Create table if not exists
            cursor.execute(create_table_sql)
            print(f"Table '{table_name}' checked/created successfully.")

            # Insert data into the table
            for _, row in df.iterrows():
                cursor.execute(insert_sql, tuple(row))

            # Commit the transaction
            connection.commit()
            print(f"Data from {csv_file_path} \
                  has been successfully inserted into the database.")
            result = cursor.fetchall()
            return result
        
    except Error as e:
        print(f"Error: {e}")
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")


def execute_complex_query(host, user, password, database):
    """
    Execute a complex SQL query involving joins, aggregation, and sorting.
    
    Parameters:
    host (str): MySQL server host.
    user (str): MySQL username.
    password (str): MySQL password.
    database (str): Name of the database.
    """
    try:
        # Establish a connection to MySQL
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        
        if connection.is_connected():
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
            WHERE rv.review_year BETWEEN 2020 AND 2021
            GROUP BY r.restaurant, r.country, r.rank
            HAVING total_reviews > 3
            ORDER BY average_review_score DESC, r.rank ASC;
            """

            # Execute the query
            cursor.execute(query)

            # Fetch all the results
            result = cursor.fetchall()

            # Display the results
            print("Restaurant | Country | Rank | Total Reviews | \
                  Avg Review Score | Min Review Score | Max Review Score")
            print("-" * 90)
            for row in result:
                print(f"{row[0]} | {row[1]} | \
                      {row[2]} | {row[3]} | {row[4]} | {row[5]} | {row[6]}")
            return result

    except Error as e:
        print(f"Error: {e}")
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")
