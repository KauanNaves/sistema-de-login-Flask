# Banco de dados fictício 
from werkzeug.security import generate_password_hash
USERS = [
    {
        "id":  1,
        "email": 'kauan@email.com',
        "password": generate_password_hash('123@Kauan')
    },
    {
        "id": 2,
        "email": 'cecilia@email.com',
        "password": generate_password_hash('123#Cecilia')
    }
]