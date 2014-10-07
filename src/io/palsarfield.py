# -* coding: UTF-8 *-
'''
Created on 16 mars 2013

@author: kpat
'''
class PalsarField(object):
    ''' 
    cette classe représente les champs d'un enregistrement ou record
    '''
    
    def __init__(self, offset_debut, offset_fin, description, formatData) :
        self.__offsetDebut = offset_debut
        self.__offsetFin = offset_fin
        # exemple les 4 premiers octets du Volume Descriptor Record est
        # Record sequence number = 1' 
        self.__description = description
        # format des octets lus: B = octets, I8 = entier de 8 octets,
        # F16.7 = réel de 
        self.__dataType = formatData
        self.__valeur = 0
        
    
    def __str__(self):
        return self.__description + " **** " + self.__valeur
    
    
    def getLength(self):
        return (self.__offsetFin - self.__offsetDebut) + 1
    
    @property
    def dataType(self):
        return self.__dataType
    
    @property
    def debutOffset(self):
        return self.__offsetDebut
   
    @property
    def description(self):
        return self.__description
    
    @property
    def valeur(self):
        return self.__valeur
    
    @description.setter
    def description(self, valeur):
        self.__description = valeur
        
    @valeur.setter
    def valeur(self, val):
        self.__valeur = val