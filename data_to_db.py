import csv
from util import *
from consts import *
from table_schema import get_table_details
import io


def upload_data_to_db(uploaded_file):
    table_schema, columns = get_table_details()

    conn, c = connect_db()
    c.execute(table_schema)
    conn.commit()

    column_str = "("
    for col in columns:
        column_str = column_str + col + ", "

    column_str = column_str[:-2] + ")"

    col_str_var = "("
    col_str_var = col_str_var + ("%s, " * (len(columns)-1)) + "%s)"

    i = 0

    csvreader = csv.reader(uploaded_file.text.split('\n'), delimiter=',')

    next(csvreader)
    for row in csvreader:
        print(i)
        c.execute(
            f"INSERT INTO {table_name} {column_str} VALUES {col_str_var}",
            row
        )
        i = i + 1

    conn.commit()
    conn.close()
