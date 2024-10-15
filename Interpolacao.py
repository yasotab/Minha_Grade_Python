from string import Template

Nome, Idade = 'Ana', 30

print ('Nome: %s Idade: %d' % (Nome, Idade,)) # Mais Antiga
print ('Nome: {0} Idade: {1}'.format(Nome, Idade)) # python < 3.6
print (f'Nome: {Nome} Idade: {Idade}') # python >= 3.6

s = Template('Nome: $Nome Idade: $Idade')
print (s.substitute(Nome=Nome, Idade=Idade))
