import getCount
import time
import dataBase
uwu = True
while uwu:
    
    getCount.getUserCount()
    dataBase.addrow(getCount.getUserCount())
    time.sleep(600)