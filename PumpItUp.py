"""
@author: Mike Wilcox

"""
import pandas as pd

#
'''
import os
dir = 'C:\...\PumpItUp' #your working dir
os.chdir(dir)
#'''


# Define train_values_url
train_values_url = "http://s3.amazonaws.com/drivendata/data/7/public/4910797b-ee55-40a7-8668-10efd5c1b960.csv"
# Define train_labels_url
train_labels_url = "http://s3.amazonaws.com/drivendata/data/7/public/0bf8bc6e-30d0-4c50-956a-603fc693d966.csv"
# Define test_values_url
#test_values_url = "http://s3.amazonaws.com/drivendata/data/7/public/702ddfc5-68cd-4d1d-a0de-f5f566f76d91.csv"


# Import train_values
train_values = pd.read_csv(train_values_url)
# Import train_labels
train_labels = pd.read_csv(train_labels_url)
# Import test_values
#test_values = pd.read_csv(test_values_url)

df = train_values.merge(train_labels,how='left', on='id')

    
dfColDescr = df[df.columns].astype('string').describe().transpose()
dfColDescr = df.dtypes.to_frame(name='Dtypes').join(df.describe(include='all', percentiles = [.5]).transpose()).merge(dfColDescr, left_index=True, right_index=True, suffixes=('', '_str'))
dfColDescr.drop(['count_str','unique','top', 'freq'], axis=1, inplace=True)
dfColDescr['missing'] = len(df.index) - dfColDescr['count'].astype('int64')

print dfColDescr
dfColDescr.to_csv('dfColDescr.csv')
#os.startfile('dfColDescr.csv')
