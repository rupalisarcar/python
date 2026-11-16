import requests
from datetime import date

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

TOKEN = "create_user_pixel"
USERNAME = "rupali-7"
grpah_ID = "graph-1"

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}
# response = requests.post(url= PIXELA_ENDPOINT, json=user_params)

headers = {
    "X-USER-TOKEN" : TOKEN
}

graph_params = {
    "id" : grpah_ID,
    "name" : "Reading",
    "unit" : "commit",
    "type" : "int",
    "color" : "ajisai"
}
graph_url = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
# graph_create = requests.post(url=graph_url, json=graph_params, headers=headers)

graph_data_entry_url = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{grpah_ID}"
print(graph_data_entry_url)
now = date.today().strftime("%Y%m%d")
print(now)
data_params = {
    "date" : "20261107",
    "quantity" : "4"
} 

# data_response = requests.post(url=graph_data_entry_url, json=data_params, headers=headers)
# print(data_response)

# UPDATE_PIXEL_url =f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{grpah_ID}/20261109"
# update_data={
#     "quantity":"12"
# }

DELETE_PIXEL_URL = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{grpah_ID}/20261107"
delete_response = requests.delete(url=DELETE_PIXEL_URL, headers=headers)

print(delete_response)
print(delete_response.text)