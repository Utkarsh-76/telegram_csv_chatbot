from consts import client
import psycopg2
import csv
from consts import input_file_path


def call_openai(prompt, table_schema, top_entries, temperature=0):

    cols = f"""
    These are the schemas for products table along with 5 entries from the table with columns separated by (;):

    {table_schema}
    {top_entries}"""

    INITIAL_PROMPT = f"""
    {cols}

    I'll start prompting you and I want you to return SQL query.
    """

    response = client.chat.completions.create(
        model="datascience-gpt4",
        messages=[
            {"role": "system", "content": INITIAL_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=temperature,
        max_tokens=2000
    )

    return response.choices[0].message.content


def connect_db():
    # conn = psycopg2.connect(
    #     dbname='temp',
    #     user='postgres',
    #     password='postgres',
    #     host='localhost',
    #     port='5432'
    # )

    conn = psycopg2.connect(
        dbname='sample_database',
        user='first',
        password='password',
        host='localhost',
        port='5432'
    )

    c = conn.cursor()

    return conn, c


def save_csv(file_):

    rows = file_.text.split('\n')
    with open(input_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            writer.writerow(row.split(','))
