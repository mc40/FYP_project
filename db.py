import psycopg2

def db(host, uuid, dbname, password):
    conn_string = "host={0} user={1} dbname={2} password={3}".format(host, uuid, dbname, password)
    conn = psycopg2.connect(conn_string)

    cur = conn.cursor()
    cur.execute("select * from information_schema.tables where table_name=%s", ('movie',))
    if not bool(cur.rowcount):
        cur.execute("CREATE TABLE movie (id serial PRIMARY KEY, header VARCHAR(100), link VARCHAR(100), runtime VARCHAR(50), type VARCHAR(100));")
    print("Finished creating table")

    return cur