def LEER_NUMERO():
    num = int(input("Introduce un número: "))
    return num

NUMERO = LEER_NUMERO()

if NUMERO % 2 == 0:
  for i in range(NUMERO, (0)-1, -2):
    print(i)

else:
  for i in range(NUMERO, (1)-1, -2):
    print(i)