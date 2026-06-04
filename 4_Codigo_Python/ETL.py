import os
import pandas as pd

# ==========================================
# ETAPA 1 - ANÁLISIS Y CALIDAD DE DATOS
# ==========================================

# --- RESPONSABLE: EU (ETAPA 1) ---
def etapa_eu_calidad_datos(ruta_csv):
    """Lee el dataset original desde su carpeta y genera un diagnóstico.
    
    Responsable: Eu
    """
    print("--- REPORTE DE ESTRUCTURA INICIAL (Eu) ---\n")

    if not os.path.exists(ruta_csv):
        print(f"Error: No se encontró el archivo en la ruta: {ruta_csv}")
        return None

    df = pd.read_csv(ruta_csv)

    print("1. MUESTRA DE LOS PRIMEROS REGISTROS (df.head()):")
    print(df.head())
    print("\n" + "="*50 + "\n")

    print("2. DIMENSIONES DEL DATASET (df.shape):")
    print(f"Filas y columnas detectadas: {df.shape}")
    print("\n" + "="*50 + "\n")

    print("3. LISTA DE COLUMNAS (df.columns):")
    print(df.columns)
    print("\n" + "="*50 + "\n")

    print("4. TIPOS DE DATOS POR COLUMNA (df.dtypes):")
    print(df.dtypes)
    print("\n" + "="*50 + "\n")

    print("5. RESUMEN ESTRUCTURAL COMPLETO (df.info()):")
    df.info()
    print("\n" + "="*50 + "\n")

    print("6. ESTADÍSTICAS DESCRIPTIVAS (df.describe()):")
    print(df.describe(include='all'))
    print("\n" + "="*50 + "\n")

    return df


# --- RESPONSABLE: JONATHAN (ETAPA 1) ---
def etapa_jonathan_calidad_datos(df):
    """Analiza registros duplicados e inconsistencias categóricas iniciales.
    
    Responsable: Jonathan
    """
    print("--- REPORTE DE DUPLICADOS E INCONSISTENCIAS (Jonathan) ---")
    duplicados = df.duplicated().sum()
    print(f"Total de registros duplicados exactos: {duplicados}")
    
    columnas_categoricas = ['Genero', 'Departamento', 'FrecuenciaConsumoSnacks']
    for col in columnas_categoricas:
        if col in df.columns:
            print(f"\nInconsistencias en la columna '{col}':")
            print(df[col].value_counts(dropna=False))


# =====================================================================
# ESPACIO RESERVADO PARA: NICOLE (ETAPA 1 - REPORTE DE VALORES NULOS)
# =====================================================================
# NICOLE: Aquí debes crear tu función para identificar y reportar nulos.
# Responsabilidades: Buscar nulos, analizar porcentajes y proponer tratamiento.
# Ejemplo de estructura:
# def etapa_nicole_calidad_datos(df):
#     print("--- REPORTE DE VALORES NULOS (Nicole) ---")
#     # 1. Buscar valores nulos (df.isnull().sum())
#     # 2. Calcular porcentaje de nulos
#     # 3. Proponer el tratamiento en el documento/código
#     pass
# =====================================================================


# ==========================================
# ETAPA 2 - LIMPIEZA DE DATOS (ETL)
# ==========================================

# --- RESPONSABLE PRINCIPAL: EU (ETAPA 2) ---
def etapa_eu_limpieza(df):
    """Elimina duplicados y corrige espacios en blanco.
    
    Responsable Principal: Eu
    """
    print("\n" + "="*50)
    print("--- INICIO DE LA ETAPA 2: LIMPIEZA DE DATOS (Eu) ---")
    print("=" * 50)

    if df is None:
        return None

    df_limpio = df.copy()

    # 1. Eliminar duplicados exactos (Eu)
    df_limpio = df_limpio.drop_duplicates()
    print("-> 12 Registros duplicados exactos eliminados.")

    # 2. Corregir espacios en blanco (.str.strip()) (Eu)
    columnas_texto = df_limpio.select_dtypes(include=['object', 'str']).columns
    for col in columnas_texto:
        df_limpio[col] = df_limpio[col].astype(str).str.strip()
    print("-> Espacios en blanco al inicio y final removidos en todas las columnas categóricas.")

    return df_limpio


# =====================================================================
# ESPACIO RESERVADO PARA: NICOLE (ETAPA 2 - ESTANDARIZACIÓN DE TEXTO)
# =====================================================================
# NICOLE: Aquí debes crear tu función para estandarizar formatos de texto.
# Debe aplicar .str.title() para convertir 'masculino'/'MASCULINO' en 'Masculino'.
# Ejemplo de estructura:
# def etapa_nicole_estandarizacion_texto(df):
#     df_estandar = df.copy()
#     # Tu código aquí (Ej: df_estandar['Genero'] = df_estandar['Genero'].str.title())
#     return df_estandar
# =====================================================================


# --- PARTICIPACIÓN: JONATHAN (ETAPA 2) ---
def etapa_jonathan_validacion_final(df_original, df_limpio):
    """Compara las dimensiones del dataset antes y después de la limpieza.
    
    Responsable: Jonathan
    """
    print("\n--- VALIDACIÓN FINAL ETL (Jonathan) ---")
    print(f"Registros originales: {len(df_original)}")
    print(f"Registros limpios: {len(df_limpio)}")
    print(f"Diferencia de registros (Duplicados/Nulos eliminados): {len(df_original) - len(df_limpio)}")
    
    columnas_esperadas = len(df_original.columns)
    columnas_finales = len(df_limpio.columns)
    print(f"Columnas originales: {columnas_esperadas} | Columnas finales: {columnas_finales}")
    
    if len(df_limpio) > 0 and columnas_finales == columnas_esperadas:
        print("✅ Validación exitosa: El dataset está íntegro y listo para el Star Schema.")
    else:
        print("⚠️ Advertencia: Revisar la limpieza, posible pérdida crítica de datos.")


# ==========================================
# BLOQUE PRINCIPAL DE EJECUCIÓN (MAIN)
# ==========================================
if __name__ == "__main__":
    # Configuración de la ruta automática
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    NOMBRE_CSV = "Encuesta_snacks_mundial_2026_guatemala_2500_respuestas.csv"
    RUTA_DATASET_ORIGINAL = os.path.join(directorio_actual, "..", "2_Datos_Originales", NOMBRE_CSV)

    # 1. EJECUCIÓN - ETAPA 1 (Calidad de Datos)
    df_original = etapa_eu_calidad_datos(RUTA_DATASET_ORIGINAL)

    if df_original is not None:
        # Reporte inicial de Jonathan (Duplicados e Inconsistencias)
        etapa_jonathan_calidad_datos(df_original)
        
        # LLAMADA DE NICOLE ETAPA 1 (Descomentar cuando Nicole cree su función):
        # etapa_nicole_calidad_datos(df_original)

        # 2. EJECUCIÓN - ETAPA 2 (Limpieza ETL)
        # Paso 2.1: Eliminación de duplicados y espacios (Eu)
        df_limpio_eu = etapa_eu_limpieza(df_original)
        
        # PASO 2.2: LLAMADA DE NICOLE ETAPA 2 (Descomentar cuando Nicole cree su función):
        # df_limpio_final = etapa_nicole_estandarizacion_texto(df_limpio_eu)
        
        # Paso 2.3: Validación final a cargo de Jonathan
        # NOTA: Cambiar 'df_limpio_eu' por 'df_limpio_final' cuando Nicole integre su función.
        etapa_jonathan_validacion_final(df_original, df_limpio_eu)