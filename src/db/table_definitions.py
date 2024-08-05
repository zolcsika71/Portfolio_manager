# src/db/table_definitions.py


PORTFOLIO_CURRENT_TABLE = """
    CREATE TABLE IF NOT EXISTS PORTFOLIO_CURRENT_TABLE (
        ISIN TEXT
        Asset_class TEXT
        Asset TEXT
        Currency TEXT
        Percent REAL
    );
"""

PORTFOLIO_ERSTE_MARKET_TABLE = """
    CREATE TABLE IF NOT EXISTS PORTFOLIO_ERSTE_MARKET_TABLE (
        PORTFOLIO_NAME TEXT
        ISIN TEXT
        Asset_class TEXT
        Sub_class TEXT
        Asset TEXT
        Currency TEXT
        Percent REAL
        Currency Risk TEXT
        Sustainability TEXT
        YTD_Risk_Rating REAL
        Y1_Risk_Rating REAL
        Y3_Risk_Rating REAL
        Y5_Risk_Rating REAL
        Y1_SHARPE_RATING REAL
        Y3_SHARPE_RATING REAL
        Y5_SHARPE_RATING REAL
        Y1_VOLATILITY_RATING REAL
        Y3_VOLATILITY_RATING REAL
        INFO_RATIO_RATING REAL
        MAX_DRAWDOWN_RATING REAL
    );
"""

SQL_QUERIES = [PORTFOLIO_CURRENT_TABLE, PORTFOLIO_ERSTE_MARKET_TABLE]

