import torch
import numpy as np

tensorset = np.array([[1,4,2,6],[4,2,1,6]]) 

tensor = torch.from_numpy(tensorset) # creating a tensor

tpose = torch.t(tensor) #transpose


print(tpose)

array = [1,3,5,7,3]
for i in array:
    print(i)