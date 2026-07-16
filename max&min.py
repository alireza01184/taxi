import taxi_raw as tr
import numpy as np

taxi_all = np.sum(tr.Taxi,axis=(0,2))


print(taxi_all)

taxi_max = np.max(taxi_all)
taxi_min = np.min(taxi_all)

print(taxi_max,taxi_min)

x=0
y=0

x1= []
y1=[]

for i in taxi_all:
	if i == taxi_max:
		x1.append(x)
	x+=1
	
	if i == taxi_min :
		y1.append(y)
	y+=1
	
print (x1,y1)

for j in (x1) :
	if j == 0 :
		print(f"day/s max is/are : shanbe with {taxi_max}")
	if j == 1 :
		print(f"day/s max is/are : yekshanbe with {taxi_max}")
	if j == 2 :
		print(f"day/s max is/are : doshanbe with {taxi_max}")
	if j == 3 :
		print(f"day/s max is/are : seshanbe with {taxi_max}")
	if j == 4 :
		print(f"day/s max is/are : chaharshanbe with {taxi_max}")
	if j == 5 :
		print(f"day/s max is/are : panjshabne with {taxi_max}")
	if j == 6 :
		print(f"day/s max is/are : jomE with {taxi_max}")
		
print("\n---------------------------")

for k in (y1) :
	if k == 0 :
		print(f"day/s min is/are : shanbe with {taxi_min}")
	if k == 1 :
		print(f"day/s min is/are : yekshanbe with {taxi_min}")
	if k == 2 :
		print(f"day/s min is/are : doshanbe with {taxi_min}")
	if k == 3 :
		print(f"day/s min is/are : seshanbe with {taxi_min}")
	if k == 4 :
		print(f"day/s min is/are: chaharshanbe with {taxi_min}")
	if k == 5 :
		print(f"day/s min is/are : panjshabne with {taxi_min}")
	if k == 6 :
		print(f"day/s min is/are : jomE with {taxi_min}")

	
	
