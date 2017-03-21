from jhovanny.dao import daoInstance
from jhovanny.dao import dtoHechos
from jhovanny.entities import victima, agresor
import pyodbc
import os

__author__ = 'jhovanny'

dao = daoInstance.daoIntance()
cone = dao.getInstance()

cursor = cone.cursor()
cursor.execute('select * from etnia')

conectionString = r"DRIVER={Microsoft Excel Driver (*.xls, *.xlsx, *.xlsm, *.xlsb)};DBQ=" + os.getcwd() + "\\Examen-Rutas.xlsx"
cnxn = pyodbc.connect(conectionString, autocommit=True)

hechos = dtoHechos.dtohecho()

cr = cnxn.cursor()
registros = cr.execute('select * from [Original$]').fetchall()
for reg in registros:
    try:
        if reg[108] == 'ANTIOQUIA' and reg[109] == 'MEDELLIN':
            if reg[19] == 'S':
                regimen = 4
        elif reg[19] == 'C':
            regimen = 3
        elif reg[19] == 'E':
            regimen = 2
        elif reg[19] == 'I':
            regimen = 6
        elif reg[19] == 'N':
            regimen = 5
        else:
            regimen = 6
        if reg[8]=='M':
            sexo=1
        else:
            sexo=2
        victi = victima.victima(
            int(reg[114]), reg[51], 1, int(reg[60]), int(reg[61]), int(reg[62]), int(reg[63]), int(reg[64]), int(reg[65]),
                int(reg[66]), int(reg[67]),
                int(reg[68]), int(reg[69]), int(reg[70]), int(reg[71]), int(reg[72]), 2, int(reg[44]), reg[45], int(reg[6]),
                int(reg[7]), sexo,
                regimen, int(reg[21]),  1, reg[17],int(reg[35]))
        # se insertan las victimas
        hechos.insertarpersona(victi)

        if reg[74]=='M':
            sexo=1
        else:
            sexo=2


        if(reg[76]==''):
            val2=0
        else:
            val2=int(reg[76])

        if(reg[77]==''):
            val3=0
        else:
            val3=int(reg[77])

        if(reg[78]==''):
            val4=0
        else:
            val4=int(reg[78])

        #insertalos agresores
        agres = agresor.agresor(int(reg[73]),sexo, int(reg[75]), val3,val2, val4)
        hechos.insertaragresor(agres)


    #tabla hecho violento


    except Exception, e:
        print(str(e))
        continue


""" se creo modelo con las dimensiones victima,tiempo,agresor caa uno con un buen nivel de granularidad e integridad relacional, la tabla hechos violentos es
la de hechos, donde se toaliza cada unos de las variables asociadas al evento, su atencion sanitaria y disposicion, se puede desagregar mas, pero falta algo mas de tiempo"""




