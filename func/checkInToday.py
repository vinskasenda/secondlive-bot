import requests
from func.CheckValidToken import validate_token
from repo import check_in

def check_in_today():
    try:
        tokens = validate_token()
        for token in tokens:
            now = check_in(token['token'])
            if len(now) < 1:
                return None
            is_today = next((item for item in now if item['is_today']), None)
            
            if not is_today['is_checkin']:
                response = requests.post(
                    "https://app.secondlive.world/api/user/checkin",
                    headers={"Authorization": f"Bearer {token['token']}"}
                )
                print(is_today)
                print(f"[ Running ] : Checkin Successfully.")
            else:
                print(f"[ Completed ] : days: {is_today['days']} has been checkin")
    except Exception as error:
        print(f"[ Error ] : {error}")
