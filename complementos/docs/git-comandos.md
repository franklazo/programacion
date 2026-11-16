# Comandos

```shell
# STAGING AREA:
# Ver estado
git status
# Agregar archivos
git add .
# Quitar archivos sin commit
git rm -r --cached .
git rm --cached archivo.ext
# Quitar archivos con commit
git restore --staged .
```

```shell
# COMMITS:
# Mostrar commits
git log
# Ejecutar commit
git commit -m "Descripción breve de los cambios"
# Editar commit (No recomendado si ya está en remoto)
git commit --amend -m "Descripción corregida del commit"
# Forzar cambios del commit en remoto
git push origin main --force-with-lease
```

```shell
# BORRAR COMMIT:
# Conservar cambios y Staging Area
git reset --soft HEAD~1
# Conservar cambios
git reset --mixed HEAD~1
# Borrar todo
git reset --hard HEAD~1
```

```shell
# REPOSITORIOS REMOTOS:
# Descargar
git clone url
# Mostrar url
git remote -v
# Cambiar url
git remote set-url origin url
```

```shell
# VERSIONES ESTABLES:
# Mostrar etiquetas
git tag
# Detalles de etiqueta
git show v1.0.0
# Etiquetar commit
git tag -a v1.0.0 -m "Descripción breve de la actualización"
# Subir a repositorio remoto
git push origin --tags
```
