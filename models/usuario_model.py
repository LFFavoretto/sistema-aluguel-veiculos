from conexao import conectar

def inserir_usuario(email, senha):
    con = conectar()
    cur = con.cursor()

    sql = """
    INSERT INTO usuarios (email, senha)
    VALUES (%s, %s)
    """
    cur.execute(sql, (email, senha))

    con.commit()
    usuarios_id = cur.lastrowid
    cur.close()
    con.close()
    return usuarios_id


def buscar_por_email(email):
    con = conectar()
    cur = con.cursor(dictionary=True, buffered=True)

    sql = "SELECT * FROM usuarios WHERE email = %s"
    cur.execute(sql, (email,))
    
    resultado = cur.fetchone()

    cur.close()
    con.close()
    return resultado

