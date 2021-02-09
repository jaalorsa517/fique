from typing import List
from mariadb import connect, Error
import app.config_db as cdb


def _connection():
    return connect(
        host=cdb.MYSQL_HOST,
        database=cdb.MYSQL_DATABASE,
        user=cdb.MYSQL_USER,
        password=cdb.MYSQL_PASSWORD,
    )


def getRaw(sql: str, columns: List):
    """
    Función que devuelve los datos solicitados
    :param sql-> Consulta manual
    :param columns-> Columnas que debera devolver la sentencia sql.
    :return List(dict)-> Retorna Lista de diccionarios.
                    Retorna error en caso de fallo en conexion.
                    Retorna lista vacia no encuentra ninguna coicidencia.
    """
    data = []
    try:
        rows = []
        with _connection().cursor() as cur:
            cur.execute(sql)
            rows = cur.fetchall()
        if len(rows) > 0:
            for row in rows:
                data.append(dict(zip(columns, row)))
        return data
    except Error as e:
        rows = [dict(error=e)]
        return rows


def getId(table: str, item: dict, id: str):
    """
    Función que devuelve el id de un recursos especifico
    :param table->Nombre de la tabla a consultar
    :param item->Diccionario columna=valor
    :param id->Nombre de la columna id
    :return int-> Retorna int.
                    Retorna error en caso de fallo en conexion.
                    Retorna lista vacia no encuentra ninguna coicidencia.
    """
    try:
        _id = []
        with _connection().cursor() as cur:
            cur.execute(
                "SELECT `{id}` FROM {table} WHERE {wh}".format(
                    id=id,
                    table=table,
                    wh=str.join(" AND ",
                                ["`{}` = ? ".format(k)
                                 for (k) in item.keys()]),
                ),
                list(item.values()),
            )
            _id = cur.fetchone()
        return _id[0]
    except Error as e:
        return None


def getWithJoin(table1: str, table2: str, column1: list, column2: list,
                keyUnion: str):
    """
    Función que devuelve todos los elementos del recurso
    :param table1->Nombre de la tabla a consultar
    :param table2->Nombre de la tabla a consultar
    :param column1->Lista de las columnas a consultar
    :param column2->Lista de las columnas a consultar
    :param keyUnion->Key relacionada
    :return List(dict)-> Retorna una lista de diccionarios.
                    Retorna error en caso de fallo en conexion.
                    Retorna lista vacia no encuentra ninguna coicidencia.
    """
    data = []
    try:
        rows = []
        col1 = str.join("`,`", column1)
        col2 = str.join("`,`", column2)
        with _connection().cursor() as cur:
            cur.execute(
                f"SELECT `{col1}`,`{col2}` FROM {table1} INNER JOIN {table2} ON {table1}.`{keyUnion}`={table2}.`f{keyUnion[1:]}`"
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
        rows = []
        col = str.join("`,`", columns)
        with _connection().cursor() as cur:
            cur.execute(f"SELECT `{col}` FROM {table}")
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
    :return dict-> Retorna un diccionario.
                    Retorna error en caso de fallo en conexion.
    """
    try:
        with _connection() as con:
            cur = con.cursor()
            cur.execute(
                f"INSERT INTO {table} (`{str.join('`,`',columns)}`) VALUES ({str.join(',',['?' for i in range(len(data))])})",
                data,
            )
            con.commit()
            cur.execute("SELECT @@identity AS id")
            id = cur.fetchone()
        return dict(id=id[0])
    except Error as e:
        return dict(error=str(e))


def updateResource(table: str, columns: list, data: list, id: dict):
    """
    Funcion que actualiza un item en el recurso
    :param table->Nombre de la tabla a consultar
    :param columns->Lista de las columnas a modificar. Debe incluir el id al final
    :param data->Los datos a modificar. Debe incluir el id al final
    :return boolean-> True si crea sin problemas
                    False si no pudo crear.
    """
    try:
        with _connection() as con:
            cur = con.cursor()
            sql = f"UPDATE {table} SET `{columns[0]}` = ?"
            for i in range(1, len(columns) - 1):
                sql += f", `{columns[i]}` = ?"
            sql += f" WHERE {list(id.keys())[0]} = {id[list(id.keys())[0]]}"
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
    Funcion que borra un recurso
    :param table->Nombre de la tabla a consultar
    :param columns_id->Nombre de la columna de la clave primaria
    :param id-> id de la columna primaria
    :return boolean-> True si crea sin problemas
                    False si no pudo crear.
    """
    try:
        with _connection() as con:
            cur = con.cursor()
            cur.execute(f"DELETE FROM {table} WHERE {column_id} = {id}")
            con.commit()
        return True
    except Error as e:
        return False
