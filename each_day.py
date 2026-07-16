import taxi_raw as tr
import numpy as np

#print(tr.Taxi)

per_day = np.sum(tr.Taxi,axis=(0,2))

print(per_day)