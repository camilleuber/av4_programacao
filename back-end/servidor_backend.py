from config import *
from modelo import Cachorro

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

@app.route("/incluir_cachorro", methods=['post'])
def incluir_cachorro():
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    dados = request.get_json()
    try: 
      nova = Cachorro(**dados) 
      db.session.add(nova) 
      db.session.commit() 
    except Exception as e: 
      resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 

@app.route("/excluir_cachorro/<int:cachorro_id>", methods=['DELETE'])
def excluir_cachorro(cachorro_id):
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    try:
        Cachorro.query.filter(Cachorro.id == cachorro_id).delete()
        db.session.commit()
    except Exception as e:
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 


app.run(debug=True)