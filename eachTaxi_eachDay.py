import taxi_raw as tr
import numpy as np

tArry :np.ndarray= tr.Taxi

tArry_axis_1th = np.sum(tArry,axis=0)

#print (tArry_axis_1th)

tArry_axis_2nd = np.sum(tArry_axis_1th,axis=0)

print (tArry_axis_2nd)