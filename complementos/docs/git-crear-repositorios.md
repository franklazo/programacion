# Crear repositorios

```shell
# Crear repositorio local .git
git init
# Agregar archivos al Staging Area
git add .
# Agregar archivos al repositorio local
git commit -m "Primer commit"
```

```shell
# Crear repositorio en GitHub:
# No `README`, no `.gitignore` y no `license`
git remote add origin https://github.com/usuario/ejemplo.git
# Renombrar rama principal
git branch -M main
# Subir commit al repositorio remoto
git push -u origin main
```

```shell
# Después del primer commit
git add .
git commit -m "Descripción breve de los cambios"
git push
```
