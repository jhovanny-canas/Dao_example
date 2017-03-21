
__author__ = 'jhovanny'

import psycopg2

class daoIntance():
    def __init__(self):
        self._user = 'postgres'
        self._pass = 'jhovanny'
        self._port = 5432
        self._database = 'bdPruebaViolencia'
        self._host = 'localhost'

    def getInstance(self):
        try:
            conexion =psycopg2.connect(host=self._host,user=self._user, password=self._pass, database=self._database)
            return conexion
        except Exception, e:
            print(str(e))






