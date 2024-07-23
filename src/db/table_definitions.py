# src/db/table_definitions.py

INFO_TABLE = """
    CREATE TABLE IF NOT EXISTS Info (
        Cash INTEGER,
        EUR REAL,
        USD REAL
    );
"""

PORTFOLIO_CURRENT_TABLE = """
    CREATE TABLE IF NOT EXISTS Portfolio_current (
        ISIN TEXT(30),
        Asset_class TEXT(100),
        Asset TEXT(100),
        Currency TEXT(3),
        Percent REAL,
        HUF_invested INTEGER
    );
"""

PORTFOLIO_SUGGESTED_TABLE = """
    CREATE TABLE IF NOT EXISTS Portfolio_suggested (
        ISIN TEXT(30),
        Portfolio_type TEXT(100),
        Asset_class TEXT(100),
        Asset TEXT(100),
        Currency TEXT(3),
        Percent REAL,
        HUF_invested INTEGER
    );
"""

SELL_TABLE = """
    CREATE TABLE IF NOT EXISTS Sell (
        ISIN TEXT(30),
        Portfolio_type TEXT(100),
        Asset_class TEXT(100),
        Asset TEXT(100),
        Currency TEXT(3),
        Units REAL,
        Done INTEGER
    );
"""

BUY_TABLE = """
    CREATE TABLE IF NOT EXISTS Buy (
        ISIN TEXT(30),
        Portfolio_type TEXT(100),
        Asset_class TEXT(100),
        Asset TEXT(100),
        Currency TEXT(3),
        HUF_to_invest INTEGER,
        Done INTEGER
    );
"""

SQL_QUERIES = [INFO_TABLE, PORTFOLIO_CURRENT_TABLE, PORTFOLIO_SUGGESTED_TABLE, SELL_TABLE, BUY_TABLE]
