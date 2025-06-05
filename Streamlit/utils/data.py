# Configuración de líneas de producción
LINES = [
    {'id': 'blisters2', 'name': 'Línea de Blisters 2'},
    {'id': 'blisters3', 'name': 'Línea de Blisters 3'},
    {'id': 'blisters5', 'name': 'Línea de Blisters 5'},
    {'id': 'blisters7', 'name': 'Línea de Blisters 7'},
    {'id': 'blisters11', 'name': 'Línea de Blisters 11'},
    {'id': 'tableado33', 'name': 'Línea de Tableado 33'},
]

# Tipos de empaque
PACKAGING_TYPES = [
    {'id': 'empaqueprimario', 'name': 'Empaque Primario'},
    {'id': 'empaquesecundario', 'name': 'Empaque Secundario'},
]

# Chatbots por línea y tipo de empaque
CHATBOTS = {
    'blisters2': {
        'empaqueprimario': [
            {'name': 'Calefacción y Moldeo', 'id': 'ba97c6a6-53a4-418d-95b6-08bf787b4ac8'},
            {'name': 'Alimentación de Comprimidos', 'id': 'bot-id-2'},
            {'name': 'Sellado Blistera', 'id': 'bot-id-3'},
            {'name': 'Codificado Blistera', 'id': 'bot-id-4'},
            {'name': 'Corte y Troquelado', 'id': 'bot-id-5'},
            {'name': 'Transferencia de Blisters', 'id': 'bot-id-6'},
        ],
        'empaquesecundario': [
            {'name': 'Control de Calidad', 'id': 'bot-id-7'},
            {'name': 'Etiquetado', 'id': 'bot-id-8'},
        ]
    },
    # Puedes agregar más líneas aquí con sus respectivos bots
    'blisters3': {
        'empaqueprimario': [
            {'name': 'Calefacción y Moldeo', 'id': 'ba97c6a6-53a4-418d-95b6-08bf787b4ac8'},
            {'name': 'Alimentación de Comprimidos', 'id': 'bot-id-2'},
        ],
        'empaquesecundario': [
            {'name': 'Control de Calidad', 'id': 'bot-id-7'},
        ]
    },
    # Agregar el resto de líneas...
}