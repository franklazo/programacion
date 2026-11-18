# ----------------------------------------------------------------------
# 10. Separar y unir
# ----------------------------------------------------------------------
#
# Separa `"ana,luis,marta"` por comas, y vuelve a unirlo con guiones.
# ----------------------------------------------------------------------

datos = "ana,luis,marta"

lista = datos.split(",")
print(lista)              # ["ana", "luis", "marta"]

print("-".join(lista))    # ana-luis-marta
