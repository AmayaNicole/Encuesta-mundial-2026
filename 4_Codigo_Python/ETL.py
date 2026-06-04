import pandas as pd

def etapa_jonathan_calidad_datos(df):
    print("--- REPORTE DE DUPLICADOS E INCONSISTENCIAS (Jonathan) ---")
    # 1. Buscar registros duplicados
    duplicados = df.duplicated().sum()
    print(f"Total de registros duplicados exactos: {duplicados}")
    
    # 2. Detectar categorías repetidas / inconsistencias
    # Ejemplo con columnas categóricas (ajustar nombres según el CSV real)
    columnas_categoricas = ['Genero', 'Departamento', 'Frecuencia_Consumo']
    for col in columnas_categoricas:
        if col in df.columns:
            print(f"\nInconsistencias en la columna '{col}':")
            print(df[col].value_counts(dropna=False))

def etapa_jonathan_validacion_final(df_original, df_limpio):
    print("\n--- VALIDACIÓN FINAL ETL (Jonathan) ---")
    # Comparar datos antes y después
    print(f"Registros originales: {len(df_original)}")
    print(f"Registros limpios: {len(df_limpio)}")
    print(f"Diferencia de registros (Duplicados/Nulos eliminados): {len(df_original) - len(df_limpio)}")
    
    # Verificar que no se perdieron columnas importantes
    columnas_esperadas = len(df_original.columns)
    columnas_finales = len(df_limpio.columns)
    print(f"Columnas originales: {columnas_esperadas} | Columnas finales: {columnas_finales}")
    
    if len(df_limpio) > 0 and columnas_finales == columnas_esperadas:
        print("✅ Validación exitosa: El dataset está íntegro y listo para el Star Schema.")
    else:
        print("⚠️ Advertencia: Revisar la limpieza, posible pérdida crítica de datos.")