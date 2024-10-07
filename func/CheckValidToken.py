import requests
from func.GetTokens import get_tokens
from dotenv import load_dotenv
from repo import check_in

load_dotenv()

def validate_token():
    tokens = get_tokens()
    valid_token = []
    
    for token in tokens:
        try:
            check_in(token['token'])
            valid_token.append(token)
        except Exception as error:
            print(f"[ Error ] : token not valid , response code : {error}")
    
    print(f"[ Token valid ] : {len(valid_token)}\n")
    return valid_token
