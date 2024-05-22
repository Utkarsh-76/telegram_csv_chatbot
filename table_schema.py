import pandas as pd
from consts import *


def get_table_details():

    input_data = pd.read_csv(input_file_path)
    table_schema = f"CREATE TABLE {table_name} ( " + (' VARCHAR, '.join(input_data.columns)) + " VARCHAR);"

    return table_schema, input_data.columns
