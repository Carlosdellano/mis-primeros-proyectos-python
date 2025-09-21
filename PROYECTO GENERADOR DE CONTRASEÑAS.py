import random
import string 
while True:
    print("========= MENÚ =========")
    print ('1. Solo letras')
    print ('2. Solo números')
    print ('3. Solo símbolos')
    print ('4. Letras y números')
    print ('5. Letras y símbolos')
    print ('6. Números y símbolos')
    print ('7. Letras, números y símbolos')
    print ('8. Salir')

    elección = int(input('Elige una opción:'))
    if elección == 1:
        carácteres1 = string.ascii_letters
        contraseña1 = ''
        longitud1 = int(input('¿De cuántos carácteres quieres tu contraseña?:'))
        for i in range (longitud1):
            contraseña1 += random.choice(carácteres1)
        print('Tu contraseña es:', contraseña1)
        print("\n" + "-"*40 + "\n")
    elif elección == 2:
        carácteres2 = string.digits
        contraseña2 = ''
        longitud2 = int(input('¿De cuántos carácteres quieres tu contraseña?:'))
        for i in range (longitud2):
            contraseña2 += random.choice(carácteres2)
        print('Tu contraseña es:', contraseña2)
        print("\n" + "-"*40 + "\n")
    elif elección == 3:
        carácteres3 = string.punctuation
        contraseña3 = ''
        longitud3 = int(input('¿De cuántos carácteres quieres tu contraseña?:'))
        for i in range (longitud3):
            contraseña3 += random.choice(carácteres3)
        print('Tu contraseña es:', contraseña3)
        print("\n" + "-"*40 + "\n")
    elif elección == 4:
         carácteres4 = string.ascii_letters + string.digits
         contraseña4 = ''
         longitud4 = int(input('¿De cuántos carácteres quieres tu contraseña?:'))
         for i in range (longitud4):
             contraseña4 += random.choice(carácteres4)
         print('Tu contraseña es:', contraseña4)
         print("\n" + "-"*40 + "\n")
    elif elección == 5:
          carácteres5 = string.ascii_letters + string.punctuation
          contraseña5 = ''
          longitud5 = int(input('¿De cuántos carácteres quieres tu contraseña?:'))
          for i in range (longitud5):
              contraseña5 += random.choice(carácteres5)
          print('Tu contraseña es:', contraseña5)
          print("\n" + "-"*40 + "\n")
    elif elección == 6:
          carácteres6 = string.digits + string.punctuation
          contraseña6 = ''
          longitud6 = int(input('¿De cuántos carácteres quieres tu contraseña?:'))
          for i in range (longitud6):
              contraseña6 += random.choice(carácteres6)
          print('Tu contraseña es:', contraseña6)
          print("\n" + "-"*40 + "\n")
    elif elección == 7:
          carácteres7 = string.ascii_letters + string.digits + string.punctuation
          contraseña7 = ''
          longitud7 = int(input('¿De cuántos carácteres quieres tu contraseña?:'))
          for i in range (longitud7):
              contraseña7 += random.choice(carácteres7)
          print('Tu contraseña es:', contraseña7)
          print("\n" + "-"*40 + "\n")
    elif elección == 8:
        print('Gracias por usar el generador de contraseñas python')
        break
    else:
        print('Opción no válida, vuelve a intentarlo')
    


