import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker
from Models.Model import Usuarios
from Models.Model import Servidores
from Servidores.Servidores import acessar_servidor
from MongoDB.MongoFunctions import registrar_logs
from datetime import datetime

def cadastrar_usuario():
    print "cadastro de usuarios"
    nomeUser = raw_input("Digite o nome do usuario: ")
    emailUser = raw_input("Digite o email do usuario %s: "%nomeUser)
    while True:
        senhaUser = raw_input("Digite a senha do usuario %s: "%nomeUser)
        senhaConfirm = raw_input("Digite a senha novamente: ")
        if senhaConfirm != senhaUser:
            print "As senhas nao coincidem"
        else:
            break

    try:
        engine = create_engine("postgresql://onxentiadmin:123456@127.0.0.1/test")
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()
        usuario = Usuarios(nomeUser, emailUser, senhaUser)
        session.add(usuario)
        session.commit()
        print "Usuario %s adicionado com sucesso"%nomeUser
    except Exception as e:
        session.rollback()

def acessar_sistema():
    print "Acessando sistema"
    try:
        engine = create_engine("postgresql://onxentiadmin:123456@127.0.0.1/test")
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()
        emailUser = raw_input("Informe seu email: ")
        senhaUser = raw_input("Digite a sua senha de usuario: ")
        usuarios = session.query(Usuarios).all()
        for u in usuarios:
            if emailUser == u.email:
                if senhaUser == u.senha:
                    print "Usuario Autenticado"
                    acessar_servidor(emailUser)
                    srv = input("Digite o id do servidor que deseja acessar: ")
                    servidor = session.query(Servidores).filter(Servidores.id==srv).first()
                    registrar_logs(emailUser, servidor.endereco)
                    break
                else:
                    print "Senha Incorreta"
                    break
        else:
            print "Usuario nao encontrado"

    except Exception as e:
        print "Erro: %s"%e
        session.rollback()

def alterar_senha():
    print "Alteracao de senha"
    try: 
        engine = create_engine("postgresql://onxentiadmin:123456@127.0.0.1/test")
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()
        while True:
            emailUser = raw_input("Digite o seu email: ")
            senhaUser = raw_input("Digite a sua senha atual: ")
            usuario = session.query(Usuarios).filter(Usuarios.email==emailUser,Usuarios.senha==senhaUser).first()
            if usuario == None:
                print "Usuario ou senha incorretos"
            else:
                break

        while True:
            newSenha = raw_input("Digite a sua nova senha: ")
            confirmNew = raw_input("Confirme a sua nova senha: ")
            if confirmNew != newSenha:
                print "As senhas nao coincidem"
            else:
                usuario.senha = newSenha
                print "Senha alterada com sucesso"
                session.commit()
                break
    except Exception as e:
        print "Erro: %s"%e
        session.rollback()

def listar_adm():
    print "Lista de administradores do sistema"
    try:
        engine = create_engine("postgresql://onxentiadmin:123456@127.0.0.1/test")
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()
        usuarios = session.query(Usuarios).all()
        for u in usuarios:
            print "Id:",u.id,"Nome:",u.nome,"E-mail:",u.email
    except Exception as e:
        print "Erro: %s"%e

def sair():
    print "Saindo do sistema"
    sys.exit()