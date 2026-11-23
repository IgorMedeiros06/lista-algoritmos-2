import numpy as np

id = np.arange(10,51,5)
print(id)
id2 = np.arange(10,51,5)**2
print(id2)
idMascara = id2 > 500
print(idMascara)
id500=id2[idMascara]
print(id500)
