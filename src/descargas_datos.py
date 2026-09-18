import os
import urllib.request  # descarga el archivo pesado desde Google Drive
import pandas as pd


def download_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, "data")
    output_path = os.path.join(data_dir, "REG02_EPHC_ANUAL_2025.csv")

    os.makedirs(data_dir, exist_ok=True)
    if os.path.exists(output_path):
        print("El archivo ya existe en la carpeta local.")
        return

    url = "https://drive.google.com/uc?export=download&id=1-9gmdJCzRojDEQ2ATKJpvDbnTHj9jjZ7"
    print("Descargando datos...")
    urllib.request.urlretrieve(url, output_path)
    print("Descarga completada.")

    df = pd.read_csv(output_path, sep=";", encoding="latin-1")
    print(f"Archivo cargado correctamente. Filas: {len(df)}")
    return df


if __name__ == "__main__":
    download_data()

