from config import *

class Cachorro(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    genero = db.Column(db.String(20))
    idade = db.Column(db.String(20))
    raca = db.Column(db.String(100))
    porte = db.Column(db.String(20))
    cor = db.Column(db.String(20))

    def __str__(self):
        return str(self.id)+") "+ self.nome + ", " + self.genero + ", " + self.idade + ", " + self.raca + ", " + self.porte + ", " + self.cor
    
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "genero": self.genero,
            "idade": self.idade,
            "raca": self.raca,
            "porte": self.porte,
            "cor": self.cor
        }

  
if __name__ == "__main__":

    if os.path.exists(arquivobd):
        os.remove(arquivobd)


    db.create_all()

    cachorroum = Cachorro(nome = "Toby", genero = "masculino", idade = "5 meses", raca = "labrador", porte = "grande", cor = "preto")
    cachorrodois = Cachorro(nome = "Lulu", genero = "feminino", idade = "4 anos", raca = "sem raça definida", porte = "pequeno", cor = "branco com marrom")
    cachorrotres = Cachorro(nome = "Tommy", genero = "masculino", idade = "14 anos", raca = "poodle", porte = "médio", cor = "branco")         


    db.session.add(cachorroum)
    db.session.add(cachorrodois)
    db.session.add(cachorrotres)
    db.session.commit()
    

    print(cachorroum)
    print(cachorrodois)
    print(cachorrotres)

    
    print(cachorroum.json())
    print(cachorrodois.json())
    print(cachorrotres.json())