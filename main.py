######
# Edwin Santana 22-0259
# Refinando código
# Dependiendo de los costos se va agregar un 16%, y lo va imprimir al final.
######
def open_cost():
    archivo = open("gift_costs.txt", "r")
    gift_costs = list(archivo)
    gift_costs = [int(c) for c in gift_costs]  # convierte strings a int
    archivo.close()  # cerramos el archivo
    return gift_costs


def tax(gift_costs):
    total_price = 0
    for cost in gift_costs:
        if cost > 1000:
            total_price += cost * 1.16  # agrega impuestos
        else:
            total_price += cost  

    return total_price


def terminal():
    print(tax(open_cost()))
    # imprimir el resultado

if __name__ == '__main__':
    terminal()