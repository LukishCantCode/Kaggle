import time
start_time = time.time()
x=0
for i in range(0,10000000):
 i=x
print("--- %s seconds ---" % (time.time() - start_time))
