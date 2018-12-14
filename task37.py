import pandas
#df = pandas.read_csv('..../titanic.csv')
df = pandas.read_csv('titanic.csv')
print(df.columns)
print('Всего пассажиров:',len(df['Name']))
print('Мужчин на борту:',len(df[df['Sex'] == 'male']))
print('Процент выживаемости:',(len(df[df['Survived'] == 1])/(len(df['Name']))*100))
if (df[df['Sex'] == 'male'].shape[0]) > (df[df['Sex'] == 'famale'].shape[0]):
    print('Мужчин больше')
else:
    print('Больше женщин')
print('Процент выживших мужчин:',len(df[(df['Sex'] == 'male') & (df['Survived'] == 1)])/len(df[df['Survived'] == 1])*100)
n = len(df[df['Pclass'] == 1])
c = len(df[df['Pclass'] == 2])
v = len(df[df['Pclass'] == 3])
if n > c and n > v:
    print('Выжило больше первого класса')
elif c > n and c > v:
    print('Выжило больше второго класса')
else:
    print('Выжило больше третьего класса')

