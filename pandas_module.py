import pandas as pd
import numpy as np

dict_1 = {
    "name" : ['harry' , 'rohan' , 'subh'],
    'marks': [100 , 78 , 11],
    'city' : [ 'rampur' , 'delhi' , 'kanpur']
}


frame = pd.DataFrame(dict_1)
print(frame)
frame.to_csv('data.csv')