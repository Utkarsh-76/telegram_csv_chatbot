import psycopg2
from consts import table_name


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


conn, c = connect_db()

c.execute(f'''
    DROP TABLE {table_name}
''')

conn.commit()
conn.close()
