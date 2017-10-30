import sklearn
import pandas as pd
import numpy as np

#my_array = np.array([[1,2,3], [5,6,7]], dtype=np.int64)

#data=pd.DataFrame(my_array,columns=['A','B','C'])


import pandas as pd

data = [{"low": 0, "high": 10, "name": "a"},
        {"low": 10, "high": 20, "name": "b"},
        {"low": 20, "high": 30, "name": "c"},
        {"low": 30, "high": 40, "name": "d"},
        {"low": 40, "high": 50, "name": "e"},]

myDF = pd.DataFrame(data)

#data to be binned
mySeries = pd.Series([5.7, 30.4, 21, 35.1])

#create bins from original data
bins = list(myDF["high"])
bins.insert(0,0)

print pd.cut(mySeries, bins, labels = myDF["name"])

