
# IDS 706 Miniproject 2 - Jingxuan Li

This repository contains a project for database management and CRUD operations using SQLite, integrated with testing, logging, and a CI/CD pipeline for continuous integration and validation.

## Setup with VS Code and .devcontainer

Follow these steps to prepare and use your development environment:

### Prerequisites

- **Docker**: Ensure Docker is installed and running on your machine. [Download Docker](https://docs.docker.com/get-docker/).
- **Visual Studio Code**: Install VS Code if you haven't already. [Download VS Code](https://code.visualstudio.com/Download).
- **Remote - Containers Extension**: Install the **Remote - Containers** extension in VS Code by searching for it in the Extensions view (`Ctrl+Shift+X`).

### Getting Started

1. **Clone the Repository**:
   ```bash
   git clone git@github.com:Jourdan0803/ids-706-w5-jingxuan-li.git
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

### Logging of Database Operations

To monitor the progress of database operations, a log file `database_operations.log` is created. This file captures information about every successful operation and any encountered errors. Logs include details like table creation, data insertion, updates, deletions, and join operations. This helps with auditing, debugging, and maintaining a history of actions performed.

#### Example Log Output



## Continuous Integration (CI/CD Pipeline)

The project is integrated with a GitHub Actions CI/CD pipeline that runs the tests on every push or pull request to the main branch. This ensures the stability of the codebase and automatically validates new changes.

### Steps to Run CI/CD Pipeline

1. **GitHub Actions Workflow**:
   The CI/CD pipeline is defined in `.github/workflows/CICD.yml`. This file includes steps to:
   - Set up the Python environment.
   - Install required dependencies.
   - Run (`main.py`), which includes CRUD operations on the `.db` file.

2. **Pipeline Trigger**:
   - **Push to Main Branch**: Every time you push code to the main branch.
   - **Pull Request**: Every time a new pull request is opened against the main branch.

3. **Log and Validate**:
   You can check the GitHub Actions tab in your repository to see the logs of the pipeline run and ensure all tests pass successfully.

## Project Structure

Here is an overview of important files and directories in the repository:

- **`.devcontainer/`**: Contains Docker configuration files for setting up the development environment.
  - `Dockerfile`: Dockerfile to create a container with all dependencies installed.
  - `devcontainer.json`: Configuration file to define the development environment settings.
  
- **`.github/workflows/`**: Includes CI/CD pipeline configurations using GitHub Actions.
  - `CICD.yml`: Defines the GitHub Actions workflow for testing.

- **`Makefile`**: Defines scripts for common project tasks such as testing.
- **`README.md`**: Provides project documentation.
- **`mylib/lib.py`**: Contains the database functions (`connect_to_db`, `create_students_table`, `insert_students`, etc.).
- **`main.py`**: Main Python script to execute different database operations.
- **`test_main.py`**: test script of main.py.
- **`decriptive.ipynb`**: Jupyter Notebook for analysis and exploration.

## Available Commands in `main.py`

The following commands are available to interact with the SQLite database:

- `create_students`: Creates the students table in the database.
- `insert_students`: Inserts student records into the students table.
- `read_students_with_grade <grade>`: Reads students with a specific grade.
- `update_student_age <name> <increment>`: Updates a student's age by the given increment.
- `delete_student <name>`: Deletes a student by name.
- `create_classes`: Creates the classes table in the database.
- `insert_classes`: Inserts records into the classes table.
- `join_students_and_classes`: Performs a join between students and classes tables.

## How to Run

To run the `main.py` commands, use the following syntax:

```bash
python main.py
```

