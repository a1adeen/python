import pandas as pd
import numpy as np

dict_1 = {
    "name" : ['harry' , 'rohan' , 'subh'],
    'marks': [100 , 78 , 11],
    'city' : [ 'rampur' , 'delhi' , 'kanpur']
}

# to make an excel sheet
frame = pd.DataFrame(dict_1)
print(frame)
# to remove the index
frame.to_csv('data_index.csv' , index = False)


# print(frame.head(1))


# to get the detailed analysis
print(frame.describe())


# to check the particular column
data = pd.read_csv('data_index.csv')
print(data['marks'])


# to change the value in excel
#
# changes = data['marks'][0] = 90
# print(changes)



# to change the indexs

data.index = ['phla' , 'dusra' , 'teesra']
print(data)