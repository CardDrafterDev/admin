import jwt
import os, dotenv


def _get_secret():
    dotenv.load_dotenv()
    secret = os.environ["JWT_SECRET"]
    return secret

def decrypt_jwt(token: str) -> dict[str, dict[str, any]]:
    
    secret = _get_secret()
    
    decoded_data = jwt.decode(
        jwt=token,
        key=secret,
        algorithms=["HS256"]
    )
    
    return decoded_data


def encrypt_jwt(headers: dict, payload: dict) -> str:
    
    secret = _get_secret()
    
    encoded_data = jwt.encode(
        headers=headers,
        payload=payload,
        key=secret,
        algorithm="HS256"
    )

    return encoded_data
