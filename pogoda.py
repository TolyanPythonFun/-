from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config
from cfg import api_key

# ---------- FREE API KEY examples ---------------------
config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = OWM(api_key, config_dict)
mgr = owm.weather_manager()

place = input("Введите город: ")
# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place(place)
w = observation.weather

temp = w.temperature('celsius')["temp"]

# w.detailed_status         # 'clouds'
# w.wind()                  # {'speed': 4.6, 'deg': 330}
# w.humidity                # 87
# w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
# w.rain                    # {}
# w.heat_index              # None
# w.clouds                  # 75


print(w)
print("В городе " + place + " сейчас " + w.detailed_status)
print("Температура " + str(temp) + " градуса")
# print("Влажность воздуха - " + w.humidity + " %")
# if temp >= 20:
# 	 print("Сегодня достаточно тепло, много одежды не надевайте")
# if temp <= 20:
# 	 print("Сегодня может быть прохладно, возьмите с собой тепыле вещи")


