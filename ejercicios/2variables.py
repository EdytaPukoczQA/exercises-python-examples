#Cadena: lo que está entre comillas
gv_name = "Edyta"
#Números sin decimales (se conocen como int en programación)
gv_age = 35
#Números con decimales (se conocen como float en programación)
gv_pi = 3.14
#Booleanos (True or False) importante escribirlo con la mayúscula inicial y sin comillas
gv_likes_python = True

#Imprimir las variables = mostrar por consola
print("name", gv_name)
print("age", gv_age)
print("pi", gv_pi)
print ("Do you like Python?", gv_likes_python)

#Obtener valores introducidos por el usuario
gv_pet_name = input("What is your pet name? ")
gv_pet_age = input("How old is your pet? ")

print("Your pet name is", gv_pet_name)
print("Your pet age is", gv_pet_age)
gv_pet_age = gv_pet_age + "."
print("Your pet name is", gv_pet_name, "and his/her age is", gv_pet_age)