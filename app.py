from flask import Flask, make_response, jsonify, request
from database import db, init_app
from trataments import Tratamentos
from models import Numero
import json

app = Flask(__name__)
app.json.sort_keys = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

init_app(app)

@app.route('/numeros', methods=['GET'])
def get_numeros():
    try:
        registros = Numero.query.all()
        historico = [r.to_dict() for r in registros]
        
        return make_response(
            jsonify({
                'status': 'ok',
                'message': 'Historico de numeros ordenados',
                'data': historico,
                'total': len(historico)
            }),
            200
        )
        
    except Exception as e:
        return Tratamentos.erro_resposta(f'Erro ao processar números: {str(e)}', 500)

@app.route('/ordenar', methods=['POST'])
def ordenar_numeros():
    dados = request.get_json(silent=True)

    if not dados:
        return Tratamentos.erro_resposta('JSON invalido ou ausente')

    numeros = dados.get('numeros')

    if not isinstance(numeros, list) or len(numeros) < 3:
        return Tratamentos.erro_resposta('Envie uma lista com pelo menos 3 numeros na chave "numeros"')
    
    numeros_ordenados = sorted(numeros)

    Numero.adicionar_db(numeros, numeros_ordenados)
    
    return Tratamentos.sucesso_resposta(
        'Dados recebidos e armazenados com sucesso', numeros_ordenados
    )   

if __name__ == '__main__':
    app.run(debug= True)