CostoProducto = int(input("Ingresa el costo del producto: "))
MargenDeUtilidad = int(input("Cual es el margen que deseas ganar: "))
Porcentaje = MargenDeUtilidad / 100
Resultado = CostoProducto / (1-Porcentaje)
ResultadoFormateado = "{:,.0f}".format(Resultado)
print(f"Debes vendes el producto en: $  {ResultadoFormateado}")

