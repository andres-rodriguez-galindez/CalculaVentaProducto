PrecioVenta = int(input("Ingresa el valor de venta del producto:" ))
CostoProducto = int(input("Ingresa el costo del producto:"))
Porcentaje = ((PrecioVenta-CostoProducto)/PrecioVenta)*1
PorcentajeFormateo = f"{Porcentaje:.4f}".replace('.',',')
print(f"El porcentaje de utilidad del producto es: % {PorcentajeFormateo}")