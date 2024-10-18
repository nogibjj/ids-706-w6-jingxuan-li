from mylib.lib import load_csv_to_databricks, execute_complex_query
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def main():
    # Load WorldsBestRestaurants.csv
    print("Starting the program...")
    load_csv_to_databricks(
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
    print("Finished loading CSV to Databricks.")

    # Load RestaurantReviews.csv
    load_csv_to_databricks(
        csv_file_path="RestaurantReviews.csv",
        table_name="RestaurantReviews",
        columns_definition="""
            id INT,
            restaurant STRING,
            review_score DOUBLE,
            review_year INT
        """,
    )

    # Execute complex query
    execute_complex_query()


if __name__ == "__main__":
    main()
