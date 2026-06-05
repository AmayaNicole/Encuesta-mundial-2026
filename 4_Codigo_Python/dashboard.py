import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Configuración estética general para los gráficos
sns.set_theme(style="whitegrid")

# ==========================================
# ETAPA 6 - MÉTRICAS Y VISUALIZACIONES
# ==========================================


# --- RESPONSABLE: EU (MÉTRICAS DEMOGRÁFICAS) ---
def generar_graficos_demograficas(df_datos):
    """Calcula el total de encuestas y exporta los gráficos demográficos requeridos.

    Responsable: Eu
    """
    print("--- GENERANDO GRÁFICOS DEMOGRÁFICOS (Eu) ---")
    ruta_graficos = "1_Entregables/Graficos/"
    os.makedirs(ruta_graficos, exist_ok=True)

    # 1. Indicador: Total de encuestas
    total_encuestas = len(df_datos)
    print(f"📊 KPI - Total de Encuestas Procesadas: {total_encuestas}")

    # 2. grafico_genero.png - Gráfico de Pastel
    plt.figure(figsize=(8, 8))
    df_datos["Genero"].value_counts().plot(
        kind="pie", autopct="%1.1f%%", startangle=90, colors=sns.color_palette("pastel")
    )
    plt.title("Distribución de Participantes por Género", fontsize=14)
    plt.ylabel("")  
    plt.savefig(os.path.join(ruta_graficos, "grafico_genero.png"), bbox_inches='tight')
    plt.close()
    print("✅ grafico_genero.png generado con éxito.")

    # 3. grafico_edad.png - Gráfico de Barras Verticales
    plt.figure(figsize=(10, 6))
    order_edad = sorted(df_datos["RangoEdad"].dropna().unique())
    sns.countplot(data=df_datos, x="RangoEdad", order=order_edad, palette="Set2")
    plt.title("Distribución de Participantes por Rango de Edad", fontsize=14)
    plt.xlabel("Rango de Edad")
    plt.ylabel("Cantidad de Encuestados")
    plt.savefig(os.path.join(ruta_graficos, "grafico_edad.png"), bbox_inches='tight')
    plt.close()
    print("✅ grafico_edad.png generado con éxito.")

    # 4. grafico_departamentos.png - Barras Horizontales
    plt.figure(figsize=(12, 7))
    dept_counts = df_datos["Departamento"].value_counts()
    sns.barplot(x=dept_counts.values, y=dept_counts.index, palette="Viridis")
    plt.title("Participación de Encuestados por Departamento", fontsize=14)
    plt.xlabel("Cantidad de Encuestados")
    plt.ylabel("Departamento")
    plt.savefig(os.path.join(ruta_graficos, "grafico_departamentos.png"), bbox_inches='tight')
    plt.close()
    print("✅ grafico_departamentos.png generado con éxito.")

    # 5. grafico_municipios.png - Top 10 Municipios
    plt.figure(figsize=(12, 7))
    top_municipios = df_datos["Municipio"].value_counts().head(10)
    sns.barplot(x=top_municipios.values, y=top_municipios.index, palette="magma")
    plt.title("Top 10 Municipios con Mayor Cantidad de Encuestados", fontsize=14)
    plt.xlabel("Cantidad de Encuestados")
    plt.ylabel("Municipio")
    plt.savefig(os.path.join(ruta_graficos, "grafico_municipios.png"), bbox_inches='tight')
    plt.close()
    print("✅ grafico_municipios.png generado con éxito.")

    return total_encuestas


# --- RESPONSABLE: JONATHAN (MÉTRICAS DE MARKETING) ---
def generar_graficos_marketing(fact_encuestas):
    """Genera las visualizaciones orientadas al presupuesto y preferencias de marketing.

    Responsable: Jonathan
    """
    print("--- GENERANDO GRÁFICOS DE MARKETING (Jonathan) ---")
    ruta_graficos = "1_Entregables/Graficos/"
    os.makedirs(ruta_graficos, exist_ok=True)

    # 1. grafico_precio.png (Distribución del Precio Aceptado / Presupuesto)
    plt.figure(figsize=(10, 6))
    sns.histplot(data=fact_encuestas, x='Precio_Aceptado', bins=15, kde=True, color='skyblue')
    plt.title('Distribución del Precio Ideal para Snacks Temáticos', fontsize=14)
    plt.xlabel('Precio Aceptado (Q)')
    plt.ylabel('Frecuencia')
    plt.savefig(f"{ruta_graficos}grafico_precio.png", bbox_inches='tight')
    plt.close()

    # 2. grafico_selecciones.png (Top Selecciones Favoritas)
    plt.figure(figsize=(10, 6))
    sns.countplot(data=fact_encuestas, y='Seleccion', order=fact_encuestas['Seleccion'].value_counts().index[:10], palette='viridis')
    plt.title('Top 10 Selecciones Favoritas para el Mundial 2026', fontsize=14)
    plt.xlabel('Cantidad de Respuestas')
    plt.ylabel('Selección')
    plt.savefig(f"{ruta_graficos}grafico_selecciones.png", bbox_inches='tight')
    plt.close()

    # 3. grafico_jugadores.png (Top Jugadores)
    plt.figure(figsize=(10, 6))
    sns.countplot(data=fact_encuestas, y='Jugador', order=fact_encuestas['Jugador'].value_counts().index[:10], palette='magma')
    plt.title('Top 10 Jugadores que Motivan la Compra', fontsize=14)
    plt.xlabel('Cantidad de Respuestas')
    plt.ylabel('Jugador')
    plt.savefig(f"{ruta_graficos}grafico_jugadores.png", bbox_inches='tight')
    plt.close()

    # 4. grafico_promociones.png (Promociones Favoritas)
    plt.figure(figsize=(10, 6))
    fact_encuestas['Tipo_Promocion'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, cmap='Set3')
    plt.title('Distribución de Promociones Preferidas', fontsize=14)
    plt.ylabel('')
    plt.savefig(f"{ruta_graficos}grafico_promociones.png", bbox_inches='tight')
    plt.close()

    # 5. grafico_publicidad.png (Publicidad Favorita)
    plt.figure(figsize=(10, 6))
    sns.countplot(data=fact_encuestas, x='Publicidad_Favorita', order=fact_encuestas['Publicidad_Favorita'].value_counts().index, palette='crest')
    plt.title('Canales de Publicidad Más Atractivos', fontsize=14)
    plt.xlabel('Tipo de Publicidad')
    plt.ylabel('Cantidad de Respuestas')
    plt.xticks(rotation=45)
    plt.savefig(f"{ruta_graficos}grafico_publicidad.png", bbox_inches='tight')
    plt.close()
    
    print("✅ Gráficos de Marketing exportados con éxito.")


# =====================================================================
# ESPACIO RESERVADO PARA: NICOLE (MÉTRICAS DE CONSUMO)
# =====================================================================
# NICOLE: Aquí debes crear tu función para procesar las métricas de consumo
# y exportar los siguientes gráficos:
# - grafico_frecuencia_consumo.png
# - grafico_lugar_compra.png
# - grafico_snacks.png
# - grafico_sabores.png
# - grafico_presentacion.png
# =====================================================================
# --- RESPONSABLE: NICOLE ---
def generar_graficos_consumo(df_datos):
    
    print("\n--- GENERANDO GRÁFICOS DE CONSUMO (Nicole) ---")
    ruta_graficos = "1_Entregables/Graficos/"
    os.makedirs(ruta_graficos, exist_ok=True)

    # 1. grafico_frecuencia_consumo.png - Gráfico de Barras Verticales
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df_datos, x="FrecuenciaConsumo", palette="Set3", order=df_datos["FrecuenciaConsumo"].value_counts().index)
    plt.title("Frecuencia de Consumo de Snacks durante los Partidos", fontsize=14)
    plt.xlabel("Frecuencia de Consumo")
    plt.ylabel("Cantidad de Respuestas")
    plt.xticks(rotation=15)
    plt.savefig(os.path.join(ruta_graficos, "grafico_frecuencia_consumo.png"), bbox_inches='tight')
    plt.close()
    print("✅ grafico_frecuencia_consumo.png generado.")

    # 2. grafico_lugar_compra.png - Gráfico de Barras Horizontales
    plt.figure(figsize=(10, 6))
    lugar_counts = df_datos["LugarCompra"].value_counts()
    sns.barplot(x=lugar_counts.values, y=lugar_counts.index, palette="coolwarm")
    plt.title("Lugares Preferidos para Comprar Snacks", fontsize=14)
    plt.xlabel("Cantidad de Respuestas")
    plt.ylabel("Lugar de Compra")
    plt.savefig(os.path.join(ruta_graficos, "grafico_lugar_compra.png"), bbox_inches='tight')
    plt.close()
    print("✅ grafico_lugar_compra.png generado.")

    # 3. grafico_snacks.png - Top Snacks Favoritos
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df_datos, y="SnackFavorito", order=df_datos["SnackFavorito"].value_counts().index[:10], palette="cubehelix")
    plt.title("Top 10 Snacks Favoritos para el Mundial", fontsize=14)
    plt.xlabel("Cantidad de Respuestas")
    plt.ylabel("Tipo de Snack")
    plt.savefig(os.path.join(ruta_graficos, "grafico_snacks.png"), bbox_inches='tight')
    plt.close()
    print("✅ grafico_snacks.png generado.")

    # 4. grafico_sabores.png - Distribución de Sabores (Gráfico de Pastel)
    plt.figure(figsize=(8, 8))
    df_datos["SaborPreferido"].value_counts().plot(
        kind="pie", autopct="%1.1f%%", startangle=45, colors=sns.color_palette("Set2")
    )
    plt.title("Distribución de Sabores Preferidos", fontsize=14)
    plt.ylabel("")  
    plt.savefig(os.path.join(ruta_graficos, "grafico_sabores.png"), bbox_inches='tight')
    plt.close()
    print("✅ grafico_sabores.png generado.")

    # 5. grafico_presentacion.png - Presentación Ideal
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df_datos, x="PresentacionIdeal", palette="rocket", order=df_datos["PresentacionIdeal"].value_counts().index)
    plt.title("Preferencia de Presentación Ideal del Producto", fontsize=14)
    plt.xlabel("Tipo de Presentación")
    plt.ylabel("Cantidad de Respuestas")
    plt.savefig(os.path.join(ruta_graficos, "grafico_presentacion.png"), bbox_inches='tight')
    plt.close()
    print("✅ grafico_presentacion.png generado.")

# ==========================================
# BLOQUE PRINCIPAL DE EJECUCIÓN (MAIN)
# ==========================================
if __name__ == "__main__":
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    # Se utiliza el dataset limpio intermedio o la Fact Table según disponibilidad
    RUTA_DATASET = os.path.join(directorio_actual, "..", "3_Tablas_Limpias", "dataset_limpio.csv")

    if not os.path.exists(RUTA_DATASET):
        print(f"Error: No se encontró el dataset en: {RUTA_DATASET}")
    else:
        df_limpio = pd.read_csv(RUTA_DATASET)
        print(f"Dataset cargado correctamente. Registros a procesar: {len(df_limpio)}\n")

        # 1. Ejecución de tu sección (Eu)
        generar_graficos_demograficas(df_limpio)

        # 2. Ejecución de la sección de Jonathan
        generar_graficos_marketing(df_limpio)

        # 3. Ejecución de la sección de Nicole
        generar_graficos_consumo(df_limpio)