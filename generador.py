"""
Un generador de senal es el responsable de generar una senal portadora.

"""
import numpy as np
class Generador(object):

    def __init__(self, amplitud, fase, frecuencia):
        self.amplitud = amplitud
        self.fase = fase
        self.frecuencia = frecuencia

        #  muestras por segundo
        self.frecuencia_muestreo = frecuencia*3


    def generar(self, tiempo_inicial, tiempo_final):

        import math

        cantidad_muestras = (tiempo_final - tiempo_inicial).seconds/\
        self.frecuencia_muestreo

        muestras = range(int(cantidad_muestras))
        #TODO agregar un ruido blanco a la senal        

        ret = [self.amplitud*math.sin(2*(1/self.frecuencia)*i+self.fase) 
        + 0.25*np.random.normal(size=1) for i in muestras] #cantidad de muestras

        return ret
