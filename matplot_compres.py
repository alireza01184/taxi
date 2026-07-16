import taxi_raw as tr 
import numpy as np 
import matplotlib.pyplot as plt

taxi_all = np.sum(tr.Taxi,axis=(1,2))

X =['driver 1','driver 2','driver 3','driver 4','driver 5']

X_axis = np.arange(len(X))
 
plt.bar(X_axis,taxi_all, 0.7 , label='taxi drivers')

plt.xticks(X_axis,X)
plt.xlabel('DRIVERS')
plt.ylabel('majmo e safar ha')
plt.title("nemudar safar haie pazirofte shode")

plt.legend()
plt.show()

