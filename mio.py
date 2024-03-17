def calcular_descuento (monto_total, porcentaje_descuento = 10):
    descuento=  monto_total * (porcentaje_descuento/100)
    return descuento

descuento=calcular_descuento(200,10)
print( descuento)
descuento = calcular_descuento

# ingreso del total de la compra
total_compra = float(input('ingrese el total a pagar'))
porcentaje_descuento = float(input('ingrese el porcentaje de descuento'))

# llamada a funcion para el descuento
descuento = calcular_descuento('monto_total', 'porcecentaje_descuento')

# llamada a funcion para el calculo dela compra menos el descuento
# formula para calcular el total del descuento
compra_menos_descuento = total_compra -descuento

print('valor de la compra sin descuento: 200', total_compra)
print('valor de la compra con descuento: 20', descuento)
print('monto  total : 160', compra_menos_descuento)
