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
            print("Execute SQL Failure")
        
        self._connStop()

    def add(self, code):
        pass

    def delete(self, code):
        pass

    def average(self, code, days):
        pass

def main():
    t=pystock()
    t.list()

if __name__ == "__main__":
    main()
