import requests

APP_ID = 'e6feeefa'
APP_KEY = 'fc90f7d30875aed1aac4c894c1d2aa34'
natural_workout_endpoint = f'https://trackapi.nutritionix.com/v2/natural/exercise'
from datetime import datetime

actual_date = datetime.now()
formated_date = actual_date.strftime("%Y/%m/%d")
time = actual_date.strftime("%H:%M:%S")

header = {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY,
    'x-remote-user-id': '0'
}

query = input('What excercise you have done?: ')
post_request_body = {
    "query": query,
    "gender": "male",
    "weight_kg": 52.5,
    "height_cm": 183.64,
    "age": 20
}

response = requests.post(url=natural_workout_endpoint, json=post_request_body, headers=header)
response.raise_for_status()
print(response)
data = response.json()
# print(data)
duration = data['exercises'][0]['duration_min']
calories = data['exercises'][0]['nf_calories']
excercise = data['exercises'][0]['name']
# print(duration)
# print(calories)
# print(excercise)



put_end_point_spread_sheets = 'https://api.sheety.co/3d8ebdedf54e4ec3992f394fd1a028da/workOutTrack/workouts'


data_to_insert = {
    'workout': {
        'date': formated_date,
        'time': time,
        'exercise': excercise,
        'duration': duration,
        'calories': calories
    }
}


response = requests.post(url=put_end_point_spread_sheets, json=data_to_insert)
response.raise_for_status()
# print(response.text)
