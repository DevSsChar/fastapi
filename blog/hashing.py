from passlib.context import CryptContext

pwd_cxt=CryptContext(schemes=["argon2"], deprecated="auto")

# we use argon2 here since bcrypt was cracking
class Hash():
    def bcrypt(password: str):
        return pwd_cxt.hash(password)