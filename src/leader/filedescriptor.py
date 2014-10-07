'''
Created on 17 mars 2013

@author: kpat
'''
from src.io import PalsarRecord, PalsarField
from src.utils import DataFormatter
class FileDescriptor(PalsarRecord):
    
    def __init__(self):
        PalsarRecord.__init__(self, 'File Descriptor Record', 0, 720)
        self.set()
    
    def __str__(self):
        return PalsarRecord.__str__(self)
        
    def set(self):
        #champs retenus
        self._structure.append(PalsarField(16,27,"Format / Format Control document ID", DataFormatter.CHAR))
        