import json
import os
from dotenv import load_dotenv

load_dotenv()

def get_tokens():
    try:
        with open("configs/config.json", "r", encoding="utf-8") as file:
            tokens = json.load(file)
            for index, item in enumerate(tokens):
                print(f"\n[ Token {index + 1} ] : {item['token']}")
            print(f"[ Total tokens ] : {len(tokens)}")
        return tokens
    except Exception as error:
        print(f"[ Error ] : Token not found, please add token on configs/config.json")
        return None
