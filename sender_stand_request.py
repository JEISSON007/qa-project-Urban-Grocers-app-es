import configuration
import requests
import data


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=body, headers=data.headers)


response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())


def get_new_user_token():
    response_json = response.json()
    return response_json["authToken"]


def post_new_client_kit(kit_body):
    auth_token = get_new_user_token()
    authorization = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer "{auth_token}"'
    }
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                         json=kit_body,
                         headers=authorization
                         )
