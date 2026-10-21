import pandas as pd
datos = {
    'id_operacion': [101, 102, 103, 104, 105, 106],
    'id_cliente': [5001, 5002, 5001, 5003, 5004, 5002],
    'importe': [1250.00, 8500.50, 300.00, 12000.00, None, 6200.00],
    'pais_origen': ['España', 'Suiza', 'España', 'Panamá', 'España', 'Suiza'],
    'tipo_alerta': ['Normal', None, 'Normal', 'Bloqueada', 'Normal', 'Revisión']
}
df = pd.DataFrame(datos)
print(df)

df['importe'] = df['importe'].fillna(0)
df['tipo_alerta'] = df['tipo_alerta'].fillna('Desconocido')

print(df)

df.to_csv('datos_limpios.csv', index=False)