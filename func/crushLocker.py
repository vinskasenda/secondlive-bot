import requests
from func.CheckValidToken import validate_token

def crush_locker():
    try:
        tokens = validate_token()
        for token in tokens:
            info = requests.get(
                "https://app.secondlive.world/api/user/figure/info",
                headers={"Authorization": f"Bearer {token['token']}"}
            )

            if info.json()['data'] is None:
                return None

            intimacy_balance = float(info.json()['data']['intimacy_balance'])
            next_storage_consume_amount = float(info.json()['data']['level_info']['next_storage_consume_amount'])

            if intimacy_balance < next_storage_consume_amount:
                print(f"[ BOT ] : Insufficient CRUSH Balance. Current Balance : {intimacy_balance} CRUSH")
                return
            
            upgrade = requests.post(
                "https://app.secondlive.world/api/user/figure/upgrade",
                json={"upgrade_type": "storage"},
                headers={"Authorization": f"Bearer {token['token']}"}
            )
            print(f"[ Running ] : Upgrade Crush Locker Lv {upgrade.json()['data']['after_level']} Successfully.")
    except Exception as error:
        print(error)
