def LEER_HORASTRABAJADAS():
  horas = int(input("Introduce el número de horas trabajadas: "))
  return horas

def LEER_TARIFA():
  tarifa= float(input("Introduce la tarifa horaria: "))
  return tarifa

# Leemos los inputs del programa
HORASTRABAJADAS = LEER_HORASTRABAJADAS()
TARIFA = LEER_TARIFA()

# Calculamos la paga, tanto de horas normales como horas extra
if HORASTRABAJADAS > 40:
    PAGA_NORMAL = 40 * TARIFA
    PAGA_HORAS_EXTRA = (HORASTRABAJADAS - 40) * (TARIFA * 1.5)
else:
    PAGA_NORMAL = HORASTRABAJADAS * TARIFA
    PAGA_HORAS_EXTRA = 0

# Calculamos la paga total
PAGA_TOTAL = PAGA_NORMAL + PAGA_HORAS_EXTRA

# Sacamos la paga total por pantalla
print("Paga total: ", PAGA_TOTAL, " euros.")