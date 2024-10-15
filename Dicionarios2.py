pessoa = {'Nome': 'Profº. Alberto', 'Idade': 43, 'Cursos': ['Reacy', 'Python']}
print (pessoa)
pessoa['Idade'] = 44
pessoa['Cursos'].append('Angular')
print (pessoa)
print (pessoa.pop('Idade'))
print (pessoa)
pessoa.update({'Idade': 40, 'Sexo': 'M'})
print (pessoa)
del pessoa['Cursos']
print (pessoa)
pessoa.clear()
print (pessoa)
