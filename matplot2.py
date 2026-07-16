import taxi_raw as tr 
import numpy as np
import matplotlib.pyplot as plt


taxi:ndarray= np.sum(tr.Taxi , axis=2)
print(taxi)

days=('shanbe','yekshanbe','doshanbe','seshanbe','chaharshanbe','panjshanbe','jom e')

plt.figure(figsize=(30,6)) 

plt.plot(days, taxi[0], label='Driver 1', marker='o')
																		
plt.plot(days, taxi[1], label='Driver 2', marker='o')

plt.plot(days, taxi[2], label='Driver 3', marker='o')

plt.plot(days, taxi[3], label='Driver 4', marker='o')

plt.plot(days, taxi[4], label='Driver 5', marker='o')

plt.legend()
plt.show()
