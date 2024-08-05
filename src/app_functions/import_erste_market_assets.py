import pandas as pd
import sqlite3


def run(excel_file_path, db_path, table_name):
    # Load the specific worksheet into a DataFrame
    df = pd.read_excel(excel_file_path, sheet_name='modell portfóliók')

    # Rename the columns according to the specified mapping
    column_mapping = {
        'ISIN': 'ISIN',
        'Eszközosztály': 'Asset_class',
        'Aleszközosztály': 'Sub_class',
        'Termék': 'Asset',
        'Deviza': 'Currency',
        'Hányad (%)': 'Percent',
        'Devizakockázat': 'Currency_Risk',
        'Fenntarthatóság': 'Sustainability',
        'YTD': 'YTD_Risk_Rating',
        '1yr': 'Y1_Risk_Rating',
        '3yr': 'Y3_Risk_Rating',
        '5yr': 'Y5_Risk_Rating',
        '1Y Sharpe': 'Y1_SHARPE_RATING',
        '3Y Sharpe': 'Y3_SHARPE_RATING',
        '5Y Sharpe': 'Y5_SHARPE_RATING',
        '1Y Vol.': 'Y1_VOLATILITY_RATING',
        '3Y Vol.': 'Y3_VOLATILITY_RATING',
        'Info. ratio': 'INFO_RATIO_RATING',
        'Max. drawd.': 'MAX_DRAWDOWN_RATING'
    }

    df = df.rename(columns=column_mapping)

    # Select only the specified columns
    columns_to_import = list(column_mapping.values())
    df = df[columns_to_import]

    # Round percentage columns to 2 decimal places
    df['Percent'] = df['Percent'].round(2)

    # Trim spaces from all string columns
    str_columns = df.select_dtypes(include=['object']).columns
    df[str_columns] = df[str_columns].apply(lambda x: x.str.strip())

    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)

    try:

        # Import the data into the specified table
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f"Data imported successfully from {excel_file_path} into {table_name}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    excel_file_path = '../db/data_load/PB_Modell_Portfoliok_es_Shortlist_20240718.xls'
    db_path = '../db/investments.db'
    table_name = 'PORTFOLIO_ERSTE_MARKET_TABLE'

    run(excel_file_path, db_path, table_name)
