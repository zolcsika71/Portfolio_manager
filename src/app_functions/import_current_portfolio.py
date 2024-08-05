import pandas as pd
import sqlite3


def run(excel_file_path, db_path, table_name):
    # Load the Excel file into a DataFrame
    df = pd.read_excel(excel_file_path)

    # Round percentage columns to 2 decimal places
    percentage_columns = [col for col in df.columns if 'percent' in col.lower()]
    df[percentage_columns] = df[percentage_columns].round(2)

    # Trim spaces from all string columns
    str_columns = df.select_dtypes(include=['object']).columns
    df[str_columns] = df[str_columns].apply(lambda x: x.str.strip())

    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)

    try:
        # Import the data into the specified table
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f"Data imported successfully into {table_name}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    excel_file_path = '../db/data_load/portfolio_diversification_starter.xlsx'
    db_path = '../db/investments.db'
    table_name = 'PORTFOLIO_CURRENT_TABLE'

    run(excel_file_path, db_path, table_name)



