import numpy as np

def LEER_PERSONAS():
    # Definimos el tipo de datos estructurado (dtype) de la variable PERSONAS
    personas_dtype = [('SEXO', str), ('EDAD', int)]

    # Leemos los datos de las 50 personas dentro de la variable PERSONAS
    personas = np.array([], dtype=personas_dtype)
    for i in range(50):
        sexo = input("Introduce el sexo (H/M) de la persona " + str(i+1) + ": ")
        
        # Ponemos un bucle while por si se introduce cualquier otro string que no corresponda
        while(sexo != 'H' and sexo != 'M'): 
            sexo = input("Introduce el sexo (H/M) de la persona " + str(i+1) + ": ")
            
        edad = int(input("Introduce la edad de la persona " + str(i+1) + ": "))
        personas = np.append(personas, np.array((sexo, edad), dtype=personas_dtype))

    # Ordenamos los datos por edad y sexo
    personas = np.sort(personas, order=['EDAD', 'SEXO'])
    
    return personas


# Inicializamos las variables
num_mayor_edad = 0
num_menor_edad = 0
num_hombre_mayor_edad = 0
num_mujer_menor_edad = 0
porcentaje_mayor_edad = 0
porcentaje_mujer = 0

PERSONAS = LEER_PERSONAS()

# Sacamos el ranking
print("Ranking de las 50 personas según edad y sexo:")
for i in range(50):
    print(str(i+1) + ". " + PERSONAS[i]['SEXO'] + " " + str(PERSONAS[i]['EDAD']))

# Calculamos
for i in range(50):
    if PERSONAS[i]['EDAD'] >= 18:
        num_mayor_edad += 1
        if PERSONAS[i]['SEXO'] == 'H':
            num_hombre_mayor_edad += 1
    else:
        num_menor_edad += 1
        if PERSONAS[i]['SEXO'] == 'M':
            num_mujer_menor_edad += 1

porcentaje_mayor_edad = num_mayor_edad / 50 * 100
porcentaje_mujer = (50 - num_hombre_mayor_edad) / 50 * 100

# Sacamos
print("Número de personas mayores de edad: " + str(num_mayor_edad))
print("Número de menores de edad: " + str(num_menor_edad))
print("Número de hombres mayores de edad: " + str(num_hombre_mayor_edad))
print("Número de mujeres menores de edad: " + str(num_mujer_menor_edad))
print("Porcentaje representado por personas mayores de edad: " + str(porcentaje_mayor_edad) + "%")
print("Porcentaje representado por mujeres: " + str(porcentaje_mujer) + "%")
