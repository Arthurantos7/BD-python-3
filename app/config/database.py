from sqlalchemy import create_engine
from sqlalchemy import sessionmaker
from contextlib import contextmanager

#Parâmetros para conexão com BD MySQL.
db_user = "user"
db_password = "user_passowrd"
db_host = "localhost"
db_port = "3306"
db_name = "meu_banco"

# Endereço/ caminho para conexão com BD MySQL.
DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# Conectando ao banco de dados.
db = create_engine(DATABASE_URL)
Session = sessionmaker(bind=db)
Session = Session()

# Geremciando sessão.
@contextmanager
def get_db():
    db = Session()
    try:
        yield db
        db.commit() #se tudo de certo, faz commit.
    except Exception as erro:
        db.rollback() # se der errado, desfaz a operão.
        raise erro # Lança a exceçaõ, informando o erro.
    finally:
        db.close() # Garante o fechamento da sessão.     
