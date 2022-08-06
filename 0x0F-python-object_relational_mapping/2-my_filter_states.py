#!/usr/bin/python3

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    MY_HOST = "localhost"
    MY_USER = argv[1]
    MY_PASS = argv[2]
    MY_DB = argv[3]
    NAME = argv[4]

try:
    db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB)
    cur = db.cursor()
    query = """SELECT * FROM states
            WHERE name LIKE '{}'
            ORDER BY states.id ASC""".format(argv[4])
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    db.close()

except Exception:
    print("ERROR")
