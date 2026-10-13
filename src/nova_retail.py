"""Módulo para procesar ventas de productos."""


def hay_stock_suficiente(cantidad, stock_actual):
    """Comprueba si hay unidades suficientes para la venta."""
    return stock_actual >= cantidad


def calcular_total(cantidad, precio_unitario, igv_porcentaje):
    """Calcula el subtotal, el IGV y el total."""
    subtotal = precio_unitario * cantidad
    igv = subtotal * igv_porcentaje
    return subtotal + igv


def procesar_venta(
    codigo_producto,
    cantidad,
    stock_actual,
    precio_unitario,
    igv_porcentaje,
):
    """Registra la venta y devuelve (total, nuevo_stock), o None si falta stock."""
    if not hay_stock_suficiente(cantidad, stock_actual):
        print("Sin stock suficiente")
        return None

    total = calcular_total(cantidad, precio_unitario, igv_porcentaje)
    nuevo_stock = stock_actual - cantidad

    print(f"Venta registrada: {codigo_producto} - Total: {total:.2f}")
    return total, nuevo_stock
