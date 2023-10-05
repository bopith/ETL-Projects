# ETL Project: Extract, Transform, Load

## Overview

This Python project demonstrates a simple ETL (Extract, Transform, Load) process. 
It extracts data from a RESTful API, transforms it into a specific format, and loads it into a SQLite database. 
The project uses Python along with popular libraries such as Pandas, Requests, and SQLAlchemy.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)

## Requirements

To run this ETL project, you will need the following:

- Python (>= 3.6)
- Pandas (`pip install pandas`)
- Requests (`pip install requests`)
- SQLAlchemy (`pip install sqlalchemy`)

## Installation

1. Clone the repository to local machine:
    ```
    git clone https://github.com/your-username/etl-project.git
    ```

2. Navigate to the project directory:
    ```
    cd etl-project
    ```

3. Install the required Python packages:

    ```
    pip install -r requirements.txt
    ```

## Usage

To run the ETL process:
1. Open a command prompt or terminal window.
2. Navigate to the project directory.
3. Run the following command:
    ```
    python etl_pipeline.py
    ```

4. The ETL process will start, which includes the following steps:
- Extracting data from the [datausa.io](https://datausa.io) API.
- Transforming the data by cleaning and filtering it.
- Loading the transformed data into a SQLite database (`us_population.db`).

5. Upon successful completion, you will see the following message:
    ```
    ETL process completed successfully.
    ```

## Project Structure

The project directory contains the following files:
- `etl_pipeline.py`: The main Python script that performs the ETL process.
- `requirements.txt`: A text file listing the required Python packages.
- `README.md`: This documentation file.

