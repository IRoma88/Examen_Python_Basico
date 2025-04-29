# 🏎️ Proyecto Final 2 - Introducción a Python: Ranking Fórmula 1

Este proyecto consiste en crear un sistema de clasificación contrarreloj para pilotos de Fórmula 1 utilizando diccionarios, listas y funciones en Python.

## 📚 Descripción

El objetivo es construir un programa que:
- Almacene los tiempos de 3 vueltas de distintos pilotos.
- Permita agregar nuevos pilotos con sus tiempos.
- Genere un ranking de pilotos basado en su mejor tiempo individual (el más rápido de sus 3 vueltas).

## 🛠️ Funcionalidades

- **Diccionario `piloto_tiempos`**  
  Guarda los nombres de los pilotos como clave y una lista de sus tiempos como valor.

- **Función `agregar_piloto(diccionario, nombre, tiempos)`**  
  Añade un nuevo piloto y su lista de tiempos al diccionario.

- **Función `ranking(diccionario)`**  
  Retorna una tupla:
  - Lista de pilotos ordenados del más rápido al más lento (por su mejor vuelta).
  - Lista de sus mejores tiempos.

- **Funciones de verificación**
  Cada etapa incluye funciones `check()` que permiten validar automáticamente que los datos y funciones están correctamente implementados.

## 📋 Requisitos

- Python 3.x

No se necesitan librerías adicionales.

## ▶️ ¿Cómo ejecutarlo?

1. Asegúrate de tener Python 3 instalado.
2. Copia el código en tu editor o ejecuta el notebook si trabajas en Google Colab o Jupyter.
3. Ejecuta las celdas o el script para construir el diccionario, agregar pilotos y generar el ranking.
4. Usa las funciones `check()` para verificar que todo esté correcto.

## 💻 Ejemplo de Uso

```python
# Crear el diccionario
piloto_tiempos = {
    'F. Alonso': [30.863, 30.595, 30.249],
    'C. Sainz Jr.': [31.653, 30.009, 30.215],
    'M. Verstappen': [30.499, 30.318, 28.997]
}

# Agregar pilotos
agregar_piloto(piloto_tiempos, 'L. Hamilton', [30.617, 30.085, 29.385])
agregar_piloto(piloto_tiempos, 'V. Bottas', [31.200, 30.186, 29.586])

# Generar ranking
pilotos_ordenados, mejores_tiempos = ranking(piloto_tiempos)
print(pilotos_ordenados)
print(mejores_tiempos)
````

## 🏁 Resultado Esperado
Lista de pilotos ordenados por su mejor tiempo, de menor a mayor.

Lista de los mejores tiempos de cada piloto.

## 📄 Licencia
Este proyecto es solo para fines educativos y de práctica personal.
