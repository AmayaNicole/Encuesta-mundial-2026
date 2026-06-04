import pandas as pd
import os

def construir_dimensiones_marketing(df_limpio):
    print("--- CONSTRUYENDO DIMENSIONES DE MARKETING (Jonathan) ---")
    ruta_salida = "3_Tablas_Limpias/"
    os.makedirs(ruta_salida, exist_ok=True)
    
    # 1. Dim_Seleccion
    # Asumiendo que la columna se llama 'Seleccion_Apoyo' en el dataset limpio
    dim_seleccion = pd.DataFrame(df_limpio['Seleccion_Apoyo'].dropna().unique(), columns=['Seleccion'])
    dim_seleccion.insert(0, 'ID_Seleccion', range(1, 1 + len(dim_seleccion)))
    dim_seleccion.to_csv(f"{ruta_salida}Dim_Seleccion.csv", index=False)
    print("✅ Dim_Seleccion.csv generada.")

    # 2. Dim_Jugador
    # Asumiendo que la columna se llama 'Jugador_Motivacion'
    dim_jugador = pd.DataFrame(df_limpio['Jugador_Motivacion'].dropna().unique(), columns=['Jugador'])
    dim_jugador.insert(0, 'ID_Jugador', range(1, 1 + len(dim_jugador)))
    dim_jugador.to_csv(f"{ruta_salida}Dim_Jugador.csv", index=False)
    print("✅ Dim_Jugador.csv generada.")

    # 3. Dim_Promocion
    # Asumiendo que la columna se llama 'Promocion_Preferida'
    dim_promocion = pd.DataFrame(df_limpio['Promocion_Preferida'].dropna().unique(), columns=['Tipo_Promocion'])
    dim_promocion.insert(0, 'ID_Promocion', range(1, 1 + len(dim_promocion)))
    dim_promocion.to_csv(f"{ruta_salida}Dim_Promocion.csv", index=False)
    print("✅ Dim_Promocion.csv generada.")
    
    return dim_seleccion, dim_jugador, dim_promocion