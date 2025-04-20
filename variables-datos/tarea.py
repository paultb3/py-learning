"""
Enunciado: Dado el valor de venta de un producto, se debe
calcular el Impuesto General a las Ventas (IGV) que es del 18%, y
a partir de eso, determinar el precio de venta final.

Mejora: En esta práctica, vamos a crear un programa en Python
que permita al usuario ingresar el valor de venta del producto.
Luego, el sistema realizará los cálculos necesarios para hallar el
IGV y el precio de venta final. Esta mejora incluirá un código
Python que automatiza todo el proceso."""

#solucion
precio_producto = float(input('Ingrese el precio del producto:'))
IGV = 0.18

descuento = precio_producto - precio_producto*IGV

precio_final = round(descuento*IGV,3);

print(f'precio: {precio_producto} \nIGV: {IGV} \nPrecio Final: {descuento}')

