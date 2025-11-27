from conexao import conectar

def inserir_cliente(usuarios_id, nome, cpf, telefone, endereco, data_nascimento):
    con = conectar()
    cur = con.cursor()

    sql = """
    INSERT INTO clientes (usuarios_id, nome, cpf, telefone, endereco, data_nascimento)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    cur.execute(sql, (usuarios_id, nome, cpf, telefone, endereco, data_nascimento))
    con.commit()
    cur.close()
    con.close()

def buscar_por_cpf(cpf):
    con = conectar()
    cur = con.cursor(dictionary=True, buffered=True)

    sql = "SELECT * FROM clientes WHERE cpf = %s"
    cur.execute(sql, (cpf,))

    resultado = cur.fetchone()

    cur.close()
    con.close()
    return resultado