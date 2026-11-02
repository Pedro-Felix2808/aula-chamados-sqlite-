import sqlite3

def conectar_banco():
    conexao = sqlite3.connect("chamados.db")
    cursor = conexao.cursor()

    sql = '''
    create table if not exists chamados (
        id integer primary key autoincrement,
        titulo text not null,
        prioridade text not null,
        status text not null,
        usuario text not null
    )
    '''
    cursor.execute(sql)
    conexao.commit()
    return conexao, cursor



def abrir_chamado():
    conexao, cursor = conectar_banco()

    titulo = input("Digite o título do chamado: ")
    prioridade = input("Digite a prioridade do chamado (Baixa,Média,Alta,Crítica): ")
    status = input("Digite o status do chamado (Aberto,Em progresso,Fechado): ")
    usuario = input("Digite o nome do usuário: ")

    sql = '''
    insert into chamados (titulo, prioridade, status, usuario)
    values (?, ?, ?, ?)
    '''
    cursor.execute(sql, (titulo, prioridade, status, usuario))
    conexao.commit()
    print("Chamado aberto com sucesso!")



def listar_chamados():
    conexao, cursor = conectar_banco()

    sql = '''
    select * from chamados
    '''
    cursor.execute(sql)
    resultados = cursor.fetchall()

    if len(resultados) == 0:
        print("Nenhum chamado encontrado.")

    else:
        print("### LISTA DE CHAMADOS ###")

        print(
            f"{'ID':<5} | {'Título':<20} | {'Prioridade':<15} | {'Status':<20} | {'Usuário':<20}"
        )

        print("-" * 100)

        for chamado in resultados:
            print(
                f"{chamado[0]:<5} | "
                f"{chamado[1]:<20} | "
                f"{chamado[2]:<15} | "
                f"{chamado[3]:<20} | "
                f"{chamado[4]:<20}"
            )



def pesquisa_usuario():
    conexao, cursor = conectar_banco()

    usuario = input("Digite o nome do usuário para pesquisa: ")

    sql = '''
    select * from chamados where usuario LIKE ?
    '''
    cursor.execute(sql, (f"%{usuario}%",))
    resultados = cursor.fetchall()

    if len(resultados) == 0:
        print("Nenhum chamado encontrado.")

    else:
        print("### RESULTADO DA BUSCA ###")

        print(
            f"{'ID':<5} | {'Título':<20} | {'Prioridade':<15} | {'Status':<20}"
        )

        print("-" * 100)

        for chamado in resultados:
            print(
                f"{chamado[0]:<5} | "
                f"{chamado[1]:<20} | "
                f"{chamado[2]:<15} | "
                f"{chamado[3]:<20}"
            )



def pesquisa_prioridade():
    conexao, cursor = conectar_banco()

    prioridade = input("Digite a prioridade para pesquisa (Baixa,Média,Alta,Crítica): ")

    sql = '''
    select * from chamados where prioridade LIKE ?
    '''
    cursor.execute(sql, (f"%{prioridade}%",))
    resultados = cursor.fetchall()

    if len(resultados) == 0:
        print("Nenhum chamado encontrado.")

    else:
        print("### RESULTADO DA BUSCA ###")

        print(
            f"{'ID':<5} | {'Título':<20} | {'Prioridade':<15} | {'Status':<20}"
        )

        print("-" * 100)

        for chamado in resultados:
            print(
                f"{chamado[0]:<5} | "
                f"{chamado[1]:<20} | "
                f"{chamado[2]:<15} | "
                f"{chamado[3]:<20}"
            )


def pesquisa_status():
    conexao, cursor = conectar_banco()

    status = input("Digite o status para pesquisa (Aberto,Em progresso,Fechado): ")

    sql = '''
    select * from chamados where status LIKE ?
    '''
    cursor.execute(sql, (f"%{status}%",))
    resultados = cursor.fetchall()

    if len(resultados) == 0:
        print("Nenhum chamado encontrado.")

    else:
        print("### RESULTADO DA BUSCA ###")

        print(
            f"{'ID':<5} | {'Título':<20} | {'Prioridade':<15} | {'Status':<20}"
        )

        print("-" * 100)

        for chamado in resultados:
            print(
                f"{chamado[0]:<5} | "
                f"{chamado[1]:<20} | "
                f"{chamado[2]:<15} | "
                f"{chamado[3]:<20}"
            )



def chamados_urgentes():
    conexao, cursor = conectar_banco()

    sql = '''
    select * from chamados where prioridade = 'Crítica'
    AND status = 'Aberto'
    '''
    cursor.execute(sql)
    resultados = cursor.fetchall()

    if len(resultados) == 0:
        print("Nenhum chamado urgente encontrado.")

    else:
        print("### CHAMADOS URGENTES ###")

        print(
            f"{'ID':<5} | {'Título':<20} | {'Prioridade':<15} | {'Status':<20} | {'Usuário':<20}"
        )

        print("-" * 100)

        for chamado in resultados:
            print(
                f"{chamado[0]:<5} | "
                f"{chamado[1]:<20} | "
                f"{chamado[2]:<15} | "
                f"{chamado[3]:<20} | "
                f"{chamado[4]:<20}"
            )




def resolver_chamado():
    conexao, cursor = conectar_banco()

    id_chamado = input("Digite o ID do chamado a ser resolvido: ")

    sql = '''
    update chamados set status = 'Em progresso' where id = ?
    '''
    cursor.execute(sql, (id_chamado,))
    conexao.commit()

    if cursor.rowcount == 0:
        print("Chamado não encontrado.")
    else:
        print("Chamado  colocado para resolver com sucesso!")



def excluir_chamado():
    conexao, cursor = conectar_banco()

    id_chamado = input("Digite o ID do chamado a ser excluído: ")

    sql = '''
    delete from chamados where id = ?
    '''
    cursor.execute(sql, (id_chamado,))
    conexao.commit()

    if cursor.rowcount == 0:
        print("Chamado não encontrado.")
    else:
        print("Chamado excluído com sucesso!")



def menu():

    while True:

        print()
        print("### LISTA DE TAREFAS ###")
        print("1 - Abrir chamado")
        print("2 - Listar chamados")
        print("3 - Pesquisa por usúario")
        print("4 - Pesquisa por prioridade")
        print("5 - Pesquisa por status")
        print("6 - Chamados urgentes")
        print("7 - Resolver chamado")
        print("8 - Excluir chamado")
        print("0 - sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            
            abrir_chamado()

        elif opcao == "2":
            
            listar_chamados()

        elif opcao == "3":

            pesquisa_usuario()

        elif opcao == "4":

            pesquisa_prioridade()

        elif opcao == "5":

            pesquisa_status()

        elif opcao == "6":
        
            chamados_urgentes()

        elif opcao == "7":

            resolver_chamado()

        elif opcao == "8":

            excluir_chamado()

        elif opcao == "0":

            print("Saindo do programa...")
            break

        else:

            print("Opção inválida. Tente novamente.")


menu()