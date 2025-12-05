import datetime
from datetime import datetime, timedelta, timezone
# immport JWTError and jwt from jose
from jose import JWTError, jwt
# https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#hash-and-verify-the-passwords
# codes can be found in the official documentation link above
SECRET_KEY = "b4e1a0c9c3e54f71a4f8d8f74c52c1f603f2a5bc8cdd4e61b2f283f54d7e92af"
algorithm = "HS256"
access_token_expire_minutes = 30

# data we will give, expires_delta is the expiry time
def create_access_token(data: dict):
    to_encode = data.copy()
    # if expires_delta:
    #     expire = datetime.now(timezone.utc) + expires_delta
    # else: optional
    expire = datetime.now(timezone.utc) + timedelta(minutes=access_token_expire_minutes)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=algorithm)
    return encoded_jwt