import pandas as pd
import requests
from sqlalchemy import create_engine


def extract_data():
    '''
    Download the data from an api
    Return: json data
    '''
    try:
        url = "https://datausa.io/api/data?drilldowns=State&measures=Population"
        response = requests.get(url).json()
        data = response.get("data")
        print("Done extracting the data from an api.")
    except Exception as e:
        print("Data extract error: " + str(e))

    return data


def transform_data(data):
    '''
    Clean and transform the data to a specific format
    Return: cleaned dataset
    '''
    df = pd.DataFrame(data)

    # Change data type
    df = df.astype({"ID Year":"int","Year":"int", "Population":"int"})
    # Drop unwanted rows
    df = df[df["Year"] == 2020]
    print("Done transforming the data.")
    return df[["ID State", "State", "Year", "Population"]]


def load_data(df):
    '''
    Load the data into sqllite database
    '''
    try:
        disk_engine = create_engine('sqlite:///us_population.db')
        df.to_sql('etl_project', disk_engine, if_exists='replace')
        print("Done loading data into database. \n...")
    except Exception as e:
        print("Data load error: " + str(e))


def main():
    try:
        data = extract_data()
        df = transform_data(data)
        load_data(df)
        print("ETL process completed successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()