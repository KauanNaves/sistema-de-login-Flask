# Implementando Banco de Dados do Sistema de Login usando sqlite3

import sqlite3


# Criar conexão e criando o banco caso não exista
def createConn():
    conn = sqlite3.connect("./database/login.db")
    conn.row_factory = sqlite3.Row # Permitindo acessar os dados pelo nome das colunas
    return conn


# Criar cursor
def createCursor(conn):
    cursor = conn.cursor()
    return cursor


# Criar tabela users se não existir
def createTable():
    try:
        conn = createConn()
        cursor = createCursor(conn)

        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER NOT NULL PRIMARY KEY, name TEXT NOT NULL, email TEXT NOT NULL UNIQUE, password TEXT NOT NULL, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")
        conn.commit()
        return True
    
    except sqlite3.IntegrityError as e:
        print(f"Erro de integridade: {e}")
        conn.rollback()

    except sqlite3.OperationalError as e:
        print(f"Erro operacional: {e}")
        conn.rollback()

    except sqlite3.Error as e:
        print(f"Ocorreu um erro no banco de dados: {e}")
        conn.rollback()

    finally:
        cursor.close()
        conn.close()
        
    return False


# Criar usuário
def createUser(name: str, email: str, password: str):
    try:
        conn = createConn()
        cursor = createCursor(conn)

        cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?);", (name, email, password,))
        conn.commit()
        return True
    
    except sqlite3.IntegrityError as e:
        print(f"Erro de integridade: {e}")
        conn.rollback()

    except sqlite3.OperationalError as e:
        print(f"Erro operacional: {e}")
        conn.rollback()

    except sqlite3.Error as e:
        print(f"Ocorreu um erro no banco de dados: {e}")
        conn.rollback()

    finally:
        cursor.close()
        conn.close()
    
    return False


# Buscar usuário por id
def getUserById(id: int):
    try:
        conn = createConn()
        cursor = createCursor(conn)

        user = cursor.execute("SELECT * FROM users WHERE id = ?;", (id,)).fetchone()
        return user
    
    except sqlite3.IntegrityError as e:
        print(f"Erro de integridade: {e}")

    except sqlite3.OperationalError as e:
        print(f"Erro operacional: {e}")

    except sqlite3.Error as e:
        print(f"Ocorreu um erro no banco de dados: {e}")

    finally:
        cursor.close()
        conn.close()

    return False


def getUserByEmail(email: str):
    try:
        conn = createConn()
        cursor = createCursor(conn)

        user = cursor.execute("SELECT * FROM users WHERE email = ?;", (email,)).fetchone()
        return user
    
    except sqlite3.IntegrityError as e:
        print(f"Erro de integridade: {e}")

    except sqlite3.OperationalError as e:
        print(f"Erro operacional: {e}")

    except sqlite3.Error as e:
        print(f"Ocorreu um erro no banco de dados: {e}")

    finally:
        cursor.close()
        conn.close()

    
    return False


# Deletar usuário
def deleteUser(id: int, email: str):
    try:
        conn = createConn()
        cursor = createCursor(conn)

        cursor.execute("DELETE FROM users WHERE id = ? AND email = ?;", (id, email,))
        conn.commit()
        return True

    except sqlite3.IntegrityError as e:
        print(f"Erro de integridade: {e}")
        conn.rollback()

    except sqlite3.OperationalError as e:
        print(f"Erro operacional: {e}")
        conn.rollback()

    except sqlite3.Error as e:
        print(f"Ocorreu um erro no banco de dados: {e}")
        conn.rollback()

    finally:
        cursor.close()
        conn.close()
    
    return False


