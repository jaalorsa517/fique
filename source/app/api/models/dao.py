from mariadb import connect, Error
import app.config_db as cdb


def _connection():
    return connect(
        host=cdb.MYSQL_HOST,
        database=cdb.MYSQL_DATABASE,
        user=cdb.MYSQL_USER,
        password=cdb.MYSQL_PASSWORD,
    )


def getAll(table: str, columns: list):
    """
    Función que devuelve todos los elementos del recurso
    :param table->Nombre de la tabla a consultar
    :param columns->Lista de las columnas a consultar
    :return List(dict)-> Retorna una lista de diccionarios.
                    Retorna error en caso de fallo en conexion.
                    Retorna lista vacia no encuentra ninguna coicidencia.
    """
    data = []
    try:
        col = str.join(",", columns)
        cur = _connection().cursor()
        cur.execute(f"SELECT {col} FROM {table}")
        rows = cur.fetchall()
        if len(rows) > 0:
            for row in rows:
                data.append(dict(zip(columns, row)))
    except Error as e:
        return data.append(dict(error=str(e)))
    return data


def newResource(table: str, columns: list, data: list):
    """
    Funcion que crea un item en el recurso
    :param table->Nombre de la tabla a consultar
    :param columns->Lista de las columnas a crear
    :param data->Los datos a guardar
    :return boolean-> True si crea sin problemas
                    False si no pudo crear.
    """
    try:
        con = _connection()
        cur = con.cursor()
        cur.execute(
            f"INSERT INTO {table} ({str.join(',',columns)}) VALUES ({str.join(',',['?' for i in range(len(data))])})",
            data,
        )
        con.commit()
        return True
    except Error as e:
        return False


def updateResource(table: str, columns: list, data: list):
    """
    Funcion que actualiza un item en el recurso
    :param table->Nombre de la tabla a consultar
    :param columns->Lista de las columnas a modificar
    :param data->Los datos a modificar
    :return boolean-> True si crea sin problemas
                    False si no pudo crear.
    """
    try:
        con = _connection()
        cur = con.cursor()
        sql = f"UPDATE {table} SET {columns[0]} = ?"
        for i in range(1, len(columns) - 1):
            sql += f", {columns[i]} = ?"
        sql += f" WHERE {columns[len(columns)-1]} = {data[len(data)-1]}"
        # import pdb

        # pdb.set_trace()
        cur.execute(sql,data,)
        con.commit()
        return True
    except Error as e:
        return False


def deleteResource(table: str, column_id: str, id: int):
    """
    Funcion que crea un item en el recurso
    :param table->Nombre de la tabla a consultar
    :param columns_id->Nombre de la columna de la clave primaria
    :param id-> id de la columna primaria
    :return boolean-> True si crea sin problemas
                    False si no pudo crear.
    """
    try:
        con = _connection()
        cur = con.cursor()
        cur.execute(f"DELETE FROM {table} WHERE {column_id} = {id}")
        con.commit()
        return True
    except Error as e:
        return False
