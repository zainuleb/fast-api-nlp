import pandas as pd
from nltk.tokenize import word_tokenize
import numpy as np
import time

a=time.perf_counter()
df=pd.read_csv("locations.csv",names=["Location"])
locs=df.Location.to_list()

df=pd.read_csv("days.csv",names=["Days"])
days=df.Days.to_list()

df=pd.read_csv("professions.csv",names=["Professions"])
prof=df.Professions.to_list()

df=pd.read_csv("expressions.csv",names=["Expressions"])
exps=df.Expressions.to_list()

def lstToStr(s): 
    str1 = " "
    return (str1.join(s))


f = open("dataset.txt","a")

for i in range(100000):

    exp = exps[np.random.randint(0,len(exps))]
    exp = word_tokenize(exp)

    for j in range(len(exp)):
        if exp[j] == 'PP':
            exp[j] = prof[np.random.randint(0,len(prof))]
        elif exp[j] == 'DD':
            exp[j] = days[np.random.randint(0,len(days))]
        elif exp[j] == 'PH':
            exp[j] = locs[np.random.randint(0,len(locs))]
    
    exp_str = lstToStr(exp)

    f.write(exp_str+'\n')

    print(exp_str)

f.close()
b=time.perf_counter()
print(b-a)