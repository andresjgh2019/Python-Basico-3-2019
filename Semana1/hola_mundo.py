# Practice 5 - Lists -----------------------------------------

#list of numbers
a=[57,45,7,13]
print(a)




#list of strings
b=['Andres','Pedro','Marta']
print(b)

# how many elements in the list
n=len(a)
print(n)


print('\n'*10)



# Practice 4 - uso de operaciones  ^ , *, /,  o doble slash para division entera

x=4
print(type(x))
print(x*2)
print(x^2)
print(x**2)
print(x/2)

# esto modifica el valor de X! suma 1 y X queda como X+1 es como deci x=x+1
x+=1
print(x)

# Flotantes
y=4.3
print(type(y))

#Boolean

v1=True
v2=False

print(type(v1))
print(v1,v2)
print(v1 and v2)
print(v1 or v2)
print(not v1)
print(3==5)
print(3!=5)
print(3 <5)

print('\n'*10)

#Practice 3 - Use of variables---in Python data type does NOT matter -------------------------------------

x='hola'
print(x)

x=5
print(x)

y=x+2.5
print(y)


print('\n'*10)



# Practice 2 ------------------------------------------------------------------

# print ID prints the location of the variable in memory, print only in the other hand; prints the value stored.
variable2= 10
print('Valor:',variable2)
print('Location in RAM:',id(variable2))


# the variable ID changes when manipulated, in this case the print ID will return a different value than before
variable2= 10+1
print('Valor:',variable2)
print('Location in RAM:',id(variable2))

# variable as text, as usual the ID wil change -when printed will return a different value
variable2= '10'
print('Valor:',variable2)
print('Location in RAM:', id(variable2))



print('\n'*10)

# Practice 1 ------------------------------------------------------------------

variable = "*"

# Solution 1
print('*')
print('\t **')
print('\t \t ***')

# Solution 2
print('*\n', '\t**\n', '\t\t***')

# Solution 3
print(variable)
print('\t',variable,variable)
print('\t \t',variable,variable,variable)

# Solution 4
print(variable,'\n','\t',variable, variable,'\n','\t\t',variable,variable,variable)

# Solution 5 the *2 prints the character two times or in the other case 10X tabs
print('*\n', '\t' +'*'*2 + '\n', '\t'*10 + variable*3)





# OTRAS NOTAS ------------------------------------------------------------------


# defines a variable
texto = 'me llamo andres'

print('Hola Mundo "Mundo!" ')

# inserts a space at the end , by default enter is inserted at the end of every print
print('hola', end=' ')
print('mundo')

# inserts an enter

print('hola', end=' \n')

# inserts the ' and takes it as text not as part of the function with the use of backslash \
print('mundo \' ')

# prints a variable
print(texto)

# inserts an enter in the same instruction
print('hola\nMundo')
