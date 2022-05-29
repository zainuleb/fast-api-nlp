# import nlp_text
import pandas as pd
import numpy as np
from nltk.corpus import wordnet

print('')
print('')
# print("Enter NL query : " , end =" ")

# tokens = nlp_text.preproc()
# print(tokens)

def exp_attr(x):
    lst , rlst =[] , []

    df=pd.read_csv("D:/volunteer-app-next/fastapi/nlp_model/attributes.csv")
    lst = df.values

    for i in lst:
        if i[0] in x:
            rlst.append(i[0])
        else:
            try:
                syns = wordnet.synset(i[0]+".n.01")
                for j in syns.lemma_names():
                    if j in x:
                        rlst.append(i[0])
                        break
            except Exception:
                pass

    # if len(rlst) == 0:
    #     rlst.append('*')

    # print(rlst)
    return rlst


def imp_attr(x):
    lst , rlst = [] , []

    df=pd.read_csv("D:/volunteer-app-next/fastapi/nlp_model/domain_dictionary.csv")
    lst = df.values

    for i in lst:
        if i[0] in x:
            
            rlst.append(i[0])
        else:
            try:
                syns = wordnet.synset(i[0]+".n.01")
                for j in syns.lemma_names():
                    if j in x:
                        
                        rlst.append(i[0])
                        break
            except Exception:
                pass

    # print(rlst)
    return rlst

def gen_query(x):
    lst , slct , frm , wher = [] , [] , [] , []
    que = ""

    slct = exp_attr(x)
    wher = imp_attr(x)
    for i in wher:
        lst.append(i)

    for j in slct:
        lst.append(j)




    return lst

    # df=pd.read_csv("D:/volunteer-app-next/fastapi/nlp_model/relations.csv")
    # lst = df.values

    # for i in lst:
    #     if (i[0] in slct and i[1] not in frm):
    #         frm.append(i[1])
        
    #     if (i[0] in wher and i[1] not in frm):
    #         frm.append(i[1])

    # que += ("SELECT " + (','.join(slct)) + " FROM " + (','.join(frm)) + " WHERE ")
    
    # j = 0
    # while j < len(wher):
    #     que += wher[j] + '=' + "'" + wher[j+1] + "'" + ' AND '
    #     j += 2
    
    # que = que.rstrip(' AND ')
    
    # que += ';'

    # return que


print('')
# print(gen_query(tokens))
print('')
print('')