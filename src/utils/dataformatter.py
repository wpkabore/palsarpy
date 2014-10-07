# -* coding: UTF8 *-
'''
Created on 16 mars 2013

@author: kpat
'''

class DataFormatter(object):
    BYTE = 0
    CHAR = 1
    INT4 = 2
    INT6 = 3
    INT8 = 4
    FLOAT8_3 = 5
    FLOAT16_7 = 6
    # serie de 10 entiers codés sur 6 octets
    _10INT6 = 7
    # nombre exponentiel
    E16_7 = 8
    # serie de 2 décimaux
    _2FLOAT16_7 = 9
    INT16 = 10
    E20_13 = 11

