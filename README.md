# Proyecto Integrador - Ciencia de Datos (Fase 1)
**Tema:** Evaluar si existen diferencias salariales significativas entre hombres y mujeres que tienen empleo (2025).
**Grupo 8:** Bruna González, Karen Fisher, Marcos Gonzalez.

## Estructura del Repositorio
- `/data`: Contiene el dataset procesado y limpio (`dataset_limpio_fase1.csv`).
- `/docs`: Contiene la documentación de apoyo, incluyendo el diccionario oficial del INE (`diccionario_INGREFAM_EPHC_ANUAL_2025.pdf`).
- `/notebooks`: Contiene el Jupyter Notebook ejecutable (`.ipynb`) y la exportación oficial del informe ejecutable en formato **PDF**.
- `/output`: Gráficos y salidas generadas durante la exploración de datos.

## Nota Técnica sobre el Formato de Exportación (HTML vs. PDF)
De acuerdo con los entregables de la cátedra, se solicitaba inicialmente una exportación en formato `.html`. Sin embargo, debido a restricciones nativas recientes en la interfaz web de Google Colab que limitan la conversión directa a dicho formato, se optó metodológicamente por exportar el informe integrado de la Fase 1 en formato **PDF de alta fidelidad** generado directamente desde el entorno de ejecución. Esta decisión garantiza que la integridad visual, los estilos de diseño, la paleta de colores de los 8 gráficos del EDA, las tablas de la bitácora y la estructura de texto se mantengan intactas y legibles para su correcta evaluación.

## Instrucciones para la Reproducibilidad
1. Clonar el repositorio.
2. Instalar las dependencias ejecutando: `pip install -r requirements.txt`
3. Abrir el archivo ubicado en `/notebooks/Fase1_DataScience_Grupo8.ipynb` en Google Colab o Jupyter Lab.
4. Asegurarse de ubicar el archivo de microdatos original del INE (`REG02_EPHC_ANUAL_2025.csv`) en la ruta de trabajo si se desea ejecutar el flujo completo de limpieza y los gráficos desde cero.

## Nota sobre el dataset utilizado
Dadas las indicaciones del trabajo, el dataset utilizado pasa a encontrarse como link en el archivo 'data.txt' debido a que supera los 25Mb. Para reproducir el trabajo se debe ingresar al link y descargar manualmente los datos.