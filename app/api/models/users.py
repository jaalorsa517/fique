from mariadb import connect, Error
import app.config_db as cdb

def getUser(nickname:str):
    response = dict()
    try:
        conn = connect(
            host = cdb.MYSQL_HOST,
            database = cdb.MYSQL_DATABASE,
            user = cdb.MYSQL_USER,
            password = cdb.MYSQL_PASSWORD
        )
        cur = conn.cursor()
        cur.execute(
            'SELECT nickname,password FROM users WHERE nickname = ?',(nickname,)
        )
        if cur.rowcount >= 0:
            user = cur.fetchone()
            response['nickname']= user[0]
            response['password']= user[1]

    except Error as e:
        response['error'] = str(e)

    finally:
        return response
