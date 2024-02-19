from models import Pessoa
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import hashlib

def retorna_session():
    USUARIO = 'root'
    SENHA = ''
    HOST = 'localhost'
    BANCO = 'loginstudy'
    PORT = '3306'

    CONN = f'mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}'

    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

class ControllerCadastro():
    @classmethod
    def verifica_dados(cls, nome, email, senha):
        if len(nome) > 50 or len(nome) < 3:
            return 2
        if len(email) > 200:
            return 3
        if len(senha) > 100 or len(senha) < 6:
            return 4
        
        return 1

    @classmethod
    def cadastrar(cls, nome, email, senha):
        session = retorna_session()
        usuario = session.query(Pessoa).filter(Pessoa.email == email).all()
        
        if len(usuario) > 0:
            return 5

        dados_verificados = cls.verifica_dados(nome, email, senha)
        
        if dados_verificados != 1:
            return dados_verificados
        
        try:
            senha = hashlib.sha256(senha.encode()).hexdigest()
            p1 = Pessoa(nome=nome, email=email, senha=senha)
            session.add(p1)
            session.commit()
            return 1
        except:
            return 3

print(ControllerCadastro.cadastrar('Liz', 'liz@gmail.com', 'liz1234'))