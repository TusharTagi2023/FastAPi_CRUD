import time
import jwt
from decouple import config



secret = "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"

algo = "HS256"

 
# def token_response(token: str):
#     return{
#         "access token":token
#     }

def signJWT(userID : str):
    payload = {
        "userID": userID,
        "expiry": time.time() + 60000
    }
    token = jwt.encode(payload, secret, algo)
    return {
        "access token":token
    }


def decodeJWT(token : str):
    print("------------------------------------------------------------")
    try:
        decode_token = jwt.decode(token, secret , algorithms=algo)
        print(decode_token,"----------------------------")
        return decode_token if decode_token['expiry'] >= time.time() else None
    except:
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        return None
    
     