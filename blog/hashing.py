from passlib.context import CryptContext

pwd_cxt=CryptContext(schemes=["argon2"], deprecated="auto")

# we use argon2 here since bcrypt was cracking
class Hash():
    def bcrypt(password: str):
        return pwd_cxt.hash(password)

    def verify(hashed_password: str, plain_password: str):
        # first provide plain password, then hashed password
        return pwd_cxt.verify(plain_password, hashed_password)