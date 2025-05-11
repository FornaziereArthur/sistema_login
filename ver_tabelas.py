from app import db, Usuario
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'

with app.app_context():
    # Lista todas as tabelas
    print("\nTabelas no banco de dados:")
    print("-------------------------")
    for table in db.metadata.tables:
        print(f"- {table}")
    
    # Mostra a estrutura da tabela Usuario
    print("\nEstrutura da tabela Usuario:")
    print("-------------------------")
    for column in Usuario.__table__.columns:
        print(f"- {column.name}: {column.type}")
    
    # Lista todos os usuários cadastrados
    print("\nUsuários cadastrados:")
    print("-------------------------")
    usuarios = Usuario.query.all()
    for usuario in usuarios:
        print(f"ID: {usuario.id}")
        print(f"Nome: {usuario.nome}")
        print(f"Email: {usuario.email}")
        print("-------------------------") 