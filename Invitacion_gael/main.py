import base64

# Rutas de la imagen principal y de fondo
ruta_imagen = "C:\\Invitacion_gael\\Imagenes\\chase.png"
ruta_pie="C:\Invitacion_gael\Imagenes\pies.jpg"
ruta_fondo = "C:\\Invitacion_gael\\Imagenes\\paw.png"
ruta_html = "C:\\Invitacion_gael\\invitacion_Fiesta_de_Gael.html"

# Codificar imagen principal
with open(ruta_imagen, "rb") as img:
    imagen_base64 = base64.b64encode(img.read()).decode("utf-8")

# Codificar imagen de pie
with open(ruta_pie, "rb") as pie:
    pie_base64 = base64.b64encode(pie.read()).decode("utf-8")
    
# Codificar imagen de fondo
with open(ruta_fondo, "rb") as fondo:
    background_base64 = base64.b64encode(fondo.read()).decode("utf-8")

# Leer HTML base
with open(ruta_html, "r", encoding="utf-8") as archivo:
    html_base = archivo.read()

# Reemplazar los marcadores en el HTML
html_final = (
    html_base
    .replace("{imagen_base64}", imagen_base64)
    .replace(f"{pie_base64}",pie_base64)
    .replace("{background_base64}", background_base64)
)

# Sobrescribir el mismo archivo
with open(ruta_html, "w", encoding="utf-8") as archivo:
    archivo.write(html_final)

print("✅ Archivo actualizado correctamente:", ruta_html)
