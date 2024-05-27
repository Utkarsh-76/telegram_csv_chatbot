from util import *
import pandas as pd
from consts import *
import csv
from table_schema import get_table_details


def query_csv(user_prompt):

    data_list = []
    with open(input_file_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            data_list.append(';'.join(row))

    null_and_typecast = "Take care of Null Columns and cast the columns to proper datatypes if needed"

    table_schema, _ = get_table_details()
    first_query = call_openai(f"{user_prompt} {null_and_typecast}", table_schema, '\n'.join(data_list[:5]))
    print(first_query)

    conn, c = connect_db()

    try:
        df = pd.read_sql_query(first_query, conn)
    except Exception as e:
        query_error = ":".join(e.args[0].split(":")[1:])
        print(query_error)
        second_query = call_openai(
            f"getting the following error while running the query: {first_query}"
            f"<<<error>>>:"
            f"{query_error}\n\n"
            f"Take you time and think about it step by step. Give only the correct query as the output""", table_schema, '\n'.join(data_list[:5]))
        print(second_query)

        try:
            df = pd.read_sql_query(second_query, conn)
        except Exception as e:
            query_error = ":".join(e.args[0].split(":")[1:])
            print(query_error)
            third_query = call_openai(
                f"getting the following error while running the query: {second_query}"
                f"<<<error>>>:"
                f"{query_error}\n\n"
                f"Take you time and think about it step by step. Give only the correct query as the output""", table_schema, '\n'.join(data_list[:5]))
            print(third_query)

            try:
                df = pd.read_sql_query(third_query, conn)
            except Exception as e:
                query_error = ":".join(e.args[0].split(":")[1:])
                print(query_error)
                fourth_query = call_openai(
                    f"getting the following error while running the query: {third_query}"
                    f"<<<error>>>:"
                    f"{query_error}\n\n"
                    f"Take you time and think about it step by step. Give only the correct query as the output""", table_schema, '\n'.join(data_list[:5]))
                print(fourth_query)

                df = pd.read_sql_query(fourth_query, conn)

    conn.close()

    # if df.shape == (1, 1):
    #     return df.iloc[0][0]
    # else:
    return df


# question = """Give me the list of ACs of Voltas?"""
# answer = query_csv(question)
#
# print(answer)
#
# answer.to_csv('query.csv')
