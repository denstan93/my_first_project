import pandas
info = pandas.read_csv('info.csv')
marks = pandas.read_csv('marks.csv')

x1 = info.merge(marks, left_on='id', right_on='id2')
print((info.shape[0])-(x1.shape[0]))

x2 = marks.merge(info, left_on='id2', right_on='id')
print((marks.shape[0])-(x2.shape[0]))

x3 = x1[x1['race'] == 'group A']
print((x3['math'].sum())/x3.shape[0])

x4 = marks.merge(info, left_on='id2', right_on='id', how='outer')
print(x4.shape)

x5 = marks.merge(info, left_on='id2', right_on='id', how='right')
print(x5.shape)

x6 = info.merge(marks, left_on='id', right_on='id2', how='right')
print(x6.shape)