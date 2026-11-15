# ----------------------------------------------------------------------
# 05. Mensaje personalizado
# ----------------------------------------------------------------------
#
# Pide nombre, ciudad y hobby, y construye un párrafo corto
# que combine los tres datos con buen formato.
# ----------------------------------------------------------------------

print("\n=== Mensaje personalizado ===\n")

nombre = input("Tu nombre: ").strip().title()
ciudad = input("Tu ciudad: ").strip().title()
hobby = input("Tu hobby: ").strip().lower()

parrafo = (
    f"Hola, me llamo {nombre} y vivo en {ciudad}. "
    f"En mi tiempo libre disfruto mucho de {hobby}. "
    f"Si alguna vez pasas por {ciudad}, con gusto lo compartimos."
)

print(f"\n{parrafo}\n")
