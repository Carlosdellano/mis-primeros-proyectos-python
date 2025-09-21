while True:
    print ('1. Sumar')
    print ('2. Restar')
    print ('3. Multiplicar')
    print ('4. Dividir')
    print ('5. Potencia')
    print ('6. Raíz cuadrada')
    print ('7. Porcentaje')
    print ('8. Salir')

    elección = int (input('Elige una opción: '))
    if elección == 1 :
        suma1 = float(input('Dime el primer número:'))
        suma2 = float(input('Dime el segundo número:'))
        resultado_suma = suma1 + suma2
        print ('El resultado es:', resultado_suma)
    elif elección == 2:
        resta1 = float (input('Dime el primer número:'))
        resta2 = float(input('Dime el segundo número:'))
        resultado_resta = resta1 - resta2
        print ('El resultado es:', resultado_resta)
    elif elección == 3:
        multiplicación1 = float(input('Escribe el primer número:'))
        multiplicación2 = float(input('Escribe el segundo número:'))
        resultado_multiplicación = multiplicación1 * multiplicación2
        print ('El resultado es:', resultado_multiplicación)
    elif elección == 4:
        división1 = float(input('Escribe el primer número:'))
        división2 = float(input('Escribe el segundo número:'))
        if división2 == 0:
            print ('Error de cálculo (No se pueden dividir números entre 0)')
        else :
            resultado_división = división1 / división2
            print ('El resultado es:', resultado_división)
    elif elección == 5:
        base1 = float(input('Escribe la base:'))
        exponente2 = float(input('Escribe el exponente:'))
        resultado_potencia = base1 ** exponente2
        print ('El resultado es:', resultado_potencia)
    elif elección == 6:
        raízcuadrada1 = float(input('Escribe el número:'))
        if raízcuadrada1 < 0 :
            print ('Error de cálculo (no existen raíces de números negativos)')
        else :
            resultado_raízcuadrada = raízcuadrada1 ** (1/2)
            print ('El resultado es:', resultado_raízcuadrada)
    elif elección == 7:
        porcentaje1 = float(input('Escribe el porcentaje (%)'))
        porcentaje2 = float(input('Escribe el número al que aplicar el porcentaje:'))
        resultado_porcentaje = (porcentaje1 / 100) * porcentaje2
        print ('El resultado es:', resultado_porcentaje)
    elif elección == 8:
        print ('Gracias por usar la calculadora python')
        break
    else :
        print ('Elección no válida, vuelve a intentarlo')

