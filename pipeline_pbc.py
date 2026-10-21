import sqlite3
import pandas as pd
conexion = sqlite3.connect('sistema_bancario.db')
consulta_sql = """
SELECT * FROM volcado_pbc 
WHERE riesgo_sistema != 'Bajo'
ORDER BY id_cliente;
"""
df = pd.read_sql_query(consulta_sql, conexion)
conexion.close()
df['importe'] = pd.to_numeric(df['importe']).fillna(-1)
df['alerta_fraccionamiento'] = df['importe'].apply(
    lambda x: 'POSIBLE FRACCIONAMIENTO' if 4900 <= x < 5000 else 'Normal'
)
print(df[['id_cliente', 'importe', 'pais_destino', 'riesgo_sistema', 'alerta_fraccionamiento']])
df.to_csv('informe_final_pbc.csv', index=False)

