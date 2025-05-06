from database import db
import json

class Numero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numeros_originais = db.Column(db.Text)
    numeros_ordenados = db.Column(db.Text)
    data_criacao = db.Column(db.DateTime, server_default=db.func.now())

    def to_dict(self):
        originais = json.loads(self.numeros_originais)
        ordenados = json.loads(self.numeros_ordenados)
        return {
            'id': self.id,
            'numeros_originais': f'{originais}',
            'numeros_ordenados': f'{ordenados}',
            'data_criacao': self.data_criacao.isoformat() if self.data_criacao else None
        }
    
    def adicionar_db(numeros, numeros_ordenados):
        try:
            novo_numero = Numero(
                numeros_originais= json.dumps(numeros),
                numeros_ordenados= json.dumps(numeros_ordenados)
            )
            db.session.add(novo_numero)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
    
    def __repr__(self):
        return f'<Numero {self.id}>'