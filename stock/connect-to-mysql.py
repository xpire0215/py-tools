import pymysql

def main():
    connection = pymysql.connect(
            host='localhost', 
            user='pystock', 
            password='pystock', 
            db='pystock',
            charset='utf8'
    )
    
    company_name = '\'台積電\''

    # INSERT Method
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `interest_list` (`code`, `name`) VALUES (2330, {})".format(company_name)
            cursor.execute(sql)
            connection.commit()
    except:
        print("Insert table failure")

'''
    # QUERY Method    
    try:
        with connection.cursor() as cursor:
            sql = "SHOW TABLES"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
            cursor.close()              
    except:
        print("Execute SQL Failure")
    
    connection.close()
'''

if __name__ == '__main__':
    main()
