'''
Created on 13 avr. 2013

@author: kpat
'''
from src.io import PalsarField, PalsarRecord
from src.utils import DataFormatter

class DataQualitySummary(PalsarRecord):
    
    def __init__(self):
        PalsarRecord.__init__(self, 'Data Quality Summary Record', 27548, 1620)
        self.set()
        
    def set(self):
        # champs retenus
        self._structure.append(PalsarField(7, 2,
                                           "Résolution spatiale / Nominal slant range resolution",
                                           DataFormatter.BYTE))
        self._structure.append(PalsarField(143, 19,
                                           "Résolution spatiale / Nominal azimut resolution",
                                           DataFormatter.FLOAT16_7))