#en python las variables pueden cambiar de tipo
#como en la mayoría de los lenguajes dínamicos

var_one = 42
var_one = "Ezequiel"
print(var_one)

#cambiar tipos de variables
var_two = 50
var_two_str = str(var_two)
var_two_float = float(var_two)
print(var_two_str)
print(var_two_float)

#obteniendo el tipo de la variable
print(type(var_two))
print(type(var_two_str))
print(type(var_two_float))
