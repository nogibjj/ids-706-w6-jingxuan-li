# main.py

from mylib.lib import load_csv_to_mysql, execute_complex_query


def main():
    # Load WorldsBestRestaurants.csv
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
    execute_complex_query(
        host="localhost",
        user="root",
        password="Jourdan980803..",
        database="restaurants",
    )


if __name__ == "__main__":
    main()
