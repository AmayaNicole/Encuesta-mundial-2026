import os
import pandas as pd

# ==========================================
# ETAPA 3 - DISEÑO DEL STAR SCHEMA
# ==========================================

# --- RESPONSABLE: EU (DIMENSIONES DEMOGRÁFICAS) ---
def construir_dimensiones_demograficas(df_limpio):
    """Genera las tablas de dimensiones demográficas con sus respectivas claves primarias.
    
    Responsable: Eu
    """
    print("--- CONSTRUYENDO DIMENSIONES DEMOGRÁFICAS (Eu) ---")
    ruta_salida = "3_Tablas_Limpias/"
    os.makedirs(ruta_salida, exist_ok=True)
    
    # 1. Dim_Edad
    dim_edad = pd.DataFrame(df_limpio['RangoEdad'].dropna().unique(), columns=['RangoEdad'])
    dim_edad.insert(0, 'ID_Edad', range(1, 1 + len(dim_edad)))
    dim_edad.to_csv(os.path.join(ruta_salida, "Dim_Edad.csv"), index=False)
    print("✅ Dim_Edad.csv generada.")

    # 2. Dim_Genero
    dim_genero = pd.DataFrame(df_limpio['Genero'].dropna().unique(), columns=['Genero'])
    dim_genero.insert(0, 'ID_Genero', range(1, 1 + len(dim_genero)))
    dim_genero.to_csv(os.path.join(ruta_salida, "Dim_Genero.csv"), index=False)
    print("✅ Dim_Genero.csv generada.")

    # 3. Dim_Departamento
    dim_departamento = pd.DataFrame(df_limpio['Departamento'].dropna().unique(), columns=['Departamento'])
    dim_departamento.insert(0, 'ID_Departamento', range(1, 1 + len(dim_departamento)))
    dim_departamento.to_csv(os.path.join(ruta_salida, "Dim_Departamento.csv"), index=False)
    print("✅ Dim_Departamento.csv generada.")

    # 4. Dim_Municipio
    dim_municipio = pd.DataFrame(df_limpio['Municipio'].dropna().unique(), columns=['Municipio'])
    dim_municipio.insert(0, 'ID_Municipio', range(1, 1 + len(dim_municipio)))
    dim_municipio.to_csv(os.path.join(ruta_salida, "Dim_Municipio.csv"), index=False)
    print("✅ Dim_Municipio.csv generada.")

    # 5. Dim_Ocupacion
    dim_ocupacion = pd.DataFrame(df_limpio['Ocupacion'].dropna().unique(), columns=['Ocupacion'])
    dim_ocupacion.insert(0, 'ID_Ocupacion', range(1, 1 + len(dim_ocupacion)))
    dim_ocupacion.to_csv(os.path.join(ruta_salida, "Dim_Ocupacion.csv"), index=False)
    print("✅ Dim_Ocupacion.csv generada.")

    return dim_edad, dim_genero, dim_departamento, dim_municipio, dim_ocupacion


# --- RESPONSABLE: JONATHAN (DIMENSIONES DE MARKETING) ---
def construir_dimensiones_marketing(df_limpio):
    """Genera las tablas de dimensiones orientadas a marketing y publicidad.
    
    Responsable: Jonathan
    """
    print("\n--- CONSTRUYENDO DIMENSIONES DE MARKETING (Jonathan) ---")
    ruta_salida = "3_Tablas_Limpias/"
    os.makedirs(ruta_salida, exist_ok=True)
    
    # 1. Dim_Seleccion (Ajustado a 'SeleccionApoya' según estructura real)
    col_seleccion = 'SeleccionApoya' if 'SeleccionApoya' in df_limpio.columns else 'Seleccion_Apoyo'
    dim_seleccion = pd.DataFrame(df_limpio[col_seleccion].dropna().unique(), columns=['Seleccion'])
    dim_seleccion.insert(0, 'ID_Seleccion', range(1, 1 + len(dim_seleccion)))
    dim_seleccion.to_csv(os.path.join(ruta_salida, "Dim_Seleccion.csv"), index=False)
    print("✅ Dim_Seleccion.csv generada.")

    # 2. Dim_Jugador (Ajustado a 'JugadoresInfluyentes' según estructura real)
    col_jugador = 'JugadoresInfluyentes' if 'JugadoresInfluyentes' in df_limpio.columns else 'Jugador_Motivacion'
    dim_jugador = pd.DataFrame(df_limpio[col_jugador].dropna().unique(), columns=['Jugador'])
    dim_jugador.insert(0, 'ID_Jugador', range(1, 1 + len(dim_jugador)))
    dim_jugador.to_csv(os.path.join(ruta_salida, "Dim_Jugador.csv"), index=False)
    print("✅ Dim_Jugador.csv generada.")

    # 3. Dim_Promocion (Ajustado a 'PromocionPreferida' según estructura real)
    dim_promocion = pd.DataFrame(df_limpio['PromocionPreferida'].dropna().unique(), columns=['Tipo_Promocion'])
    dim_promocion.insert(0, 'ID_Promocion', range(1, 1 + len(dim_promocion)))
    dim_promocion.to_csv(os.path.join(ruta_salida, "Dim_Promocion.csv"), index=False)
    print("✅ Dim_Promocion.csv generada.")
    
    return dim_seleccion, dim_jugador, dim_promocion


# =====================================================================
# ESPACIO RESERVADO PARA: NICOLE (RESPONSABLE PRINCIPAL ETAPA 3)
# =====================================================================
# NICOLE: Aquí debes incluir la construcción de las dimensiones restantes
# (ej. Dim_Snacks, Dim_Tiempo) y la construcción de la Tabla de Hechos (Fact Table).
# =====================================================================


# ==========================================
# BLOQUE PRINCIPAL DE EJECUCIÓN (MAIN)
# ==========================================
if __name__ == "__main__":
    # Ruta del dataset limpio generado en la Etapa 2
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    RUTA_DATASET_LIMPIO = os.path.join(directorio_actual, "..", "3_Tablas_Limpias", "dataset_limpio.csv")

    if not os.path.exists(RUTA_DATASET_LIMPIO):
        print(f"Error: No se encontró el dataset limpio en: {RUTA_DATASET_LIMPIO}")
        print("Asegúrate de ejecutar primero etl.py para generar el archivo limpio.")
    else:
        # Cargar los datos limpios de la fase anterior
        df_limpio = pd.read_csv(RUTA_DATASET_LIMPIO)
        print(f"Dataset limpio cargado correctamente. Registros a procesar: {len(df_limpio)}\n")

        # 1. Ejecución de tu parte (Eu)
        construir_dimensiones_demograficas(df_limpio)
        
        # 2. Ejecución de la parte de Jonathan
        construir_dimensiones_marketing(df_limpio)

        # 3. Flujo de Nicole (A ser integrado por ella)
        # Aquí Nicole llamará a sus funciones para completar el Star Schema:
        # construir_dimensiones_consumo(df_limpio)
        # construir_tabla_hechos(df_limpio, ...)