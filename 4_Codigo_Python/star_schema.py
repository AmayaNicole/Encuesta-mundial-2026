import os
import pandas as pd

# =====================================================================
# ETAPA 3: DISEÑO DEL STAR SCHEMA  &  ETAPA 4: CONSTRUCCIÓN DE DIMENSIONES
# =====================================================================

# --- RESPONSABLE: EU (ETAPAS 3 Y 4 - DIMENSIONES DEMOGRÁFICAS) ---
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


# --- RESPONSABLE: JONATHAN (ETAPAS 3 Y 4 - DIMENSIONES DE MARKETING) ---
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
# ESPACIO RESERVADO PARA: NICOLE (RESPONSABLE PRINCIPAL ETAPAS 3 Y 4)
# =====================================================================
# NICOLE: Aquí debes incluir el diseño y construcción de las dimensiones 
# restantes y la integración final de la Tabla de Hechos (Fact Table).
# =====================================================================
# --- RESPONSABLE: NICOLE (DIMENSIONES DE CONSUMO Y TIEMPO) ---
# --- RESPONSABLE: NICOLE (DIMENSIONES DE CONSUMO Y TIEMPO) ---
def construir_dimensiones_consumo(df_limpio):
    """Genera las tablas de dimensiones orientadas al consumo de snacks y tiempo.
    
    Responsable: Nicole
    """
    print("\n--- CONSTRUYENDO DIMENSIONES DE CONSUMO Y TIEMPO (Nicole) ---")
    ruta_salida = "3_Tablas_Limpias/"
    os.makedirs(ruta_salida, exist_ok=True)

    # CORRECCIÓN: Nombres exactos basados en la estructura del df_limpio
    columnas_consumo = {
        'FrecuenciaConsumoSnacks': ('Dim_Frecuencia.csv', 'ID_Frecuencia'),
        'LugarCompraSnacks': ('Dim_LugarCompra.csv', 'ID_LugarCompra'),
        'ConQuienVePartidos': ('Dim_CompaniaPartidos.csv', 'ID_CompaniaPartidos'),
        'SnacksSeleccionados': ('Dim_Snacks.csv', 'ID_Snack'),
        'SaborPreferido': ('Dim_Sabor.csv', 'ID_Sabor'),
        'PresentacionPreferida': ('Dim_Presentacion.csv', 'ID_Presentacion')
    }
    
    tablas_generadas = []
    for col, (archivo, id_col) in columnas_consumo.items():
        dim_df = pd.DataFrame(df_limpio[col].dropna().unique(), columns=[col])
        dim_df.insert(0, id_col, range(1, 1 + len(dim_df)))
        dim_df.to_csv(os.path.join(ruta_salida, archivo), index=False)
        print(f"✅ {archivo} generada.")
        tablas_generadas.append(dim_df)

    # CORRECCIÓN: Dimensión de Tiempo usando 'FechaEncuesta'
    col_tiempo = 'FechaEncuesta' if 'FechaEncuesta' in df_limpio.columns else None
    if col_tiempo:
        dim_tiempo = pd.DataFrame(df_limpio[col_tiempo].dropna().unique(), columns=[col_tiempo])
    else:
        dim_tiempo = pd.DataFrame(['2026-06-01'], columns=['FechaEncuesta'])
    
    dim_tiempo.insert(0, 'ID_Tiempo', range(1, 1 + len(dim_tiempo)))
    dim_tiempo.to_csv(os.path.join(ruta_salida, "Dim_Tiempo.csv"), index=False)
    print("✅ Dim_Tiempo.csv generada.")
    tablas_generadas.append(dim_tiempo)

    return tuple(tablas_generadas)


def construir_tabla_hechos(df_limpio, dim_edad, dim_genero, dim_depto, dim_muni, dim_ocupacion, 
                           dim_seleccion, dim_jugador, dim_promocion,
                           dim_frecuencia, dim_lugar, dim_compania, dim_snack, dim_sabor, dim_presentacion, dim_tiempo):
    """Une el dataset limpio con todas las dimensiones para generar la Fact Table central.
    
    Responsable: Nicole
    """
    print("\n--- CONSTRUYENDO TABLA DE HECHOS CENTRAL (Nicole) ---")
    ruta_salida = "3_Tablas_Limpias/"
    fact = df_limpio.copy()
    
    # Cruces demográficos (Eu)
    fact = fact.merge(dim_edad, on='RangoEdad', how='left')
    fact = fact.merge(dim_genero, on='Genero', how='left')
    fact = fact.merge(dim_depto, on='Departamento', how='left')
    fact = fact.merge(dim_muni, on='Municipio', how='left')
    fact = fact.merge(dim_ocupacion, on='Ocupacion', how='left')
    
    # Cruces de marketing (Jonathan)
    col_sel = 'SeleccionApoya' if 'SeleccionApoya' in fact.columns else 'Seleccion_Apoyo'
    fact = fact.merge(dim_seleccion, left_on=col_sel, right_on='Seleccion', how='left')
    col_jug = 'JugadoresInfluyentes' if 'JugadoresInfluyentes' in fact.columns else 'Jugador_Motivacion'
    fact = fact.merge(dim_jugador, left_on=col_jug, right_on='Jugador', how='left')
    fact = fact.merge(dim_promocion, left_on='PromocionPreferida', right_on='Tipo_Promocion', how='left')
    
    # CORRECCIÓN: Cruces de consumo con nombres reales
    fact = fact.merge(dim_frecuencia, on='FrecuenciaConsumoSnacks', how='left')
    fact = fact.merge(dim_lugar, on='LugarCompraSnacks', how='left')
    fact = fact.merge(dim_compania, on='ConQuienVePartidos', how='left')
    fact = fact.merge(dim_snack, on='SnacksSeleccionados', how='left')
    fact = fact.merge(dim_sabor, on='SaborPreferido', how='left')
    fact = fact.merge(dim_presentacion, on='PresentacionPreferida', how='left')
    
    # CORRECCIÓN: Cruce de tiempo
    col_tiempo = 'FechaEncuesta' if 'FechaEncuesta' in fact.columns else None
    if col_tiempo and col_tiempo in dim_tiempo.columns:
        fact = fact.merge(dim_tiempo, on=col_tiempo, how='left')
    else:
        fact['ID_Tiempo'] = 1

    # CORRECCIÓN: Filtrado final de columnas lógicas (Cambiando Precio_Aceptado por PrecioAdecuado)
    columnas_fact = [
        'ID_Edad', 'ID_Genero', 'ID_Departamento', 'ID_Municipio', 'ID_Ocupacion',
        'ID_Seleccion', 'ID_Jugador', 'ID_Promocion',
        'ID_Frecuencia', 'ID_LugarCompra', 'ID_CompaniaPartidos', 'ID_Snack', 'ID_Sabor', 'ID_Presentacion',
        'ID_Tiempo', 'PrecioAdecuado'
    ]
    
    fact_table = fact[columnas_fact]
    fact_table.insert(0, 'ID_Encuesta', range(1, 1 + len(fact_table)))
    fact_table.to_csv(os.path.join(ruta_salida, "Fact_Encuestas.csv"), index=False)
    print("✅ Fact_Encuestas.csv generada con éxito. ¡Modelo Star Schema completo!")
    
    return fact_table

# ==========================================
# BLOQUE PRINCIPAL DE EJECUCIÓN (MAIN)
# ==========================================
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

        # Ejecución del pipeline de construcción (Etapa 4)
        
        # 1. Ejecución de Eu (¡AQUÍ ATRAPAMOS LAS VARIABLES!)
        dim_edad, dim_genero, dim_departamento, dim_municipio, dim_ocupacion = construir_dimensiones_demograficas(df_limpio)
        
        # 2. Ejecución de la parte de Jonathan (¡AQUÍ ATRAPAMOS LAS VARIABLES!)
        dim_seleccion, dim_jugador, dim_promocion = construir_dimensiones_marketing(df_limpio)

        # 3. Flujo de Nicole 
        dim_frec, dim_lug, dim_comp, dim_snk, dim_sab, dim_pres, dim_tiem = construir_dimensiones_consumo(df_limpio)

        # 4. Construcción final de la Tabla de Hechos
        fact_encuestas = construir_tabla_hechos(
            df_limpio, 
            dim_edad, dim_genero, dim_departamento, dim_municipio, dim_ocupacion,
            dim_seleccion, dim_jugador, dim_promocion,
            dim_frec, dim_lug, dim_comp, dim_snk, dim_sab, dim_pres, dim_tiem
         )