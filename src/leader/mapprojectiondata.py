'''
Created on 13 avr. 2013

@author: kpat

Ce fichier n'existe pas dans les produits de niveau 1.1
'''
from src.io import PalsarRecord, PalsarField
from src.utils import DataFormatter

class MapProjectionData(PalsarRecord):
    
    def __init__(self):
        PalsarRecord.__init__(self, 'Map Projection Data', 4816, 1620)
        self.set()
        
    def set(self):
        #on ajoute seulement les champs qui nous intéressent
        self._structure.append(PalsarField(29, 32, 
                                           'Map projection descriptor', 
                                           DataFormatter.CHAR))