# -* coding: UTF-8 *-
'''
Created on 17 mars 2013

@author: kpat
'''
from abc import ABCMeta, abstractmethod
from src.utils.dataformatter import DataFormatter
class PalsarRecord(object):
    __metaclass__ = ABCMeta

    
    def __init__(self, libelle, offset_debut, taille):
        self._libelle = libelle
        self._offsetDebut = offset_debut
        self._nbreOctets = taille
        self._structure = []
        self._donnees = []
    
    def __str__(self):
        sb = ''
        for pf in self._structure:
            #print(pf)
            sb += str(pf) + "\n"
        
        #print(sb)
        return sb
        
    @abstractmethod
    def set(self):
        '''
        créé la liste des champs spécifiques au FileDescriptor du
        Leader File
        '''
        pass
    
    def addField(self, palsarField):
        self._structure.append(palsarField)
        
    def readField(self, palsarField):
        #dataTmp = self._donnees[palsarField.debutOffset:palsarField.getLength()]
        dataType = palsarField.dataType
        
        sb = ''
        
        if dataType == DataFormatter.CHAR:
            debut = palsarField.debutOffset
            for i in range(palsarField.getLength()):
                sb += chr((self._donnees[debut]) & 0xff)
                debut+=1
                
        elif dataType == DataFormatter.BYTE :
            #conversion en entier non signé et transformation en string
            if palsarField.getLength() == 1 :
                sb = str(self._donnees[palsarField.debutOffset] & 0xff)
            else:
                nbre = 0
                debut = palsarField.debutOffset
                #conversion en entier non signé par décalage de bit
                for i in range(palsarField.getLength()):
                    nbre <<= 8
                    nbre |= self._donnees[debut] & 0xff
                    debut+=1
                sb = str(nbre)
                
        # tous les entiers sont traités pareil
        elif dataType in [DataFormatter.INT4, DataFormatter.INT6,
                       DataFormatter.INT8, DataFormatter._10INT6,
                       #tous les décimaux sont traités pareil
                       DataFormatter.FLOAT16_7, DataFormatter.FLOAT8_3,
                       DataFormatter._2FLOAT16_7, DataFormatter.E16_7,
                       DataFormatter.E20_13] :
            debut = palsarField.debutOffset
            for i in range(palsarField.getLength()):
                sb += chr((self._donnees[debut]) & 0xff)
                debut+=1
        
        palsarField.valeur = sb

    
    def open(self, dataTemp):
        '''
        initialise l'enregistrement à partir d'un tableau d'octets
        provenant d'un fichier PALSAR
        '''
        self._donnees = dataTemp
        for pf in self._structure:
            self.readField(pf)
            
    @property
    def offsetDebut(self):
        return self._offsetDebut
    
    @property
    def nbreOctets(self):
        return self._nbreOctets
