total_gastado = int(input("Ingrese el total gastado: "))
def calcular_gasto_promedio(total_gastado, numero_dias):
    gasto_promedio_diario = total_gastado / numero_dias
    return gasto_promedio_diario

def calcular_balance(presupuesto, gasto_promedio):
    return dinero_disponibe