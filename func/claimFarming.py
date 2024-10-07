import requests
from func.CheckValidToken import validate_token

def claim_farming():
    try:
        tokens = validate_token()
        for token in tokens:
            response = requests.post(
                "https://app.secondlive.world/api/user/figure/claim",
                json={"is_claim_double": False},
                headers={"Authorization": f"Bearer {token['token']}"}
            )

            if response.json()['code'] == 100002:
                print(f"[ Completed ] : No claim left. {response.json()['data']}")
                return
            print(f"[ Running ] : Claim farming successfully. Rewards: {response.json()['data']['claim_intimacy']} CRUSH")
    except Exception as error:
        print(error)
