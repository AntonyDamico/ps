def hacer_habitaciones(data, pos_caja_p, const_mts):
    '''
    Convierte el diccionario de data en objetos Habitacion
    '''
    data[0]['habAnterior'] = None
    habitaciones = [make_habitacion_principal(data[0], pos_caja_p)]
    data.pop(0)

    for hab in data:
        habitaciones.append(make_habitacion(hab, habitaciones, const_mts))

    return habitaciones


def make_habitacion_principal(data, caja_p):
    '''
    Devuelve un objeto Habitacion con una caja autogenerada
    '''
    habitacion_p = Habitacion(
        data['computadoras'], data['x'],
        data['y'], data['ancho'],
        data['alto'])
    habitacion_p.agregar_caja_principal(*[cord for cord in caja_p])
    return habitacion_p


def make_habitacion(data, habitaciones, const_mts):
    '''
    Crea un objeto habitacion con la informacion pasada en diccionario
    '''
    return Habitacion(
        data['computadoras'],
        data['x'], data['y'],
        data['ancho'], data['alto'],
        habitaciones[data['habAnterior']],
        const_mts
    )


def parseCajas(data):
    '''
    Convierte el diccionario data en un array de objetos
    tipo Caja
    '''
    cajas = []
    for caja in data:
        cajas.append(make_caja(caja))
    return cajas


def make_caja(data):
    '''
    Devuelva un objeto tipo Caja con la información que se le pasó
    '''
    return Caja(data['x'], data['y'], computadoras=data['computadoras'])


def calcular_habitaciones(habitaciones, margen_error, precio, pisos):
    '''
    Hace los cálculos del cableado con información de las habitaciones
    '''
    cableado_aereo = sum([hab.cableado_aereo for hab in habitaciones])
    cableado_bajada = sum([hab.cableado_bajada for hab in habitaciones])
    respuestas = {
        'cableado_aereo': cableado_aereo,
        'cableado_bajada': cableado_bajada
    }
    respuestas.update(calculos_generales(
        cableado_aereo, cableado_bajada, margen_error, precio, pisos))
    return respuestas


def calcular_cajas(cajas, const_mts, margen_error, precio, pisos):
    '''
    Hace los cálculos del cableado con información de las cajas 
    '''
    cableado_aereo = sum(
        [(caja.computadoras * (caja.x + caja.y)) for caja in cajas])
    cableado_bajada = sum([(caja.computadoras * const_mts) for caja in cajas])
    respuestas = {
        'cableado_aereo': cableado_aereo,
        'cableado_bajada': cableado_bajada
    }
    respuestas.update(calculos_generales(
        cableado_aereo, cableado_bajada, margen_error, precio, pisos))
    return respuestas


def calculos_generales(cableado_aereo, cableado_bajada, margen_error, precio, pisos):
    '''
    Realiza cálculos generales para el cableado
    '''
    error = (margen_error/100) * (cableado_aereo+cableado_bajada)
    total_piso = cableado_aereo + cableado_bajada + error
    precio_piso = total_piso * precio
    total_edificio = total_piso * pisos
    precio_edificio = precio_piso * pisos
    return {
        'error': error,
        'total_piso': total_piso,
        'precio_piso': precio_piso,
        'total_edificio': total_edificio,
        'precio_edificio': precio_edificio
    }


def calcular_pos_caja_principal(habitaciones):
    '''
    Calcula la posición de la caja en la habitación principal 
    '''
    hab_p = habitaciones[0]
    habs_arr = habitaciones[1:]
    pos_final = [0, 0]
    p_vecinos = [hab for hab in habs_arr if hab['habAnterior'] == 0]

    for vecino in p_vecinos:
        if hab_p['x'] > vecino['x']:
            pos_final[0] = hab_p['ancho']

        if hab_p['y'] > vecino['y']:
            pos_final[1] = hab_p['alto']
    return pos_final
