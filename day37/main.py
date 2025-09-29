import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

TOKEN = os.getenv("TOKEN")
USERNAME = os.getenv("USERNAME")

pixela_endpoint = "https://pixe.la/v1/users"

user_param = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

### This POST request was just to create a user, it cannot be executed again.
# response = requests.post(url=pixela_endpoint, json=user_param)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "test1",
    "name": "Warhammer3",
    "unit": "hr",
    "type": "float",
    "color": "ajisai",
}

headers = {"X-USER-TOKEN": TOKEN}

### Creates graph, already been done, cannot create duplicate graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now()
formatted_date = today.strftime("%Y%m%d")

post_to_graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/test1"

post_to_graph_config = {"date": formatted_date, "quantity": "1"}


### POST a new tick to the tracker
# response = requests.post(
#     url=post_to_graph_endpoint, json=post_to_graph_config, headers=headers
# )
# print(response.text)

### Browse pixela tracker graph here 'https://pixe.la/v1/users/paul1/graphs/test1.html'

delete_graph_endpoint = f"https://pixe.la//v1/users/{USERNAME}/graphs/test1"

### Delete graph
# response = requests.delete(url=delete_graph_endpoint, headers=headers)
# print(response.text)
