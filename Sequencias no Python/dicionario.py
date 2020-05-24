#Dicionario Parte 1
print('Dicionario Parte 1')
dict = {'k1': "cat", 'k2': "dog", 'k3': "mouse", 'k4': "fish"}

print(dict)
print(dict['k1'])
print(dict['k3'])

dict['k5'] = 'parrot'

print(dict)

dict['k2'] = 'squirrel'
print(dict)

#Dicionario Parte 2
print('\r')
print('Dicionario Parte 2')
Team = {}
Team['Point Guard'] = 'Dirk'
Team['Shooting Guard'] = 'Al'
Team['Small Forward'] = 'Sean'
Team['Power Forward'] = 'Alexander'
Team['Center'] = 'Hector'

print(Team['Center'])
print(Team.get('Small Forward'))
print(Team.get('Coach'))