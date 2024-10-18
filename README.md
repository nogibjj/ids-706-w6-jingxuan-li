[![CI](https://github.com/nogibjj/ids-706-w6-jingxuan-li/actions/workflows/CICD.yml/badge.svg)](https://github.com/nogibjj/ids-706-w6-jingxuan-li/actions/workflows/CICD.yml)
# IDS 706 Miniproject 6 - Jingxuan Li

This repository contains a project for database management and CRUD operations using Databricks, integrated with Complex SQL Query.

## Setup with VS Code and .devcontainer

Follow these steps to prepare and use your development environment:

### Prerequisites

- **Docker**: Ensure Docker is installed and running on your machine. [Download Docker](https://docs.docker.com/get-docker/).
- **Visual Studio Code**: Install VS Code if you haven't already. [Download VS Code](https://code.visualstudio.com/Download).
- **Remote - Containers Extension**: Install the **Remote - Containers** extension in VS Code by searching for it in the Extensions view (`Ctrl+Shift+X`).

### Getting Started

1. **Clone the Repository**:
   ```bash
   git clone git@github.com:Jourdan0803/ids-706-w6-jingxuan-li.git
   ```

2. **Open in VS Code**:
   Open the cloned repository folder in Visual Studio Code.

3. **Reopen in Container**:
   When prompted in VS Code, click on "Reopen in Container" to start working inside a Docker container. Alternatively, use the Command Palette (`Cmd+Shift+P` on macOS or `Ctrl+Shift+P` on Windows/Linux) and select **Remote-Containers: Reopen Folder in Container**.

4. **Build Docker Image**:
   On the first launch in a container, Docker will build the development environment as specified in the `.devcontainer/Dockerfile`. This process may take a few minutes depending on your internet connection and computer speed.

5. **Development Environment Ready**:
   Once the container setup is complete, you will have a fully configured Python development environment ready for use.

## Running Tests

To ensure your code modifications function correctly, a suite of tests is included in this project.

1. **Open Terminal in VS Code**:
   Use the integrated terminal in VS Code (`Ctrl+``), ensuring you are at the project root directory.

2. **Execute Tests**:
   Run the tests using the Makefile command:
   ```bash
   make test
   ```

3. **Review Test Results**:
   Examine the output in the terminal to verify that all tests pass without errors.



## Project Structure

Here is an overview of important files and directories in the repository:

- **`.devcontainer/`**: Contains Docker configuration files for setting up the development environment.
  - `Dockerfile`: Dockerfile to create a container with all dependencies installed.
  - `devcontainer.json`: Configuration file to define the development environment settings.
  
- **`.github/workflows/`**: Includes CI/CD pipeline configurations using GitHub Actions.
  - `CICD.yml`: Defines the GitHub Actions workflow for testing.

- **`Makefile`**: Defines scripts for common project tasks such as testing.
- **`README.md`**: Provides project documentation.
- **`mylib/lib.py`**: Contains the database functions
- **`main.py`**: Main Python script to execute different database operations.
- **`test_main.py`**: test script of main.py.



## How to Run

To run the `main.py` commands, use the following syntax:

```bash
python main.py
```


### SQL Query Explanation

```sql
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
```

### Explanation

1. **SELECT Clause**:
   - This part of the query specifies the columns to be returned in the result set:
     - `r.restaurant`: The name of the restaurant.
     - `r.country`: The country where the restaurant is located.
     - `r.rank`: The rank of the restaurant.
     - `COUNT(rv.review_score) AS total_reviews`: The total number of reviews for each restaurant.
     - `AVG(rv.review_score) AS average_review_score`: The average score of the reviews.
     - `MIN(rv.review_score) AS min_review_score`: The minimum review score.
     - `MAX(rv.review_score) AS max_review_score`: The maximum review score.

2. **FROM Clause**:
   - The query retrieves data from two tables: `WorldsBestRestaurants` (aliased as `r`) and `RestaurantReviews` (aliased as `rv`).

3. **LEFT JOIN**:
   - This joins the `WorldsBestRestaurants` table with the `RestaurantReviews` table on the `restaurant` column. A LEFT JOIN ensures that all records from `WorldsBestRestaurants` are included, even if there are no matching records in `RestaurantReviews`.

4. **WHERE Clause**:
   - Filters the results to include only those reviews that were made between the years 2021 and 2022.

5. **GROUP BY Clause**:
   - Groups the results by `restaurant`, `country`, and `rank`. This is necessary for the aggregate functions (`COUNT`, `AVG`, `MIN`, `MAX`) to work correctly.

6. **HAVING Clause**:
   - Further filters the grouped results to include only those restaurants that have more than 1 reviews.

7. **ORDER BY Clause**:
   - Sorts the results first by `average_review_score` in descending order (highest scores first), and then by `rank` in ascending order (lowest ranks first).

### Expected Results

- The query will return a list of restaurants from the `WorldsBestRestaurants` table, along with their country, rank, and review statistics (total, average, minimum, and maximum scores) from the `RestaurantReviews` table.
- Only restaurants with more than 1 reviews between 2021 and 2022 will be included in the results.
- The results will be sorted by the average review score in descending order, so the highest-rated restaurants appear first. If two restaurants have the same average score, they will be sorted by their rank in ascending order.

This query is useful for analyzing the performance and popularity of top restaurants based on customer reviews over a specific period.
