import psycopg

DB_NAME = "simple_rest"
DB_USER = "root"
DB_PASS = "secret"
DB_HOST = "localhost"
DB_PORT = "5432"


def run_sql(sql, call = ''):
    conn = None
    results = []

    try:
        conn=psycopg.connect(dbname=DB_NAME,
                        user=DB_USER,
                        password=DB_PASS,
                        host=DB_HOST,
                        port=DB_PORT)
        cur = conn.cursor(row_factory=psycopg.rows.dict_row)
        print(sql.as_string(cur))
        cur.execute(sql)
        conn.commit()

        if call == 'fetchone':
            results = cur.fetchone()
        elif call == 'fetchall':
            results = cur.fetchall()
        else:
            print('no need')
        cur.close()
    except (Exception, psycopg.DatabaseError) as error:
        print("Error in transction Reverting all other operations of a transction ", error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()
    return results