a = '123'
b = ' de Oliveira 4'

print (a + b)
print (a.__add__(b))
print (str.__add__(a,b))

print (dir(str))

print (len(a))
print (a.__len__())

print ('1' in a)
print (a.__contains__('1'))
