from config import *
from modelo import Cachorro, Veterinario, Medicamento


@app.route("/")
def inicio():
    return 'Sistema de cadastro de cachorros. '+\
        '<a href="/listar_cachorros">Cheque aqui os listados</a>'

@app.route("/listar_cachorros")
def listar_cachorros():
    cachorros = db.session.query(Cachorro).all()
    cachorros_em_json = [ x.json() for x in cachorros ]
    resposta = jsonify(cachorros_em_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 

@app.route('/inserir_cachorro', methods=['post'])
def inserir_cachorro():
    response = jsonify({"status": "201", "result": "ok", "details": "Cachorro adicionado!"})
    data = request.get_json()
    try:
        novo = Cachorro(**data)
        db.session.add(novo)
        db.session.commit()
    except Exception as e:
        response = jsonify({"status": "400", "result": "error", "details ": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response 

@app.route('/deletar_cachorros/<int:id>', methods=['DELETE'] )
def deletar_cachorros(id):
    response = jsonify({"status": "200", "result": "ok", "details": "ok"})
    try:
        Cachorro.query.filter(Cachorro.id == id).delete()
        db.session.commit()
    except Exception as e:
        response = jsonify({"status": "400" , "result": "error", "details": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
    
@app.route("/listar_veterinarios")
def listar_veterinarios():
    veterinarios = db.session.query(Veterinario).all()
    lista_jsons = [ x.json() for x in veterinarios ]
    resposta = jsonify(lista_jsons)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/listar_medicamentos")
def listar_medicamentos():
    medicamentos = db.session.query(Medicamento).all()
    lista_jsons = [ x.json() for x in medicamentos ]
    resposta = jsonify(lista_jsons)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

if __name__ == '__main__':
    app.run(debug=True)