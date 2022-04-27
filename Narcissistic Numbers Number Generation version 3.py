import math
import numpy as np
import datetime as dt
import time
from batchup import data_source

start_time = time.time()
My_list = np.arange(1,100000001, 1)
g = 0
a = 0
d = 0
k = 0
z = 0
b = My_list[a]
cupok = []
all_the_marbles = []
ds = data_source.ArrayDataSource([My_list]) 

for (batch_My_list) in ds.batch_iterator(batch_size=100):
    L = 100
    while a < L:
        b = batch_My_list[0][a]
        #print(str(b) + "b")
        f = int(math.log10(b)+1)
        while d < f:
            c = (int(str(b)[d]))
            g += c**f
            d += 1
        if g == b:
            cupok.append(b)
            d = 0
            g = 0
            print("kilo")
        else:
            d = 0
            g = 0
        a += 1
    L = 0    
    a = 0
    z +=1
    #print(k)
    #print(cupok)
    print(z)
    #all_the_marbles.append(cupok)

date = dt.datetime.now()
format_date = f"{date:%a, %b %d %Y}"
time_string = time.strftime('%H_%M_%S')
np.savetxt("C:/Users/Admin/Downloads/Narcissistic Numbers research/narcicistic numbers outputs/test"+format_date+time_string+".txt", cupok)

print("--- %s seconds ---" % (time.time() - start_time))
print(np.shape(batch_My_list))
print(cupok)
