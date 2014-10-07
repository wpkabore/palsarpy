'''
Created on 17 mars 2013

@author: kpat
'''

from src.io import PalsarField, PalsarRecord
from src.utils import DataFormatter

class DataSetSummary(PalsarRecord):
    
    def __init__(self):
        PalsarRecord.__init__(self, 'Data set Summary Record', 720, 4096)
        self.set()
        
    def set(self):
        #champs retenus
        self._structure.append(PalsarField(20,51,"id-image / Scene identifier", DataFormatter.CHAR))
        self._structure.append(PalsarField(484,491,"Angle d'incidence / Incidence angle at scene center", DataFormatter.FLOAT8_3))
        self._structure.append(PalsarField(1094,1109,"Niveau de produit / Product level code", DataFormatter.CHAR))
        self._structure.append(PalsarField(1110,1141,"Niveau de produit / Product type specifier", DataFormatter.CHAR))
        self._structure.append(PalsarField(1206,1221,"Bandwith per look in Azimuth (Hz)", DataFormatter.FLOAT16_7))
        self._structure.append(PalsarField(1122,1237,"Bandwith per look in Range", DataFormatter.FLOAT16_7))
        self._structure.append(PalsarField(1534,1541,"Orbitre / Time direction indicator along line direction", DataFormatter.CHAR))
        self._structure.append(PalsarField(1702,1717,"Taille du pixel / Pixel spacing (meter)", DataFormatter.FLOAT16_7))
        