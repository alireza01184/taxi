import taxi_raw as tr
import numpy as np

x= np.sum(tr.Taxi, axis=(1))

for i in x:
	#print(i)
	print(i[0])
