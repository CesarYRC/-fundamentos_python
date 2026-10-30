linea = "       2026-10-12|ERROR|payment_gateway|Timeout en la respuesta    "

print(linea)
# strip: elimina espacios
linea_limpia = linea.strip()
print(linea_limpia)

# split: separa
campos = linea_limpia.split("|")

print(campos)

print(campos[1]) # Resultado : "ERROR"
print(len(campos)) # Resultado: 4