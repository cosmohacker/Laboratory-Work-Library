from mysql.connector import MySQLConnection
from utils import temp

conn = temp.conn


class Show:
    @staticmethod
    def show_records(table):
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table}")
        datas = cursor.fetchall()
        rows = []
        for row in datas:
            rows.append(row)
        return rows

    @staticmethod
    def get_column(table, column, target, value):
        cursor = conn.cursor()
        cursor.execute(f"SELECT {column} FROM {table} WHERE {target} = '{value}'")
        data = cursor.fetchone()
        return data[0] if data else None

    @staticmethod
    def get_record(table, column, target, value):
        cursor = conn.cursor()
        cursor.execute(f"SELECT {column} FROM {table} WHERE {target} = '{value}'")
        data = cursor.fetchone()
        return data if data else None


    @staticmethod
    def show_records_paginate(table_name, offset, limit, target):
        cursor = conn.cursor()
        if target == '':
            cursor.execute(f"SELECT * FROM {table_name} LIMIT %s, %s", (offset, limit))
        else:
            cursor.execute(f"SELECT * FROM {table_name} WHERE Type = '{target}' LIMIT %s, %s", (offset, limit))
        datas = cursor.fetchall()
        rows = []
        for row in datas:
            rows.append(row)
        return rows

    @staticmethod
    def search_records_paginate(table, search_input, offset, limit):
        cursor = conn.cursor()
        if table == 'Librarian':
            table = 'Administrator'
        cursor.execute(f"SHOW COLUMNS FROM {table}")
        columns = [column[0] for column in cursor.fetchall()]
        search_conditions = " OR ".join([f"{column} LIKE '%{search_input}%'" for column in columns])
        query = f"SELECT * FROM {table} WHERE {search_conditions}"
        cursor.execute(query)
        results = cursor.fetchall()
        rows = []
        for row in results:
            rows.append(row)
        return rows

    @staticmethod
    def show_specified_record(table, target):
        cursor = conn.cursor()
        target_columns = ' AND '.join(f"{col} = %s" for col in target)
        cursor.execute(f"SELECT * FROM {table} WHERE {target_columns}", tuple(target.values()))
        rows = list(cursor.fetchall())
        return rows

    @staticmethod
    def get_columns(table):
        if table == 'Librarian':
            table = 'Administrator'
        cursor = conn.cursor()
        cursor.execute(f"SHOW COLUMNS FROM {table}")
        columns = [column for column in cursor.fetchall()]
        return columns

    @staticmethod
    def count_rows(table):
        if table == 'Librarian':
            table = 'Administrator'
        cursor = conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        total_rows = cursor.fetchone()[0]
        return total_rows


class Insert:

    @staticmethod
    def insert_record(table, data):
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        values = tuple(data.values())
        cursor = conn.cursor()
        cursor.execute(sql, values)
        temp.conn.commit()
        return cursor.lastrowid


class Update:

    @staticmethod
    def alter_record(table, data, target):
        cursor = conn.cursor()
        columns = ', '.join([f"{col} = %s" for col in data.keys()])
        target_columns = ' AND '.join([f"{col} = %s" for col in target.keys()])
        values = list(data.values()) + list(target.values())
        sql = f"UPDATE {table} SET {columns} WHERE {target_columns}"
        cursor.execute(sql, values)
        temp.conn.commit()
        return cursor.lastrowid


class Delete:

    @staticmethod
    def delete_record(table, column_name,value):
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {table}  WHERE {column_name} = '{value}'")
        temp.conn.commit()
        return cursor.rowcount
