from Usuarios.Usuarios import cadastrar_usuario, acessar_sistema, alterar_senha, sair
from Servidores.Servidores import cadastrar_servidor, remover_servidor, definir_adm
from MongoDB.MongoFunctions import listar_ultimos_acessos

def menu():
    listar_ultimos_acessos()
    print "\
            1 - Cadastrar Usuario: \n\
            2 - Acessar Sistema: \n\
            3 - Cadastrar Servidor: \n\
            4 - Remover Servidor: \n\
            5 - Definir Administrador: \n\
            6 - Alterar Senha: \n\
            7 - Sair: \n"

    opcao = input("Digite a sua opcao: ")
    return opcao

def switch(x):
    dict_options = {1:cadastrar_usuario,2:acessar_sistema,3:cadastrar_servidor,4:remover_servidor,5:definir_adm,6:alterar_senha,7:sair}
    dict_options[x]()

if __name__ == '__main__':
    try:
        while True:
            switch(menu())
    except Exception as e:
        print "Erro: "%e
