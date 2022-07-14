#%%
import datetime


def vida_en_segundos(fecha_nacimiento: str) -> float:
    """
    La función debe toma como entrada una cadena en formato 'dd/mm/AAAA' 
    (día, mes, año con 2, 2 y 4 dígitos, separados con barras normales) 
    y devuelve un float.
    """
    fecha_nacimiento_datetime = datetime.datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
    timedelta = datetime.datetime.now() - fecha_nacimiento_datetime

    return float(timedelta.seconds)


# %%
