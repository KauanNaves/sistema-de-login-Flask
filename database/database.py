# Banco de dados fictício 
from werkzeug.security import generate_password_hash
USERS = [
    {
        "id":  1,
        "name": "Kauan Augusto Naves",
        "email": 'kauan@email.com',
        "password": generate_password_hash('123@Kauan')
    },
    {
        "id": 2,
        "name": "Cecília Marangoni dos Santos",
        "email": 'cecilia@email.com',
        "password": generate_password_hash('123#Cecilia')
    }
]

ID = len(USERS)