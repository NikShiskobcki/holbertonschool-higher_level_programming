#!/usr/bin/python3

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    MY_HOST = "localhost"
    MY_USER = argv[1]
    MY_PASS = argv[2]
    MY_DB = argv[3]
    STATE_NAME = argv[4]

try:
    db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB)
    cur = db.cursor()
    cur.execute("""SELECT cities.name
                FROM cities LEFT JOIN states ON cities.state_id = states.id
                WHERE states.name=%s
                ORDER BY cities.id ASC
                """, (STATE_NAME,))
    rows = cur.fetchall()
    ans = []
    for row in rows:
        ans.append(row[0])
    print(*ans, sep=', ')
    db.close()

except Exception:
    print("ERROR")
