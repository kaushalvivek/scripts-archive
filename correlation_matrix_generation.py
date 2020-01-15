import pandas as pd
import codecs

with codecs.open('book1.csv', 'r', encoding='utf-8',
                 errors='ignore') as fdata:
  data = pd.read_csv(fdata)
  corr_mat = data.corr()
  corr_mat.to_csv('corr_matrix.csv')
