import requests
from datetime import datetime

USERNAME = 'lalonunez'
TOKEN = 'ndj2b3hbsadjlklljj'
# Create account with post method
pixela_end_point ='https://pixe.la/v1/users'

actual_date = datetime.now()
formated_date = actual_date.strftime("%Y%m%d")


user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=pixela_end_point, json=user_params)

# Create a graph with POST method

graph_endpoint = f'{pixela_end_point}/{USERNAME}/graphs'

graph_config = {
    'id': 'grahp1',
    'name': 'Reading Graph',
    'unit': 'pages',
    'type': 'int',
    'color': 'ajisai',
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response)

pixel_post_end_point = f'{pixela_end_point}/{USERNAME}/graphs/grahp1'

pixel_config = {
    'date': formated_date,
    'quantity': '10'
}



# response = requests.post(url=pixel_post_end_point, json=pixel_config, headers=headers)
# print(response)


pixel_put_config = {
    'quantity': '5'
}

# pixel_put_end_point = f'{pixela_end_point}/{USERNAME}/graphs/grahp1/{formated_date}'
# response = requests.put(url=pixel_put_end_point, json=pixel_put_config, headers=headers)



pixel_delete_end_point = f'{pixela_end_point}/{USERNAME}/graphs/grahp1/{formated_date}'
response = requests.delete(url=pixel_delete_end_point, headers=headers)
print(response.text)


