from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker
from Models.Model import Servidores, Usuarios
from Usuarios.Usuarios import listar_adm


def cadastrar_servidor():
    print "Cadastro de Servidores"
    nome = raw_input("Digite o nome do servidor: ")
    endereco = raw_input("Digite o endereco IP do servidor %s: "%nome)
    adm = raw_input("Digite o nome do sysadmin do servidor %s: "%nome)
    try:
        engine = create_engine("postgresql://onxentiadmin:123456@127.0.0.1/test")
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()
        servidor = Servidores(nome, endereco, adm)
        session.add(servidor)
        session.commit()
        print "Servidor %s cadastrado com sucesso"%nome
    except Exception as e:
        print "Erro: "%e
        session.rollback()

def remover_servidor():
    print "Removendo servidores"
    try:
        engine = create_engine("postgresql://onxentiadmin:123456@127.0.0.1/test")
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()
        servidores = session.query(Servidores).all()
        for s in servidores:
            print "Id:",s.id,"Nome:",s.nome,"IP:",s.endereco
        opcao = input("Digite o ID do servidor que deseja remover: ")
        servidor = session.query(Servidores).filter(Servidores.id==opcao).first()
        ask = raw_input("Tem certeza que deseja remover o servidor %s? (s ou n): "%servidor.nome)
        if ask == 's':
            session.delete(servidor)
            session.commit()
            print "Servidor %s removido com sucesso!"%servidor.nome
        else:
            print "Parece que vc desistiu!"
    except Exception as e:
        print "Erro: %s"%e

def definir_adm():
    listar_adm()
    print "Definindo administrador"
    try:
        engine = create_engine("postgresql://onxentiadmin:123456@127.0.0.1/test")
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()
        option = input("Digite o ID do administrador: ")
        usuario = session.query(Usuarios).filter(Usuarios.id==option).first()
        defAdm = raw_input("Deseja definir o adm %s como administrador de um servidor? (s ou n): "%usuario.nome)
        if defAdm == 's':
            servidores = session.query(Servidores).all()
            for s in servidores:
                print "Id:",s.id,"Nome:",s.nome,"IP:",s.endereco,"Adm Atual:",s.administrador
                while True:
                    option2 = input("Digite o ID do servidor que deseja definir para o usuario %s: "%usuario.nome)
                    if option2 != s.id:
                        print "Id invalido"
                    else:
                        break
                serverID = session.query(Servidores).filter(Servidores.id==option2).first()
                defnewAdm = raw_input("Deseja definir este usuario como adm do servidor %s ? (s ou n): "%serverID.nome)
                if defnewAdm == 's':
                    serverID.administrador = usuario.nome
                    session.commit()
                    print "%s definido(a) como novo(a) adm deste servidor"%usuario.nome
                    for s in servidores:
                        print "Id:",s.id,"Nome:",s.nome,"IP:",s.endereco,"Adm Atual:",s.administrador

                else:
                    print "Ops, voce desistiu de definir este usuario como adm"

        else:
            print "Ops, parece que voce desistiu!"

    except Exception as e:
        print "Erro %s"%e
