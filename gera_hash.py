import bcrypt
senha = "#Admnt1"
hashed = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
print(hashed)