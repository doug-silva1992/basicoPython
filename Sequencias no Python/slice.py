#Slice parte 1
Participants = ['John', 'Leila', 'Gregory', 'Cate', "Dwayne",'George', 'Catherine']

print(Participants)
print(Participants[1:3])
print(Participants[:2])
print(Participants[4:])
print(Participants[-2:])

#Slice parte 2
Participants = ['John', 'Peter', 'Maria', 'Leila', 'Dwayne', 'Catherine']

print(Participants.index("Maria"))

Newcomers = ['Joshua', 'Brittany']
print(Newcomers)

Bigger_List = [Participants, Newcomers]
print(Bigger_List)

Participants.sort()
print(Participants)

Number = [1, 2, 3, 4, 5]
Number.sort()
print(Number)

Number.sort(reverse=True)
print(Number)
