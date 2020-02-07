import pymysql

def main():
    conn = pymysql.connect(host='localhost', user='pystock', password='pystock', db='pystock')
    cur = conn.cursor()
    cur.execute("SHOW TABLES")
    for r in cur:
        print(r)
    cur.close()
    conn.close()

if __name__ == '__main__':
    main()
