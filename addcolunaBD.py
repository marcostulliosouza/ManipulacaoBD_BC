import pymysql.cursors
import hashlib

# Configurações do banco de dados
config = {
    'host': '10.161.100.11',
    'user': 'bct_write',
    'password': 'bcwriter22',
    'database': 'better_call_test',
    'charset': 'utf8',  # Definindo o conjunto de caracteres como utf8
}

def adicionarTabelaLocalChamado(cursor):
    query = "CREATE TABLE local_chamado (loc_id INT(10), loc_nome VARCHAR(45));"
    cursor.execute(query)
    # Commit para confirmar a transação
    if cursor.connection.commit():
        print("Tabela local_chamado adicionada com sucesso!")
    else:
        print("Erro ao adicionar tabela local_chamado")
def inserindoDadosLocalChamado(cursor):
    query = """
    INSERT INTO local_chamado (loc_id, loc_nome) VALUES 
    (1, 'DEBUG - LF'), 
    (2, 'DEBUG'),
    (3, 'POS-001'), 
    (4, 'POS-002'), 
    (5, 'POS-003'), 
    (6, 'POS-004'), 
    (7, 'POS-005'),
    (8, 'POS-006'), 
    (9, 'POS-007'), 
    (10, 'POS-008'), 
    (11, 'POS-009'), 
    (12, 'POS-010'), 
    (13, 'POS-011'), 
    (14, 'POS-012'), 
    (15, 'POS-013'), 
    (16, 'POS-028'), 
    (17, 'POS-029'), 
    (18, 'POS-030'), 
    (19, 'POS-032'), 
    (20, 'POS-033'), 
    (21, 'POS-034'), 
    (22, 'POS-036'), 
    (23, 'POS-037'), 
    (24, 'POS-038'), 
    (25, 'POS-039'), 
    (26, 'POS-040'), 
    (27, 'POS-041'), 
    (28, 'POS-042'), 
    (29, 'POS-043'), 
    (30, 'POS-044'), 
    (31, 'LF-001'), 
    (32, 'LF-002'), 
    (33, 'LF-003'), 
    (34, 'LF-004'), 
    (35, 'LF-005'), 
    (36, 'LF-006'), 
    (37, 'MEC-001'), 
    (38, 'MEC-002'), 
    (39, 'MEC-003'), 
    (40, 'MEC-004'), 
    (41, 'MEC-EXTERNO'), 
    (42, 'EXTERNO'), 
    (43, 'RMA')
    """
    cursor.execute(query)
    if cursor.connection.commit():
        print("Itens adicionados!")
    else:
        print("Falha ao adicionar itens!")

def adicionarColuna(cursor):
    # Inserir um novo produto na tabela produtos
    query = "ALTER TABLE chamados ADD COLUMN cha_local VARCHAR(45);"
    cursor.execute(query)
    # Commit para confirmar a transação
    if cursor.connection.commit():
       print('deu certo')

def atualizarColuna(cursor, tabela, coluna, tipo):
    # Inserir um novo produto na tabela produtos
    query = "ALTER TABLE %s MODIFY %s %s;"
    cursor.execute(query, (tabela, coluna, tipo))
    # Commit para confirmar a transação
    if cursor.connection.commit():
        print(f"{coluna} adicionada com sucesso na tabela {tabela}!")
    else:
        print(f"Erro ao adicionar {coluna} na tabela {tabela}")

def adicionarValorTiposChamados(cursor):
    query = "INSERT INTO tipos_chamado (tch_id, tch_descricao) VALUES (6, MUDANÇA DE POSIÇÃO)"
    cursor.execute(query)
    if cursor.connection.commit():
        print("Item adicionado!")
    else:
        print("Falha ao adicionar item!")

def main():
    try:
        # Conectar ao banco de dados
        conexao = pymysql.connect(**config)
        with conexao.cursor() as cursor:
            adicionarColuna(cursor)
            atualizarColuna(cursor, 'chamados', 'cha_descricao', 'VARCHAR(1000)')
            adicionarTabelaLocalChamado(cursor)
            inserindoDadosLocalChamado(cursor)
            adicionarValorTiposChamados(cursor)
    except pymysql.Error as err:
        print("Erro ao conectar ou manipular o banco de dados:", err)

    finally:
        # Fechar conexão com o banco de dados
        if 'conexao' in locals() and conexao.open:
            conexao.close()
            print("Conexão fechada.")


if __name__ == "__main__":
    main()
