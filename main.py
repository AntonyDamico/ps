from . import utils

habitaciones = [
    {'numero': 0, 'computadoras': 0, 'x': 0, 'y':0, 'alto':4, 'ancho':4, 'habAnterior': 'ninguna'},
    {'numero': 1, 'computadoras': 3, 'x': 0, 'y':4, 'alto':4, 'ancho':4, 'habAnterior': 0},
    {'numero': 2, 'computadoras': 2, 'x': 4, 'y':0, 'alto':4, 'ancho':4, 'habAnterior': 0},
    {'numero': 3, 'computadoras': 2, 'x': 8, 'y':0, 'alto':4, 'ancho':4, 'habAnterior': 2},
    {'numero': 4, 'computadoras': 1, 'x': 12, 'y':0, 'alto':4, 'ancho':4, 'habAnterior': 3},
    {'numero': 5, 'computadoras': 4, 'x': 12, 'y':4, 'alto':4, 'ancho':4, 'habAnterior': 4},
]

const_cable_bajada = 8
margen_error = 12
precio_mt_cable = 3
pisos = 2

pos_caja_p = utils.calcular_pos_caja_principal(habitaciones)
habitaciones_objs = utils.hacer_habitaciones(habitaciones, pos_caja_p, const_cable_bajada)
respuestas = utils.calcular_habitaciones(habitaciones_objs, margen_error, precio_mt_cable, pisos)


print('cableado_aereo:', respuestas['cableado_aereo'])
print('cableado_bajada:', respuestas['cableado_bajada'])
print('error:', respuestas['error'])
print('total_piso:', respuestas['total_piso'])
print('precio_piso:', respuestas['precio_piso'])
print('total_edificio:', respuestas['total_edificio'])
print('precio_edificio:', respuestas['precio_edificio'])
