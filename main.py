import requests
import time
import json


def get_json(url):
    response = requests.get(URL)
    todos = json.loads(response.text)
    return todos


def info(json, cnt):
    info = {}
    for i in range(cnt):
        temp_night = json['daily'][i]['temp']['night']
        feels_like_night = json['daily'][i]['feels_like']['night']
        date = json['daily'][i]['dt']
        format_date = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(date))
        sunrise = json['daily'][i]['sunrise']
        sunset = json['daily'][i]['sunset']
        info[format_date] = {'Фактическая температура ночью': temp_night,
                             'Ощущаемая температура ночью': feels_like_night,
                             'Время восхода': sunrise,
                             'Время заката': sunset}
    return info


def min_difference_temp(info_dict):
    min_difference_temp = 0
    for key, value in info_dict.items():
        min_difference_temp = value['Фактическая температура ночью'] - value['Ощущаемая температура ночью']
        break
    for key, value in info_dict.items():
        difference = value['Фактическая температура ночью'] - value['Ощущаемая температура ночью']
        if abs(difference) < min_difference_temp:
            min_difference_temp = difference
    return min_difference_temp


def maximum_duration_of_the_day(info_dict):
    maximum_duration_of_the_day = 0
    for key, value in info_dict.items():
        maximum_duration_of_the_day = value['Время заката'] - value['Время восхода']
        break
    for key, value in info_dict.items():
        difference = value['Фактическая температура ночью'] - value['Ощущаемая температура ночью']
        if abs(difference) > maximum_duration_of_the_day:
            maximum_duration_of_the_day = difference
    return maximum_duration_of_the_day


def print_info(info):
    for key, value in info.items():
        print(f'{key}:{value}')


def convert_to_preferred_format(sec):
    sec = sec % (24 * 3600)
    hour = sec // 3600
    sec %= 3600
    min = sec // 60
    sec %= 60

    return "%02d:%02d:%02d" % (hour, min, sec)


city_name = 'Moscow'
API_key = 'd8c1f786ff64c7f128eb322102a2e4f9'
CNT = 5
lat = 55.752972
lon = 37.623107
URL = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}' \
      f'&exclude=current,hourly,alerts,minutely&appid={API_key}&units=metric'
json_text = get_json(URL)
info = info(json_text, CNT)
print_info(info)
min_difference_tem = min_difference_temp(info)
maximum_duration_of_the_day = convert_to_preferred_format(maximum_duration_of_the_day(info))
print(f'Минимальная разница фактической и ощущаемой температуры за 5 дней: {min_difference_tem} градусов Цельсия')
print(f'Максимальная продолжительность светового дня за 5 дней: {maximum_duration_of_the_day}')









