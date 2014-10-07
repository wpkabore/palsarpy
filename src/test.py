
from src.io import PalsarFile
from src.leader import  DataSetSummary, FileDescriptor 
from src.leader import DataQualitySummary, MapProjectionData

volume = PalsarFile("Volume Directory", 0)
leaderFD = FileDescriptor()
leaderDss = DataSetSummary()
leaderDqs = DataQualitySummary()
#leaderMap = MapProjectionData()

#try
#volume.open("/media/kpat/Projet_PALSAR/Donnees_source/mode_PLR/niveau_1.1/PSR_MMC_TP__0003674001_Orpaillage/VOL-ALPSRP059810080-P1.1__A");
volume.open("/media/kpat/Projet_PALSAR/Donnees_source/mode_PLR/niveau_1.1/PSR_MMC_TP__0003674001_Orpaillage/LED-ALPSRP059810080-P1.1__A")
volume.chargerRecord(leaderFD)
volume.chargerRecord(leaderDss)
#volume.chargerRecord(leaderMap)
volume.chargerRecord(leaderDqs)
volume.close()

print(leaderFD)
print("******************************************")
print("******************************************")
print(leaderDss)
print("******************************************")
print("******************************************")
print(leaderDqs)
print("******************************************")
print("******************************************")
#print(leaderMap)