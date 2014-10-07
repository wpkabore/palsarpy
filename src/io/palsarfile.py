# -* coding: UTF-8 *-
'''
Created on 17 mars 2013

@author: kpat
modélise un fichier au format PALSAR par exemple
le Volume Directory File
'''
class PalsarFile:
    def __init__(self, libelle, nbre_record):
        self.__libelle = libelle
        self.__nbreRecord = nbre_record
        self.__cheminFichierSource = ''
        self.__fichierSource = ''
        self.listeRecords = []
        
    def open(self, nom_fichier):
        self.__cheminFichierSource = nom_fichier
        self.__fichierSource = open(self.__cheminFichierSource, 'rb')
    
    def close(self):
        self.__fichierSource.close()
        
    def chargerRecord(self, palsarRecord):
        """ 
        lit le nombre d'octets d'un enregistrement et
        initialise ce dernier
        """
        self.__fichierSource.seek(palsarRecord.offsetDebut)
        dataTemp = self.__fichierSource.read(palsarRecord.nbreOctets)
        if(len(dataTemp)<1):
            return 0
        palsarRecord.open(dataTemp)
        return 1