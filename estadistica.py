import pandas as pd

# Datos de ejemplo
data = {
    "producto": [
        "Café", "Té", "Galletas", "Azúcar", "Yerba", "Leche", "Miel",
        "Pan", "Harina", "Aceite", "Sal", "Fideos", "Mermelada", "Jugo", "Cacao"
    ],
    "cantidad": [
        120, 80, 150, 200, 130, 90, 60, 220, 170, 210, 65, 35, 120, 30, 90
    ],
    "precio": [
        1800, 1200, 950, 850, 2500, 1100, 3000, 300, 750, 890, 220, 60, 90, 130, 1700
    ]
}

# Crear el DataFrame
df_ejemplo = pd.DataFrame(data)

# Exportar a Excel
ruta_excel = "ventas.xlsx"
df_ejemplo.to_excel(ruta_excel, index=False)

print("✅ Archivo 'ventas.xlsx' generado correctamente.")
