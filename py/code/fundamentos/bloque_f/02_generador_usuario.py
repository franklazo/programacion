# ----------------------------------------------------------------------
# 02. Generador de usuario
# ----------------------------------------------------------------------
#
# Dado nombre y apellido,
# genera un usuario tipo `inicial + apellido` en minúsculas
# y un correo `usuario@dominio.com`.
# ----------------------------------------------------------------------

print("\n=== Generador de usuario ===\n")

nombre = input("Nombre: ").strip()
apellido = input("Apellido: ").strip()

usuario = (nombre[0] + apellido).lower()
correo = f"{usuario}@dominio.com"

print(f"\nUsuario: {usuario}")
print(f"Correo:  {correo}\n")
