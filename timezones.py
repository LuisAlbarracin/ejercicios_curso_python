from datetime import datetime
import pytz

bogota_timezone = pytz.timezone("America/Bogota")
bogota_date = datetime.now(bogota_timezone)
print("Bogotá: ", bogota_date.strftime('%d/%m/%Y, %H:%M:%S'))

berlin_timezone = pytz.timezone("Europe/Berlin")
berlin_date = datetime.now(berlin_timezone)
print("Berlin: ", berlin_date.strftime('%d/%m/%Y, %H:%M:%S'))

japan_timezone = pytz.timezone("Japan")
japan_date = datetime.now(japan_timezone)
print("Japon: ", japan_date.strftime('%d/%m/%Y, %H:%M:%S'))
