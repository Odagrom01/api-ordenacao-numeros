from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app):
    app.config.update({
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///numeros.db',
        'SQLALCHEMY_TRACK_MODIFICATIONS': False
    })
    db.init_app(app)

    with app.app_context():
        db.create_all()
        print('Banco de dados inicializado')