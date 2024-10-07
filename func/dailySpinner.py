import requests
from func.CheckValidToken import validate_token

def daily_spinner():
    try:
        tokens = validate_token()
        for token in tokens:
            spin = requests.post(
                "https://app.secondlive.world/api/lottery-turntable/use",
                headers={"Authorization": f"Bearer {token['token']}"}
            )

            if spin.json()['code'] == 100002:
                print(f"[ Completed ] : No daily spins left. {spin.json()['data']}")
                return
            print(f"[ Running ] : Daily Spinner Successfully. Rewards: {spin.json()['data']['prize_amount']}")
    except Exception as error:
        print(error)
