
import pandas as pd
import numpy as np
import sys
import logging

def main():
    try:
        path = sys.argv[1]
    except:
        logging.error("Invalid file path")
    try:
        weight = sys.argv[2]
    except:
        logging.error("Invalid weights")
    try:
        impact = sys.argv[3]
    except:
        logging.error("Impacts not entered")
    try:
        out_name = sys.argv[4] 
    except:
        logging.error("Give a valid output file name")
    
    #file upload
    mydata=pd.read_csv(sys.argv[1]) 
    
    #weight
    # w = int(input('Enter the weights (only positive integers allowed\n'))
    # w = [2,3,1,0.5]
    w = sys.argv[2].split(',')

    #impact
    # i = int(input('Enter the impact as 1 for positive and -1 for negative\n'))
    # i = [-1, -1, 1, 1]
    i = sys.argv[3].split(',')

    #element multipy
    r = []
    for j in range(0, len(w)):
      r.append(float(w[j]) * float(i[j]))

    # r

    d1 = mydata

    first_column = mydata.columns[0]
    # Delete first column
    d = mydata.drop([first_column], axis=1)
    d.to_csv('file.csv', index=False)
    d = pd.DataFrame(d)
    d

    

    def func(df, col):
      df[col] = df[col] / np.sqrt(df[col].sum())

    d=d*d
    # d

    # for i in range(len(d)-1):
    for i in range(d.shape[1]):
      func(d, d.columns[i])

    # d

    d=d*r
    # d

    d.sum(axis=1)

    # for i in range(len(d)):
    #   d["Topsis Score 2"] = d.sum(axis=1)
    # d

    d["Topsis Score"] = d.sum(axis=1)
    # d

    ranks = list(range(len(d)))
    Rank = [x for x in ranks]
    d['Index']=Rank
    # d

    d = d.sort_values(by=['Topsis Score'], ascending=False)
    # d

    ranks = list(range(len(d)))
    Rank = [x+1 for x in ranks]
    d['Rank']=Rank
    # d

    d = d.sort_values(by=['Index'])
    # d

    # d1

    d1['Topsis Score'] = d['Topsis Score']
    d1['Rank'] = d['Rank']
    d1.to_csv(sys.argv[4])


    

    
    
if __name__=='__main__':
    main()