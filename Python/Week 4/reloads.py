#reloads an imported module in python
import importlib #whrere the reload func sits
import sample #if we wrote this lone multi times interpeter still print it once here comes the reload func role


importlib.reload(sample)
importlib.reload(sample)

import importlib
import fileChanges
def changs():
    try:
        importlib.reload(fileChanges)
        fileChanges.printChange()
    except:
        pass
for i in range(5):
    changs()
    
    input("hit enter to reload..")