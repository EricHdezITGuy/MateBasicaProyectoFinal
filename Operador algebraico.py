""" 
Operador Algebraico
Autor: Eric Hernandez Marin
Curso: Lógica y Matemática Básica 2021-1 SC37 
"""

memoria = []

respuestas = (1, 2, 3)
respuestas_1 = (0, 1)

''' Aquí se crean las tuplas para que el programa aprenda el abecedario y números'''
letras = 'abcdefghijklmnñopqretuvwxyz'
letras = tuple(letras + letras.upper())
números = tuple('0123456789')

'''Este método convierte la elección de string a int'''
def opción(pregunta):
    if pregunta == '0':
        return 0
    elif pregunta == '1':
        return 1
    elif pregunta == '2':
        return 2
    elif pregunta == '3':
        return 3

'''Esto revisa si un elemento tiene "/" y lo convierte en su inverso multiplicativo'''
def divisor(expresión):
    separador = expresión.split('/')

    for i in range(1, len(separador)):

        if set(separador[i]) & set(letras) == set():
            continue

        contenedor_constantes = []

        for n in separador[i]:
            try:
                if n == '.' or n == '-':
                    pass
                else:
                    int(n)
                contenedor_constantes.append(n)
            except ValueError:
                if len(contenedor_constantes) != 0:
                    separador[i] = separador[i].replace(separador[i][0: separador[i].index(
                        n)], str(float(''.join(contenedor_constantes)) ** -1), 1)
                break

        monomio = ''

        for n in separador[i]:
            if n == '*':
                break
            else:
                monomio += n

        if len(contenedor_constantes) != 0:
            monomio = monomio.replace(
                str(float(''.join(contenedor_constantes)) ** -1), '', 1)

        contenedor_1 = []

        for k in range(len(monomio)):
            try:
                if not monomio[k] in letras:
                    continue
                elif monomio[k] in letras and monomio[k + 1] != '^':
                    contenedor_1.append(monomio[k] + '^1')
                elif monomio[k] in letras and monomio[k + 1] == '^':
                    contenedor_2 = monomio[k] + '^'
                    for k_1 in monomio[k + 2: len(monomio)]:
                        try:
                            if k_1 != '.' and k_1 != '-':
                                int(k_1)
                            contenedor_2 += k_1
                        except ValueError:
                            break
                    contenedor_1.append(contenedor_2)
            except IndexError:
                contenedor_1.append(monomio[k] + '^1')

        contenedor_1.sort()
        contenedor_3 = []
        contenedor_3.append(contenedor_1[0][0: 2])
        contenedor_4 = 0

        for j in contenedor_1:
            if j[0: 2] in contenedor_3:
                contenedor_4 += -float(j[2: len(j)])
            else:
                contenedor_3[-1] = contenedor_3[-1] + str(contenedor_4)
                contenedor_4 = -float(j[2: len(j)])
                contenedor_3.append(j[0: 2])
        contenedor_3[-1] = contenedor_3[-1] + str(contenedor_4)

        if len(contenedor_constantes) != 0:
            monomio = str(float(''.join(contenedor_constantes))
                          ** -1) + ''.join(contenedor_3)
        else:
            monomio = ''.join(contenedor_3)

        if not '*' in separador[i]:
            separador[i] = monomio
        else:
            separador[i] = separador[i].replace(
                separador[i][0: separador[i].index('*')], monomio, 1)

    for i in range(len(separador)):
        if i == 0:
            continue

        if not '*' in separador[i]:
            if set(separador[i]) & set(letras) == set():
                if '^' in separador[i]:
                    potencia = separador[i].split('^')
                    separador[i] = str(float(potencia[0]) ** float(potencia[1]))
                separador[i] = str(float(separador[i]) ** -1)
        else:
            copia = separador[i].split('*', maxsplit=1)[0]
            copia_1 = separador[i].split('*', maxsplit=1)[1]
            if set(copia) & set(letras) == set():
                if '^' in copia:
                    potencia = copia.split('^')
                    copia = str(float(potencia[0]) ** float(potencia[1]))
                copia = str(float(copia) ** -1)
            separador[i] = copia + '*' + copia_1

    new_monomio = '*'.join(separador)
    return new_monomio

'''Toma las constantes de la expresión original y las multiplica; las que son iguales las suma'''
def multiplicador(expresión):

    separador = expresión.split('*')
    contenedor_constantes = []

    for i in range(len(separador)):
        if separador[i][0] in letras:
            continue

        if set(separador[i]) & set(letras) != set():
            contenedor_1 = ''

            for n in separador[i]:
                try:
                    if n != '.' and n != '-' and n != '^':
                        int(n)
                    contenedor_1 += n
                except ValueError:
                    contenedor_constantes.append(contenedor_1)
                    separador[i] = separador[i].replace(contenedor_1, '', 1)
                    break
        else:
            contenedor_constantes.append(separador[i])
            separador[i] = ''

    if len(contenedor_constantes) > 0:
        for i in range(len(contenedor_constantes)):
            if contenedor_constantes[i] == '-':
                contenedor_constantes[i] = '-1'

        for i in range(len(contenedor_constantes)):
            if '^' in contenedor_constantes[i]:
                contenedor_constantes[i] = float(contenedor_constantes[i].split(
                    '^')[0]) ** float(contenedor_constantes[i].split('^')[1])
            else:
                contenedor_constantes[i] = float(contenedor_constantes[i])

        contenedor_2 = 1

        for i in range(len(contenedor_constantes)):
            contenedor_2 *= contenedor_constantes[i]

        contenedor_2 = str(contenedor_2)

    just_variable = ''.join(separador)
    if just_variable != '':
        contenedor_3 = []

        for i in range(len(just_variable)):
            try:
                if not just_variable[i] in letras:
                    continue
                elif just_variable[i] in letras and just_variable[i + 1] != '^':
                    contenedor_3.append(just_variable[i] + '^1')
                elif just_variable[i] in letras and just_variable[i + 1] == '^':
                    contenedor_4 = ''
                    for n in just_variable[i + 2: len(just_variable)]:
                        try:
                            if n != '.' and n != '-' and n != '^':
                                int(n)
                            contenedor_4 += n
                        except ValueError:
                            break
                    if '^' in contenedor_4:
                        contenedor_4 = multiplicador(contenedor_4)
                    contenedor_3.append(just_variable[i] + '^' + contenedor_4)
            except IndexError:
                contenedor_3.append(just_variable[i] + '^1')

        contenedor_3.sort()
        contenedor_5 = []
        contenedor_5.append(contenedor_3[0][0: 2])
        contenedor_6 = 0

        for i in contenedor_3:
            if i[0: 2] in contenedor_5:
                contenedor_6 += float(i[2: len(i)])

            else:
                contenedor_5[-1] = contenedor_5[-1] + str(contenedor_6)
                contenedor_6 = float(i[2: len(i)])
                contenedor_5.append(i[0: 2])
        contenedor_5[-1] = contenedor_5[-1] + str(contenedor_6)
        just_variable = ''.join(contenedor_5)

    if len(contenedor_constantes) > 0 and just_variable != '':
        new_monomio = contenedor_2 + just_variable
    elif len(contenedor_constantes) == 0 and just_variable != '':
        new_monomio = just_variable
    if len(contenedor_constantes) > 0 and just_variable == '':
        new_monomio = contenedor_2

    return new_monomio

'''Este método busca aplicar la jerarquía de los parentesís y así poder ejecutarlos en el orden correcto'''
def paréntesis(expresión):
    while '(' in expresión:

        if expresión.count('(') == 1 and (expresión[0] == '(' or expresión[-1] == ')'):
            break

        copia = expresión.replace('((', '(°(')
        copia = copia.replace('))', ')°)')

        separador = copia.split('(')
        while '' in separador:
            separador.remove('')
        contenedor_1 = '('.join(separador[0: -1]).replace('°', '')
        copia = separador[-1]
        separador = copia.split(')')
        while '' in separador:
            separador.remove('')
        contenedor_2 = ')'.join(separador[1: len(separador)]).replace('°', '')
        copia = separador[0]

        if '/' in copia:
            copia = multiplicador(divisor(copia))
        else:
            copia = multiplicador(copia)

        if contenedor_1[-1] == '^' and contenedor_1[-2] == ')':

            separador = contenedor_1.split('(')
            separador[-1] = separador[-1].replace(')^', '')

            if '/' in separador[-1]:
                separador[-1] = multiplicador(divisor(separador[-1]))
            else:
                separador[-1] = multiplicador(separador[-1])
            contenedor_constantes = ''
            for i in separador[-1]:
                if i in letras:
                    break
                else:
                    contenedor_constantes += i
            contenedor_3 = []
            for i in range(len(separador[-1])):
                try:
                    if not separador[-1][i] in letras:
                        continue
                    elif separador[-1][i] in letras and separador[-1][i + 1] != '^':
                        contenedor_3.append(separador[i] + '^' + copia)
                    elif separador[-1][i] in letras and separador[-1][i + 1] == '^':
                        contenedor_4 = ''
                        for j in separador[-1][i + 2: len(separador[-1])]:
                            try:
                                if j != '.' and j != '-':
                                    int(j)
                                contenedor_4 += j
                            except ValueError:
                                break
                        contenedor_4 = str(float(contenedor_4) * float(copia))
                        contenedor_3.append(
                            separador[-1][i] + '^' + contenedor_4)
                except IndexError:
                    contenedor_3.append(separador[i] + '^' + copia)

            contenedor_6 = ''.join(contenedor_3) + ')'

            if contenedor_constantes != '':
                contenedor_6 = str(float(contenedor_constantes)
                                   ** float(copia)) + contenedor_6
            separador[-1] = contenedor_6

            if len(separador) > 1:
                expresión = '('.join(separador) + contenedor_2
            elif len(separador) == 1:
                expresión = '(' + ''.join(separador) + contenedor_2

            contenedor_2 = ''
        elif contenedor_1[-1] == '(' or contenedor_1[-1] == '*' or contenedor_1[-1] == '/' or (contenedor_1[-1] == '^' and contenedor_1[-2] != ')'):
            if expresión[0] != '(':
                expresión = contenedor_1 + copia
            else:
                expresión = '(' + contenedor_1 + copia
        elif contenedor_1[-1] in letras or contenedor_1[-1] in números or contenedor_1[-1] == ')':
            if expresión[0] != '(':
                expresión = contenedor_1 + '*' + copia
            else:
                expresión = '(' + contenedor_1 + '*' + copia

        if contenedor_2 != '':
            if contenedor_2[0] == ')' or contenedor_2[0] == '*' or contenedor_2[0] == '/' or contenedor_2[0] == '^':
                expresión = expresión + contenedor_2
            elif contenedor_2[0] in letras or contenedor_2[0] in números:
                expresión = expresión + '*' + contenedor_2

    if expresión[0] == '(' and expresión[-1] != ')':
        if not ')^' in expresión:
            expresión = expresión.replace('(', '')
            separador = expresión.split(')')

            if '/' in separador[0]:
                separador[0] = multiplicador(divisor(separador[0]))
            else:
                separador[0] = multiplicador(separador[0])

            if separador[1][0] == '*' or separador[1][0] == '/' or separador[1][0] == '^':
                expresión = ''.join(separador)
            else:
                expresión = '*'.join(separador)
        else:
            expresión = expresión.replace('(', '')
            separador = expresión.split(')')
            separador[1] = separador[1].replace('^', '', 1)

            if '/' in separador[0]:
                separador[0] = multiplicador(divisor(separador[0]))
            else:
                separador[0] = multiplicador(separador[0])

            contenedor_exponentes = ''

            for i in separador[1]:
                try:
                    if i != '.' or i != '-' or i != '^':
                        int(i)
                    contenedor_exponentes += i
                except ValueError:
                    break

            separador[1] = separador[1].replace(contenedor_exponentes, '', 1)

            if '^' in contenedor_exponentes:
                contenedor_exponentes = multiplicador(contenedor_exponentes)

            contenedor_constantes = ''
            for i in separador[0]:
                if i in letras:
                    break
                else:
                    contenedor_constantes += i
            if '^' in contenedor_constantes:
                contenedor_constantes = multiplicador(contenedor_constantes)
            if contenedor_constantes != '':
                contenedor_constantes = str(
                    float(contenedor_constantes) ** float(contenedor_exponentes))

            contenedor_7 = []
            for i in range(len(separador[0])):
                try:
                    if not separador[0][i] in letras:
                        continue
                    elif separador[0][i] in letras and separador[0][i + 1] != '^':
                        contenedor_7.append(
                            separador[0][i] + '^' + contenedor_exponentes)
                    elif separador[0][i] in letras and separador[0][i + 1] == '^':
                        contenedor_8 = ''
                        for n in separador[0][i + 2: len(separador[0])]:
                            try:
                                if n != '.' and n != '-':
                                    int(n)
                                contenedor_8 += n
                            except ValueError:
                                break
                        contenedor_7.append(
                            separador[0][i] + '^' + str(float(contenedor_8) * float(contenedor_exponentes)))

                except IndexError:
                    contenedor_7.append(
                        separador[0][i] + '^' + contenedor_exponentes)

            if contenedor_constantes != '':
                expresión = contenedor_constantes + ''.join(contenedor_7)
            else:
                expresión = ''.join(contenedor_7)

            if separador[1] != '':
                expresión = expresión + separador[1]
    elif expresión[0] != '(' and expresión[-1] == ')':
        expresión = expresión.replace(')', '')
        separador = expresión.split('(')

        if '/' in separador[1]:
            separador[1] = multiplicador(divisor(separador[1]))
        else:
            separador[1] = multiplicador(separador[1])

        if separador[0][-1] == '*' or separador[0][-1] == '/' or separador[0][-1] == '^':
            expresión = ''.join(separador)
        else:
            expresión = '*'.join(separador)
    elif expresión[0] == '(' and expresión[-1] == ')':
        expresión = expresión.replace('(', '')
        expresión = expresión.replace(')', '')

    if '/' in expresión:
        expresión = multiplicador(divisor(expresión))
    else:
        expresión = multiplicador(expresión)

    return expresión

'''Este método diferencia las variables, los exponentes y la constante. Le da la opción de guardar en la lista de memoria.'''
def just_monomio(monomio):
    print('El resultado es: ' + monomio)

    separador = {'variables': [], 'constante': [], 'exponentes': []}

    def diferenciador(verificador, monomio_1):
        copia_monomio = monomio_1

        if verificador != set():

            for i in verificador:
                separador['variables'].append(i)
                copia_monomio = copia_monomio.replace(i, '')

            if copia_monomio != '' and copia_monomio != '-':
                separador['constante'].append(str(float(copia_monomio)))
            elif copia_monomio == '':
                separador['constante'].append('1.0')
            elif copia_monomio == '-':
                separador['constante'].append('-1.0')
        else:
            separador['constante'].append(str(float(copia_monomio)))

    if not '^' in monomio:
        diferenciador(set(letras).intersection(monomio), monomio)
    else:
        copia_monomio = monomio

        while '^' in copia_monomio:
            contenedor_exponentes = []
            separador_1 = copia_monomio.split('^', maxsplit=1)

            if separador_1[1][0] == '-':
                contenedor_exponentes.append('-')
                separador_1[1] = separador_1[1].replace('-', '', 1)

            for i in separador_1[1]:
                try:
                    if i != '.':
                        int(i)
                    contenedor_exponentes.append(i)
                except ValueError:
                    separador_1[1] = separador_1[1].replace(
                        separador_1[1][0: separador_1[1].index(i)], '', 1)
                    break

            separador['exponentes'].append(''.join(contenedor_exponentes))

            if separador['exponentes'][-1] == '0' and separador_1[0][-1] in letras:
                monomio = monomio.replace(separador_1[0][-1] + '^' + '0', '')

            diferenciador(set(letras).intersection(
                separador_1[0]), separador_1[0])

            copia_monomio = separador_1[1]

        if copia_monomio != '':
            diferenciador(set(letras).intersection(
                copia_monomio), copia_monomio)

    while len(separador['constante']) > 1:
        separador['constante'].pop()

    for i in separador.items():
        print(i[0] + ' : ' + ', '.join(i[1]))

    if monomio == '' or monomio in memoria:
        print('La expresión no será guardada')
    else:
        pregunta = opción(
            input('¿Guardar resultado en memoria? (Sí : 1 / No : 0): '))

        while not pregunta in respuestas_1:
            pregunta = opción(input('Seleccione una opción válida: '))

        if pregunta == 1:
            memoria.append(monomio)
            print('!La expresión "' + monomio + '" ha sido guardada en memoria!')
        else:
            print('!La expresión "' + monomio + '" ha sido eliminada!')


'''Este método viene a reemplazar lo que esté en memoria.'''
def reemplazar(dato_memoria):
    variables = set(dato_memoria) & set(letras)

    if variables == set():
        print('No hay variables en la expresión')
    else:
        variables = tuple(variables)

        for i in range(len(variables)):
            print(str(i) + ' : ' + variables[i])

        b = True

        while b == True:
            variable = input('Elija la variable a reemplazar: ')

            if variable in variables:
                b = False
            else:
                print('Intente de nuevo')

        b = True

        while b == True:
            try:
                número = str(
                    float(input('Ingrese el número por el cual desea reemplazar la variable: ')))
                b = False
            except ValueError:
                print('Intente de nuevo')

        contenedor_constantes = ''

        for i in dato_memoria:
            if i in letras:
                break
            else:
                contenedor_constantes += i

        if contenedor_constantes != '':
            dato_memoria = dato_memoria.replace(contenedor_constantes, '', 1)

        separador = list(dato_memoria)

        for i in range(len(separador)):
            if separador[i] != variable:
                continue
            else:
                if i == 0 and len(separador) == 1:
                    separador[i] = número
                elif i == 0 and len(separador) > 1:
                    if separador[i + 1] == '^':
                        separador[i] = número
                    else:
                        separador[i] = número + '*'
                elif i > 0:
                    try:
                        if separador[i + 1] == '^':
                            separador[i] = '*' + número
                        else:
                            separador[i] = '*' + número + '*'
                    except IndexError:
                        separador[i] = '*' + número

        dato_memoria = ''.join(separador)

        if contenedor_constantes != '':
            dato_memoria = contenedor_constantes + '*' + dato_memoria

        return dato_memoria

'''Este método está para imprimir el menú, luego tiene un input donde empieza a tomar los datos para darle continuidad a las opciones del menú.'''
def Interacción_usuario():
    print('=================================')
    print('Bienvenido al operador algebraico')
    print('=================================')
    print('Creado por Eric Hernandez Marin')
    print('=================================')
    print('')
    print('Seleccione una de las siguientes opciones:')
    print('')
    print('1- Ingresar una expresión. Recuerda encerrar los exponentes entre paréntesis')
    print('2- Mostrar monomios en memoria.')
    print('3- Reemplazar una variable de un monomio de la memoria')
    print('')

    pregunta = opción(input('Seleccione una opción: '))

    while not pregunta in respuestas:
        pregunta = opción(input('Seleccione una opción válida: '))

    if pregunta == 1:
        dato_usuario = input('Ingrese la expresión: ')
        dato_usuario = dato_usuario.replace(' ', '')
        dato_usuario = dato_usuario.replace('[', '(')
        dato_usuario = dato_usuario.replace(']', ')')
        dato_usuario = dato_usuario.replace('{', '(')
        dato_usuario = dato_usuario.replace('}', ')')

        if '(' in dato_usuario:
            just_monomio(paréntesis(dato_usuario))
        else:
            if '/' in dato_usuario:
                just_monomio(multiplicador(divisor(dato_usuario)))
            else:
                just_monomio(multiplicador(dato_usuario))

    elif pregunta == 2:
        if memoria != []:
            for i in memoria:
                print(memoria.index(i), ':', i)
        else:
            print('La memoria está vacía')

    elif pregunta == 3:
        if memoria != []:
            for i in memoria:
                print(memoria.index(i), ':', i)

            b = True

            while b == True:
                try:
                    dato = int(input('Ingrese el índice del monomio: '))

                    if not dato in tuple(range(len(memoria))):
                        print('Intente de nuevo')
                    else:
                        dato = memoria[dato]
                        b = False
                except ValueError:
                    print('Intente de nuevo')

            new_dato = reemplazar(dato)

            if new_dato == None:
                pass
            else:
                just_monomio(multiplicador(new_dato))

        else:
            print('La memoria está vacía')

    pregunta_1 = opción(
        input('¿Volver al menú de inicio? (Sí : 1 / No : 0): '))

    while not pregunta_1 in respuestas_1:
        pregunta_1 = opción(input('Seleccione una opción válida: '))

    if pregunta_1 == 1:
        Interacción_usuario()


Interacción_usuario()