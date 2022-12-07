"""Presentacion"""
# Edwin Santana 22-0259
# Refinando código
# Dependiendo de los costos se va agregar un 16% de impuestos, y se va imprimir,
# y lo dividimos en 3 funciones.

def open_cost():
    """Abre el archivo y crea una lista"""
    with open("gift_costs.txt","r", encoding="utf-8" ) as costos:
        gift_costs = list(costos)
        gift_costs = [int(c) for c in gift_costs]  # convierte strings a int
        costos.close()  # cerramos el archivo
    return gift_costs


def tax(gift_costs):
    """Calculo agregando los impuestos"""
    total_price = 0
    for cost in gift_costs:
        if cost > 1000:
            total_price += cost * 1.16  # agrega impuestos
        else:
            total_price += cost

    return total_price


def terminal():
    """Ultima funcion, donde imprime el costo"""
    print(tax(open_cost()))
    # imprimir el resultado

if __name__ == '__main__':
    terminal()
