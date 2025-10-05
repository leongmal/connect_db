import pymysql
from config import host, user, password, db_name


try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )

    print("successfully connected...")
    print('#+'*10)

    try:
        # create table

        # with connection.cursor() as cursor:
        #     create_table_query = "CREATE TABLE users ("\
        #                         "id INT AUTO_INCREMENT,"\
        #                         "name varchar(10),"\
        #                         "password varchar(20),"\
        #                         "email varchar(20),"\
        #                         "title VARCHAR(100),"\
        #                         "PRIMARY KEY (id) )"
        
        #     cursor.execute(create_table_query)
        #     connection.commit()
        #     print("             Creat TABLE !!! Ok!")

        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO users (name, password, email, title) VALUES ('Anna','qwerty','3123@com','TOP')"
        #     cursor.execute(insert_query)
        #     connection.commit()
        
        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO users (name, password, email, title) VALUES ('Ivan','qwerty','ivan3@com','Hah')"
        #     cursor.execute(insert_query)
        #     connection.commit()

        #delete data
        # with connection.cursor() as cursor:
        #     delete_query = "DELETE FROM users WHERE  id = 5;"
        #     cursor.execute(delete_query)
        #     connection.commit()

        # drop table
        with connection.cursor() as cursor:
            drop_table = "DROP TABLE users;"
            cursor.execute(drop_table)
        


        #select all data from table
        with connection.cursor() as cursor:
            select_all_rows = "SELECT *FROM users"
            cursor.execute(select_all_rows)
            # cursor.execute("SELECT *FROM users")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print('$$'*10)

    finally:
        connection.close()


except Exception as ex:
    print("Connection refused...")
    print(ex)

