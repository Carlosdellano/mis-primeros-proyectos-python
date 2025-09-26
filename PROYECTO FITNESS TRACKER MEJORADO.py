while True:
    print('1. Calcular IMC')
    print('2. Calcular calorías recomendadas (TDEE)')
    print('3. Sugerencia de alimentos según objetivo')
    print('4. Salir')
    
    elección = int(input('Elige una opción:'))
    if elección == 1:
        peso = float(input('Introduce tu peso (kg):'))
        altura = float(input('Introduce tu altura (m):'))
        resultado_IMC = peso / (altura ** 2)
        if resultado_IMC < 18.5 :
            print ('Tu IMC es:', resultado_IMC,'. Eso indica bajo peso. Revisa tu alimentación y consulta con un profesional si lo consideras necesario.')
            print("\n" + "-"*40 + "\n")
        elif 18.5 <= resultado_IMC <= 24.9  :
            print ('Tu IMC es:', resultado_IMC,'. Tu IMC está en el rango saludable. ¡Buen trabajo!')
            print("\n" + "-"*40 + "\n")
        elif 25 <= resultado_IMC <= 29.9  :
            print ('Tu IMC es:', resultado_IMC,'. Tu IMC indica sobrepeso. Estás por encima del rango saludable, sería recomendable cuidar la alimentación y la actividad física.')
            print("\n" + "-"*40 + "\n")
        elif 30 <= resultado_IMC <= 34.9  :
            print ('Tu IMC es:', resultado_IMC,'. Tu IMC indica obesidad grado I. Estás en un nivel de obesidad inicial, lo recomendable es trabajar en dieta y ejercicio constantes')
            print("\n" + "-"*40 + "\n")
        elif 35 <= resultado_IMC <= 39.9:
            print('Tu IMC es:', resultado_IMC,'. Tu IMC indica obesidad grado II. Es un nivel elevado de obesidad, sería aconsejable apoyo profesional en nutrición y entrenamiento.')
            print("\n" + "-"*40 + "\n")
        elif resultado_IMC >= 40: 
            print ('Tú IMC es:', resultado_IMC,'. Tu IMC indica obesidad grado III (mórbida). Este nivel implica un riesgo serio para la salud, es muy importante buscar atención médica especializada.')
            print("\n" + "-"*40 + "\n")
    elif elección == 2:
        edad = int(input('Introduce tu edad:').strip())
        sexo = input('Introduce tu sexo (M/F):').strip()
        peso = float(input('Introduce tu peso (kg):').strip())
        altura = float(input('Introduce tu altura (cm):').strip())
        nivel_actividad = input('Introduce tu nivel de actividad (sedentario, activo, muy activo):').lower().strip()
        if sexo == 'M':
            tdee = (10*peso) + (6.25*altura) - (5*edad) + 5
        else:
            tdee = (10*peso) + (6.25*altura) - (5*edad) - 161
        if nivel_actividad == 'sedentario' :
            tdee *= 1.2
        elif nivel_actividad == 'activo' :
            tdee *= 1.55
        elif nivel_actividad == 'muy activo' :
            tdee *= 1.75
        print (f'- TDEE (calorías para mantener tu peso): {tdee:.2f} calorías')
        print (f'- Para bajar peso, deberías consumir {tdee - 500:.2f} calorías')
        print (f'- Para subir peso deberías consumir {tdee + 300:.2f} calorías')
        print("\n" + "-"*40 + "\n")
    elif elección == 3:
        alimentos_bajar = ['Pechuga de pollo', 'Claras de huevo', 'Avena', 'Verduras', 'Yogur natural']
        alimentos_mantener = ['Arroz', 'Pescado blanco', 'Carne magra', 'Frutas variadas', 'Legumbres']
        alimentos_subir = ['Arroz', 'Pasta', 'Frutos secos', 'Aguacate', 'Carne roja', 'Salmón']
        objetivo = input('Introduce tu objetivo (bajar peso, mantener peso, subir peso):').lower().strip()
        if objetivo == 'bajar peso': 
            print ('Te recomendamos estos alimentos para bajar de peso:')
            for alimento in alimentos_bajar:
                print ('-', alimento)
        elif objetivo == 'mantener peso':
            print('Te recomendamos estos alimentos para mantener tu peso:')
            for alimento in alimentos_mantener:
                print('-', alimento)
        elif objetivo == 'subir peso':
            print('Te recomendamos estos alimentos para subir de peso:') 
            for alimento in alimentos_subir:
                print('-', alimento)
        print("\n" + "-"*40 + "\n")
    elif elección == 4:
        print('Gracias por usar el Fitness Tracker pyhton')
        break
    else:
        print('Opción no válida, vuelve a intentarlo')
        print('\n' + 40*'-' + '\n')
    