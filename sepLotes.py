#####################  Práctica 01: Procesamiento por lotes 1  ###################################

# Abre el archivo de entrada en modo lectura y el archivo de salida en modo escritura
with open("prueba2.txt", "r") as entrada, open("archivo_salida.txt", "w") as salida:
    # Lee cada línea del archivo de entrada
    for linea in entrada:
        # Divide la línea en sus componentes usando la coma como separador
        datos = linea.strip().split(',')

        # Separa los grupos hexadecimales y el par de enteros
        grupos_hexadecimales = datos[0].split(':')
        grupo_8 = grupos_hexadecimales[7].split('/')

        # Convierte los grupos hexadecimales a decimal
        grupos_decimal = [str(int(x, 16)) for x in grupos_hexadecimales[:7]]

        # Obtiene la segunda cadena de texto
        segunda_cadena = datos[2]

        # Convierte la dirección IP en hexadecimal
        ip_decimal = datos[5].split('.')
        ip_hexadecimal = '.'.join([format(int(x), 'X') for x in ip_decimal])

        # Escribe los resultados en el archivo de salida
        resultado = f"{segunda_cadena} : {' : '.join(grupos_decimal)} : {ip_hexadecimal}\n"
        salida.write(resultado)

# Cierra los archivos
entrada.close()
salida.close()
