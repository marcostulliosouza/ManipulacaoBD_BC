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

# def adicionar_colaborador(cursor, nome_usuario, senha_usuario, login_usuario):
#     query = "INSERT INTO colaboradores (col_nome, col_categoria, col_ativo, col_senha, col_login) VALUES (%s, 10, 1, %s, %s)"
#     cursor.execute(query, (nome_usuario, senha_usuario, login_usuario))
#     cursor.connection.commit()
#     print("Colaborador adicionado com sucesso!")

# def atualizar_usuario(cursor, senha_usuario, login_usuario):
#     query = "UPDATE colaboradores SET col_senha = %s WHERE col_login = %s"
#     cursor.execute(query, (senha_usuario, login_usuario))
#     cursor.connection.commit()
#     print("Colaborador adicionado atualizado!")

# def buscar_id_cliente(cursor, nome_cliente):
#     # Consulta para buscar o ID do cliente pelo nome
#     query = "SELECT cli_id FROM clientes WHERE cli_nome = %s"
#     cursor.execute(query, (nome_cliente,))
#     resultado = cursor.fetchone()
#     if resultado:
#         return resultado[0]  # Retorna o primeiro valor encontrado (ID do cliente)
#     else:
#         return None  # Retorna None se nenhum cliente for encontrado

#
def adicionar_produto(cursor):
    # Inserir um novo produto na tabela produtos
    query = "INSERT INTO produtos (pro_nome, pro_cliente, pro_ativo, pro_com_teste) VALUES ('31000005583', 317, 1, 1)"
    cursor.execute(query)
    # Commit para confirmar a transação
    cursor.connection.commit()
    print("Produto adicionado com sucesso!")
# def alterarStatusDispositivo(cursor):
#     query = 'UPDATE dispositivos SET dis_status = 1 WHERE dis_id = 932;'
#     cursor.execute(query)
#     if cursor.connection.commit():
#         print('Sucesso!')
#     else:
#         print('Não sucesso!')

# def adicionar_cliente(cursor, nome_cliente):
#     # Inserir um novo produto na tabela produtos
#     query = "INSERT INTO clientes (cli_nome, cli_responsavel, cli_ativo) VALUES (%s, 8, 1)"
#     cursor.execute(query, (nome_cliente))
#     # Commit para confirmar a transação
#     cursor.connection.commit()
#     print("Cliente adicionado com sucesso!")

# def mudarDetrator(cursor):
#     query = "UPDATE detratores SET dtr_indicador = 0 WHERE dtr_id = 60"
#     cursor.execute(query)
#     # Commit para confirmar a transação
#     cursor.connection.commit()
#     print("sucesso!")
# def adicionarDetrator(cursor):
#     query = "INSERT INTO detratores (dtr_id, dtr_tipo, dtr_indicador, dtr_descricao, dtr_ativo) VALUES (67, 6, 0, 'CHAMADO CANCELADO', 1)"
#     cursor.execute(query)
#     # Commit para confirmar a transação
#     cursor.connection.commit()
#     print("sucesso!")

# def atualizarDescricao(cursor):
#     query = 'ALTER TABLE acoes_chamados MODIFY ach_descricao VARCHAR(1000);'
#     cursor.execute(query)
#     if cursor.connection.commit():
#         print('Sucesso!')
#     else:
#         print('Não sucesso!')
# def alterarClientedoDispositivo(cursor):
#     query = 'UPDATE dispositivos SET dis_cliente = 321 WHERE dis_id = 984;'
#     cursor.execute(query)
#     if cursor.connection.commit():
#         print('Sucesso!')
#     else:
#         print('Não sucesso!')
# def deletarProduto(cursor):
#     query = 'DELETE FROM produtos WHERE pro_id = 12795;'
#     cursor.execute(query)
#     cursor.connection.commit()  # Executa a operação de commit diretamente
#     if cursor.rowcount > 0:
#         print('Sucesso! Linhas afetadas:', cursor.rowcount)
#     else:
#         print('Nenhuma linha afetada. Produto não encontrado ou já excluído.')

# def adicionarLocal(cursor):
#     query = "INSERT INTO local_chamado (loc_id, loc_nome) VALUES (59, '13THP04')"
#     cursor.execute(query)
#     # Commit para confirmar a transação
#     if cursor.connection.commit():
#         print("sucesso!")

# def atualizarLocaL(cursor):
#     query = "UPDATE local_chamado SET loc_nome = 'LFREE-006' WHERE loc_id = 36"
#     cursor.execute(query)
#     # Commit para confirmar a transação
#     cursor.connection.commit()
#     print("sucesso!")

# def deletarPlanodeProducao(cursor, id):
#     try:
#         # Deletar todas as ordens de produção associadas ao plano de produção
#         query_delete_ordens = f'DELETE FROM ordens_de_producao WHERE odp_plano_de_producao = {id};'
#         cursor.execute(query_delete_ordens)
#
#         # Deletar o plano de produção
#         query_delete_plano = f'DELETE FROM planos_de_producao WHERE pdp_id = {id};'
#         cursor.execute(query_delete_plano)
#
#         # Confirmar a transação
#         cursor.connection.commit()
#
#         print('Sucesso!')
#     except Exception as e:
#         # Se ocorrer algum erro, fazer rollback e imprimir a mensagem de erro
#         cursor.connection.rollback()
#         print(f'Erro ao deletar o plano de produção: {e}')
#         print('Não sucesso!')
# def adicionarProduto(cursor):

def main():
    try:
        # Conectar ao banco de dados
        conexao = pymysql.connect(**config)
        with conexao.cursor() as cursor:
            # alterarStatusDispositivo(cursor)
            adicionar_produto(cursor)
            # alterarClientedoDispositivo(cursor)
            # deletarProduto(cursor)
            # atualizarLocaL(cursor)
            #  deletarPlanodeProducao(cursor, 1716)
            # adicionarLocal(cursor)
            # deletarDispositivo(cursor)
            # atualizarDescricao(cursor)
            # adicionarDetrator(cursor)
            # mudarDetrator(cursor)
            # nome_produto = 'SMART7'
            # adicionar_produto(cursor)
            # adicionar_cliente(cursor, 'T4S')
            # name_user = 'Samuel Grontoski'
            # pass_user = hashlib.md5('0123456'.encode()).hexdigest()
            # print(pass_user)
            # log_user = 'samuel.grontoski'
            # atualizar_usuario(cursor, pass_user, log_user)
            # adicionar_colaborador(cursor, name_user, pass_user, log_user)
            # print(f'Adicionado {name_user}')
            # # Exemplo: Adicionar o produto '2022.5.0SQR' do cliente 'Uppay'
            # nome_cliente = 'Uppay'
            # id_cliente = buscar_id_cliente(cursor, nome_cliente)
            # if id_cliente is not None:
            #     '''
            #     adicionar_produto(cursor, '2022.5.0SQR', id_cliente)
            #     '''
            # else:
            #     print("Cliente não encontrado.")


    except pymysql.Error as err:
        print("Erro ao conectar ou manipular o banco de dados:", err)

    finally:
        # Fechar conexão com o banco de dados
        if 'conexao' in locals() and conexao.open:
            conexao.close()
            print("Conexão fechada.")


if __name__ == "__main__":
    main()