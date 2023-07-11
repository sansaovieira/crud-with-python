import sqlite3 as lite

# Criando conexão
con = lite.connect('data.db')


#Inserindo Informações
def inserir_info(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO form (nome, email, telefone, dia, estado, assunto) VALUES (?,?,?,?,?,?)"
        cur.execute(query, i)


#Lendo Informações

def mostrar__info():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM form"
        cur.execute(query)
        info = cur.fetchall()

        for i in informacao:
            lista.append(i)
            return lista

#Atualizando Informações
def atualizar_info(i):
    with con:
        cur = con.cursor()
        query = "UPDATE form SET nome=?, email=?, telefone=?, dia=?, estado=?, assunto=? WHERE id=?"
        cur.execute(query, i)


#Apagando Informações
with con:
    cur = con.cursor()
    query = "DELETE FROM form WHERE id=?"
    cur.execute(query, [1])
