import pandas as pd
import os

# Obtener la ruta absoluta del directorio padre (Mi parque)
RUTA_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUTA_DATOS = os.path.join(RUTA_BASE, 'data')
RUTA_EXCEL = os.path.join(RUTA_DATOS, 'Inventario_de_parques_urbanos_20251125.csv')

# Crear la carpeta data si no existe
os.makedirs(RUTA_DATOS, exist_ok=True)


  
#   CARGAR EXCEL
  
def leer_parques():
    """
    Lee el archivo CSV. Si no existe, crea uno con columnas base.
    """
    if not os.path.exists(RUTA_EXCEL):
        columnas = [
            "ID", "Nombre", "Localidad", "Direccion",
            "Tamano_m2", "Tipo", "Estado",
            "Canchas", "Juegos", "Ultimo_mantenimiento"
        ]
        df = pd.DataFrame(columns=columnas)
        df.to_csv(RUTA_EXCEL, index=False)
        return df

    return pd.read_csv(RUTA_EXCEL)


  
#   GUARDAR EXCEL
  
def guardar_parques(df):
    """Guarda el DataFrame nuevamente en el CSV."""
    df.to_csv(RUTA_EXCEL, index=False)


  
#   AGREGAR PARQUE
  
def agregar_parque(datos):
    """
    Agrega un parque al Excel.
    datos: dict con los campos del formulario.
    """
    df = leer_parques()

    # ID autoincremental
    nuevo_id = 1 if df.empty else df["ID"].max() + 1
    datos["ID"] = nuevo_id

    df = df.append(datos, ignore_index=True)
    guardar_parques(df)


  
#   OBTENER PARQUE POR ID
  
def obtener_parque_por_id(id_parque):
    df = leer_parques()
    parque = df[df["ID"] == id_parque]

    if parque.empty:
        return None

    # Convertir a diccionario para usar en HTML
    return parque.to_dict(orient="records")[0]


  
#   EDITAR PARQUE
  
def editar_parque(id_parque, datos_nuevos):
    df = leer_parques()

    index = df.index[df["ID"] == id_parque]
    if len(index) == 0:
        return False

    # Actualizar solo ese registro
    for key, value in datos_nuevos.items():
        df.at[index[0], key] = value

    guardar_parques(df)
    return True


  
#   ELIMINAR PARQUE
  
def eliminar_parque(id_parque):
    df = leer_parques()

    df = df[df["ID"] != id_parque]  # Eliminar registro

    guardar_parques(df)
