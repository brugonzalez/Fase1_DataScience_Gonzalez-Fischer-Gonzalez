# Proyecto Integrador - Ciencia de Datos (Fase 1)
**Tema:** Evaluar si existen diferencias salariales significativas entre hombres y mujeres que tienen empleo (2025).
**Grupo 8:** Bruna González, Karen Fisher, Marcos Gonzalez.

## Estructura del Repositorio
- `/data`: Contiene el dataset procesado y limpio (`dataset_limpio_fase1.csv`).
- `/docs`: Contiene la documentación de apoyo, incluyendo el diccionario oficial del INE (`diccionario_INGREFAM_EPHC_ANUAL_2025.pdf`).
- `/notebooks`: Contiene el Jupyter Notebook limpio y sin salidas (`.ipynb`).
- `/output`: Contiene la versión final del proyecto **ya ejecutada** (`Fase1_DataScience_Gonzalez_Fischer_Gonzalez_Ejecutado.ipynb`) y su respectiva exportación visual en formato **`.html`**.
- `/src`: Contiene los scripts de Python utilizados para la automatización (como la descarga del dataset).

## Cómo reproducir el proyecto

Para ejecutar y evaluar este proyecto de forma rápida y sin errores de entorno, utilizaremos **Google Colab**. Solo sigue estos dos pasos:

**1. Abrir el cuaderno:**
* Ingresa a [Google Colab](https://colab.research.google.com/).
* Ve a **Archivo > Abrir cuaderno > Pestaña GitHub**.
* Pega el link del repositorio: `https://github.com/brugonzalez/Fase1_DataScience_Gonzalez-Fischer-Gonzalez`
* Haz clic en el archivo `Fase1_DataScience_Gonzalez_Fischer_Gonzalez_Ejecutado.ipynb`

*(Opcional: Si deseas probar y ejecutar el código paso a paso desde cero, haz clic en el archivo **`notebooks/Fase1_DataScience_Gonzalez_Fischer_Gonzalez_sinSalidas.ipynb`**, el cual se encuentra limpio y sin salidas iniciales).*

**2. Preparar el entorno y descargar datos:**
El dataset del INE es muy pesado para estar alojado directamente en GitHub. Para clonar el proyecto y descargar la base de datos automáticamente, **crea una celda de código al inicio del cuaderno, pega el siguiente bloque y ejecútalo**:

```python
!git clone https://github.com/brugonzalez/Fase1_DataScience_Gonzalez-Fischer-Gonzalez.git
%cd Fase1_DataScience_Gonzalez-Fischer-Gonzalez
!python src/descargas_datos.py
```

**3. Descargar el archivo HTML:**
* Una vez clonado y preparado el entorno, dirígete al panel de archivos de la izquierda, entra a la carpeta **`output/`** y podrás descargar el archivo en formato `.html`.


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
