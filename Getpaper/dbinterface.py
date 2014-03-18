import datetime
import mysql.connector
from mysql.connector import errorcode


def connect_to_db():
    try:
        cnx = mysql.connector.connect(user='root', password='123456',
                                      host='127.0.0.1',
                                      database='test')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exists")
        else:
            print(err)

def add_to_main_paper():
    cnx = mysql.connector.connect(user='root', password='123456',
                                      host='127.0.0.1',
                                      database='test')
    cursor = cnx.cursor()

    main_paper = """INSERT INTO test.main_paper
                  (id,name,doi,publish_time,auth)
                  VALUES (%(id)s,%(name)s,%(doi)s,%(publish_time)s,%(auth)s)"""
    data_paper = {
        'id':1,
        'name':'libin',
        'doi':12345,
        'publish_time':'1982-12-3',
        'auth':'libin',
    }
    cursor.execute(main_paper,data_paper)
    cnx.commit()
    cursor.close()
    cnx.close()
