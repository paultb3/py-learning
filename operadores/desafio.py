#Sistema de descuentos de un restaurante

monto_consumido = float(input("Ingrese el consumo: "))
descuento = 0

def descontar_porcentaje(monto, porcentaje):
    return monto*(porcentaje/100)

def calcular_descuento(monto):
    if(monto<=50):
        return 0
    if(monto>50 or monto<=100):
        return descontar_porcentaje(monto,10)
    if(monto>100 or monto<=200):
        return descontar_porcentaje(monto, 20)
    if(monto>200):
        return descontar_porcentaje(monto, 30)
    
def calcular_monto_final(monto):
    return monto - calcular_descuento(monto)

def mostrar_resultados(monto):
    return  f"""
            Monto: {monto}
            Descuento: {calcular_descuento(monto)}
            Monto Final: {calcular_monto_final(monto)}
            """
print(mostrar_resultados(monto_consumido))

