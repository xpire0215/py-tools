import pymysql

class pystock:
    def __init__(self):
        pass

    def _connStart(self):
        self.connection = pymysql.connect(
            host='localhost', 
            user='pystock', 
            password='pystock', 
            db='pystock',
            charset='utf8'
        )

    def _connStop(self):
        self.connection.commit()
        self.connection.close()

    def list(self, code=0):
        self._connStart()
        
        if code == 0:
            sql = "SELECT code, name FROM interest_list"
        else:
            sql = "SELECT code, name FROM interest_list WHERE code={}".format(code)

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchone()
                print(result)
                cursor.close()              
        except:
            print("Query interest_list failure")
        
        self._connStop()

    def add(self, code):
        self._connStart()
        sql = "CREATE TABLE IF NOT EXISTS {} ( id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, price FLOAT NOT NULL, date DATE NOT NULL)".format("_" + code)
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)
                cursor.close()
        except:
            print("Create table failure")
        self._connStop()

    def delete(self, code):
        pass

    def average(self, code, days):
        pass

def main():
    t=pystock()
    t.list()
    t.add("1234")

if __name__ == "__main__":
    main()
