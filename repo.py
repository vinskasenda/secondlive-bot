import requests

def check_in(token):
    try:
        API_URL = "https://app.secondlive.world/api/user/checkin-list?checkin_type=Centralized"
        response = requests.get(API_URL, headers={"Authorization": f"Bearer {token}"})
        return response.json()['data']
    except Exception as error:
        raise Exception(error)
