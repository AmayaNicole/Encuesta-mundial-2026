import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def generar_graficos_marketing(fact_encuestas):
    print("--- GENERANDO GRÁFICOS DE MARKETING (Jonathan) ---")
    ruta_graficos = "1_Entregables/Graficos/"
    os.makedirs(ruta_graficos, exist_ok=True)
    sns.set_theme(style="whitegrid")

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