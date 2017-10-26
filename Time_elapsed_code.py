#V1
import timeit
start_time = timeit.default_timer()
# code you want to evaluate
elapsed = timeit.default_timer() - start_time




import time
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))



import time

start_time = time.clock()
main()
print time.clock() - start_time, "seconds"
