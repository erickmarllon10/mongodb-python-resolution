from Usuarios.Usuarios import Users
from Servidores.Servidores import Servers
from MongoDB.MongoFunctions import MongoFunctions

def menu():
    lastaccess = MongoFunctions()
    lastaccess.listar_ultimos_acessos()
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
    server = Servers()
    user = Users()
    dict_options = {1:user.cadastrar_usuario,2:user.acessar_sistema,3:server.cadastrar_servidor,4:server.remover_servidor,5:server.definir_adm,6:user.alterar_senha,7:user.sair}
    dict_options[x]()

if __name__ == '__main__':
    try:
        while True:
            switch(menu())
    except Exception as e:
        print "Erro: "%e
