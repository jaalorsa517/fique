from mariadb import connect, Error
import app.config_db as cdb


def _connection():
    return connect(
        host=cdb.MYSQL_HOST,
        database=cdb.MYSQL_DATABASE,
        user=cdb.MYSQL_USER,
        password=cdb.MYSQL_PASSWORD,
    )


def getId(table: str, item: dict, id: str):
    """
    Función que devuelve el id de un recursos especifico
    :param table->Nombre de la tabla a consultar
    :param item->Diccionario columna=valor
    :param id->Nombre de la columna id
    :return List(dict)-> Retorna int.
                    Retorna error en caso de fallo en conexion.
                    Retorna lista vacia no encuentra ninguna coicidencia.
    """
    try:
        cur = _connection().cursor()
        cur.execute(
            "SELECT {id} FROM {table} WHERE {wh}".format(
                id=id,
                table=table,
                wh=str.join(" AND ", ["{} = ? ".format(k) for (k) in item.keys()]),
            ),
            list(item.values()),
        )
        id = cur.fetchone()
        return id[0]
    except Error as e:
        return None


def getWithJoin(table1: str, table2: str, column1: list, column2: list, keyUnion: str):
    """
    Función que devuelve todos los elementos del recurso
    :param table->Nombre de la tabla a consultar
    :param column1->Lista de las columnas a consultar
    :param column2->Lista de las columnas a consultar
    :param keyUnion->Key relacionada
    :return List(dict)-> Retorna una lista de diccionarios.
                    Retorna error en caso de fallo en conexion.
                    Retorna lista vacia no encuentra ninguna coicidencia.
    """
    data = []
    try:
        col1 = str.join(",", column1)
        col2 = str.join(",", column2)
        cur = _connection().cursor()
        cur.execute(
            f"SELECT {col1},{col2} FROM {table1} INNER JOIN {table2} ON {table1}.{keyUnion}={table2}.f{keyUnion[1:]}"
        )
        rows = cur.fetchall()
        if len(rows) > 0:
            for row in rows:
                data.append(dict(zip(column1 + column2, row)))
    except Error as e:
        return data.append(dict(error=str(e)))
    return data


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
        cur.execute(
            sql,
            data,
        )
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
