# Proyecto Integrador - Ciencia de Datos (Fase 1)
**Tema:** Evaluar si existen diferencias salariales significativas entre hombres y mujeres que tienen empleo (2025).
**Grupo 8:** Bruna González, Karen Fisher, Marcos Gonzalez.

## Estructura del Repositorio
- `/data`: Contiene el dataset procesado y limpio (`dataset_limpio_fase1.csv`).
- `/docs`: Contiene la documentación de apoyo, incluyendo el diccionario oficial del INE (`diccionario_INGREFAM_EPHC_ANUAL_2025.pdf`).
- `/notebooks`: Contiene el Jupyter Notebook ejecutable (`.ipynb`) y la exportación oficial del informe ejecutable en formato **PDF**.
- `/output`: Gráficos y salidas generadas durante la exploración de datos.

## Cómo reproducir el proyecto
1. Cloná el repositorio.
2. Creá y activá un entorno virtual según tu sistema operativo.
3. Instalá las dependencias del proyecto.
4. Abrí el notebook con Jupyter o Google Colab.

### Para clonar el repositorio en Google Colab
```python
!git clone https://github.com/brugonzalez/Fase1_DataScience_Gonzalez-Fischer-Gonzalez.git
%cd Fase1_DataScience_Gonzalez-Fischer-Gonzalez
```

### Linux y macOS
```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

### Windows
En PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
```

## Descargar los datos
El dataset es pesado, así que no se sube al repositorio. Para bajarlo desde la raíz del proyecto, ejecutá:

```bash
python3 src/descargas_datos.py
```

Esto crea la carpeta `data` si hace falta y descarga el archivo localmente. Si ya existe, no lo vuelve a bajar.

## Nota sobre el dataset
Como el archivo supera el límite de peso del repositorio, se comparte por link externo. Para reproducir el trabajo completo, el script lo descarga automáticamente cuando se ejecuta, así el proyecto final no queda pesado.
