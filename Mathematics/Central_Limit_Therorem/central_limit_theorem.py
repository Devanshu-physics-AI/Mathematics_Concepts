import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import random

# function for means
def mean(population,size):
    mean=np.empty(size)
    for i in range(size):
        a=population.sample(size).mean()
        mean[i]=a
    return mean


#import data
data=pd.read_csv("/users/devanshusharma/desktop/train.csv")
print(data.sample(5))
population=data["orders"]
print(population.sample(5))

#population size
pop_size=population.size     #7340


#creating the subplots
a,axis=plt.subplots(2,2,figsize=(8,8))

sns.kdeplot(population,fill=False,ax=axis[0,0],color="red")
plt.xlabel("No. of orders")
plt.title("population")

means1=mean(population,100)
sns.kdeplot(means1,fill=False,ax=axis[0,1],color="blue")
plt.xlabel("No. of orders")
plt.title("sample with size= 100")

means2=mean(population,250)
sns.kdeplot(means2,fill=False,ax=axis[1,0],color="orange")
plt.xlabel("No. of orders")
plt.title("sample with size= 250")

means3=mean(population,1000)
sns.histplot(means3,fill=False, kde=True,ax=axis[1,1],color="black")
plt.xlabel("No. of orders")
plt.title("sample with size= 1000")

plt.show()

'''CONVLUSION- As the size of the sample increses the graph reach more towards the normal distribution.
This data is random and we have create the random sample to the data'''


#saving the graph
#saving in the png because same quality is taking lesser space
a.savefig("/users/devanshusharma/downloads/Central_Limit_Therorem_check.jpg",dpi=500)


