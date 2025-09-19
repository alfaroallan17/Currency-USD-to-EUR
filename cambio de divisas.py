def obtener_total():
    while True:
        try:
            total = float(input("Ingrese el monto total: "))
            if total <= 0:
                raise ValueError()
            return total
        except ValueError: 
            print ('Introduzca un numero positivo')

def obtener_moneda(etiqueta):
    monedas = ("USD", "EUR")
    while True:
        moneda = input (f"moneda de {etiqueta} (USD/EUR): ").upper()
        if moneda not in monedas: 
            print ("moneda no valida")    
        else:
            return moneda
        

def convertir(total, moneda_origen, moneda_destino):
    tasas_cambio = {
        "USD": {"EUR": 0.85},  
        "EUR": {"USD": 1.18},
    }
    return total * tasas_cambio[moneda_origen][moneda_destino]

def main():
    total = obtener_total()
    moneda_origen = obtener_moneda("origen")
    moneda_destino = obtener_moneda("destino")

    if moneda_origen == moneda_destino:
        print('la moneda de origen y destino no pueden ser iguales')
        return
    
    
    total_convertido = convertir (total, moneda_origen, moneda_destino)
    print (f'{total} {moneda_origen} = {total_convertido:.2f} {moneda_destino}')

if __name__ == "__main__":
    main()