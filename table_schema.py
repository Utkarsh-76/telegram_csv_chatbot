import pandas as pd
from consts import *


def get_table_details():

    input_data = pd.read_csv(input_file_path)
    unnamed_cols = [col for col in input_data.columns if 'Unnamed' in col]
    input_data = input_data.drop(columns=unnamed_cols)
    input_data.columns = input_data.columns.str.replace(' ', '_')

    table_schema = f"CREATE TABLE {table_name} ( " + (' VARCHAR, '.join(input_data.columns)) + " VARCHAR);"

    return table_schema, input_data.columns
