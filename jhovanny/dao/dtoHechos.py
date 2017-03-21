__author__ = 'jhovanny'
import daoInstance



class dtohecho():
    def __init__(self):
        dao = daoInstance.daoIntance()
        self._conexion = dao.getInstance()

    def listarTabla(self, tabla):
        cursor = self._conexion.cursor();
        sql = "select * from %s" % tabla
        cursor.execute(sql)
        return cursor.fetchall()

    def insertarpersona(self, persona):
        cursor = self._conexion.cursor()
        try:
            sql = "insert into victima values (%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            datos = (
            persona.id, persona.nombresApellidos, persona.tipoid, persona.actividad, persona.lgtbi, persona.consumosps,
            persona.trabajadorSex, persona.desmovilizado, persona.campesino, persona.mujercabeza, persona.amacasa,
            persona.nnanbf, persona.privadolibertad, persona.victimaconflicto, persona.reincidencia, persona.alcohol,
            persona.otro, persona.telefono, persona.fechanacimienot, persona.edad, persona.unidadmedida, persona.sexo,
            persona.regimen, persona.etnia, persona.grupopoblacional, persona.direccion, persona.municipio)
            cursor.execute(sql, datos)
            self._conexion.commit()
        except Exception, e:
            self._conexion.rollback()




    def insertaragresor(self, agre):
        cursor = self._conexion.cursor()
        try:
            sql = "insert into agresor(edad,sexo,parentescoVictima, agresorNoFamiliar, convive,grupoPerpetrador) values (%s,%s,%s,%s,%s,%s)"
            datos = (agre.edad,agre.sexo,agre.parentescovictima,agre.agresornofamiliar, agre.convive,agre.grupoperpetrador)
            cursor.execute(sql, datos)
            self._conexion.commit()
        except Exception, e:
            self._conexion.rollback()







