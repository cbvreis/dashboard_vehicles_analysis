import sqlite3

import pandas as pd


class Database:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = sqlite3.connect(r"C:\Users\cassi\Desktop\CASSIO\05 - FORD\EL_VE-21-15_v1\db2.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute('PRAGMA foreign_keys = ON')
        self.connection.commit()

    def close(self):
        self.connection.close()

    def get_cursor(self):
        return self.cursor

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()

    def insert(self, table, data):
        keys = ', '.join(data.keys())
        values = ', '.join(['?'] * len(data))
        sql = 'INSERT INTO %s (%s) VALUES (%s)' % (table, keys, values)
        self.cursor.execute(sql, list(data.values()))

    def update(self, table, data, condition):
        sql = 'UPDATE %s SET ' % table
        for key in data:
            sql += '%s = ?, ' % key
            sql = sql[:-2] + ' WHERE ' + condition
        self.cursor.execute(sql, list(data.values()))

    def delete(self, table, condition):
        sql = 'DELETE FROM %s WHERE %s' % (table, condition)
        self.cursor.execute(sql)

    def select(self, table, condition):
        sql = 'SELECT * FROM %s WHERE %s' % (table, condition)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def select_all(self, table):
        sql = 'SELECT * FROM %s' % table
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def select_one(self, table, condition):
        sql = 'SELECT * FROM %s WHERE %s' % (table, condition)
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def select_column(self, table, column, condition):
        sql = 'SELECT %s FROM %s WHERE %s' % (column, table, condition)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def read_pandas(self):
        sql = """SELECT  * FROM decode d JOIN trips T ON D.vin_cd = T.Cod_Vin """
        return pd.read_sql(sql, self.connection)

    #def read_pandas_consumo(self):
    #    sql = """SELECT  * FROM decode d JOIN consumos C ON D.vin_cd = C.Cod_Vin """
    #    return pd.read_sql(sql, self.connection)

    def is_connected(self):
        return self.connection is not None
