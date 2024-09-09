import logging

import pandas as pd
from zenml import step

@step(enable_cache=False)
def ingest_data(table_name: str) -> pd.DataFrame:
    """
    Read the data from sql database and return a pandas dataframe.

    Args:
    table_name: Name of the table to read from.
    """
    try:
        pass
    except Exception as e:
        logging.error(f"Error while reading the data from {table_name}")
        raise e


