
'''
Created on 25 ene. 2017

@author: jhon
'''

from datetime import date, timedelta as td
import datetime
import math
import time

import unittest

    


#datetime.datetime.today()
#datetime.datetime(2012, 3, 23, 23, 0, 0, 0)
#datetime.datetime.today().weekday()

#tiempoDeTrabajo=[date,date];
#tarifa=[10.5,12.5]
#tarifa=
#calcularPrecio(tarifa,tiempoDeServico):
#    print("algo")
def calcularPrecio(tarifa,tiempoDeServicio):
    
    if(tarifa[0]<0 or tarifa[1]<0):
        print("Las tarifas no tienen costo positivo")
        return 0
    d1 = tiempoDeServicio[0]
    d2 = tiempoDeServicio[1]
    d3 = tiempoDeServicio[0].date()
    d4 = tiempoDeServicio[1].date()
    
    delta = d4-d3
    #convertimos el tiempo a unix para obtener los minutos
    d1_ts = time.mktime(d1.timetuple())
    d2_ts = time.mktime(d2.timetuple())
    minutos = int(d2_ts-d1_ts) / 60
    if (minutos<15):
        return 0
    if(delta.days>=7):
        print("Tiempo de servicio invalido, tiene mas de 7 dias")
        return 0
    horas = [-1,-1,-1,-1,-1,-1,-1]
    for z in range(delta.days + 1):
        if(z==0):
            if(d1.day==d2.day):
                horas[z]=d2.hour-d1.hour
            else:
                horas[z]=24-d1.hour
        elif(z==delta.days):
            if(d2.minute>0):
                horas[z]=d2.hour+1
            else:
                horas[z]=d2.hour
        else:
            horas[z]=24
    costo=0
    for i in range(delta.days + 1):
        ahora = d1+ td(days=i)
        if(ahora.weekday()>=5):
            costo=costo+(tarifa[1]*horas[i])
        else:
            costo=costo+(tarifa[0]*horas[i]) 
    return costo
    
class TestCalc(unittest.TestCase):

    def test_Menor15(self):
        tarifa=[10.5,12.5]
        d1 = datetime.datetime(2017, 1, 23,3,15)
        d2 = datetime.datetime(2017, 1, 23,3,0)
        self.assertEqual(0,calcularPrecio(tarifa,[d1,d2]))
    def test_Mas7Dias(self):
        tarifa=[10.5,12.5]
        d1 = datetime.datetime(2017, 1, 23,3,15)
        d2 = datetime.datetime(2017, 1, 30,3,0)
        self.assertEqual(0,calcularPrecio(tarifa,[d1,d2]))
    def test_Casi8Dias(self):
        tarifa=[1,2]
        d1 = datetime.datetime(2017, 1, 23,0,0)
        d2 = datetime.datetime(2017, 1, 29,23,59)

        self.assertEqual(216,calcularPrecio(tarifa,[d1,d2]))
if __name__== '__main__':
    unittest.main()
    #main    

    
    

    