from config import *

class Cachorro(db.Model):

    # atributos do cachorro

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    genero = db.Column(db.String(20))
    idade = db.Column(db.String(20))
    raca = db.Column(db.String(100))
    porte = db.Column(db.String(20))
    cor = db.Column(db.String(20))
    problemaDeSaude = db.Column(db.String(200))

    def __str__(self):
        return str(self.id)+") "+ self.nome + ", " + self.genero + ", " + self.idade + ", " + self.raca + ", " + self.porte + ", " + self.cor + ", " + self.problemaDeSaude
    
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "genero": self.genero,
            "idade": self.idade,
            "raca": self.raca,
            "porte": self.porte,
            "cor": self.cor,
            "problemaDeSaude": self.problemaDeSaude
        }

class Veterinario(db.Model):

    # atributos do veterinário, que é responsável pelos medicamentos do cachorro

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100)) # nome do veterinário
    registro = db.Column(db.String(200)) # registro que confirma a atuação legal do veterinário no mercado de trabalho
    clinica = db.Column(db.String(100)) # clínica veterinária em que o veterinário atua e atende o cachorro
    
    # atributo de chave estrangeira
    cachorro_id = db.Column(db.Integer, db.ForeignKey(Cachorro.id))
    # atributo de relacionamento, para acesso aos dados via objeto
    cachorro = db.relationship("Cachorro")

    def __str__(self): # expressão da classe em forma de texto
        return self.nome + ", " + self.registro + ", " + self.clinica + ", " + str(self.cachorro)

    def json(self):
        return {

            "id": self.id,
            "nome": self.nome,
            "registro": self.registro,
            "clinica": self.clinica,
            "cachorro_id": self.cachorro_id,
            "cachorro": self.cachorro.json()
        } 

class Medicamento(db.Model):

    # atributos do medicamento que, segundo o veterinário, é necessário para tratar o cachorro

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100)) # nome do medicamento
    dosagem = db.Column(db.String(100)) # quantidade de medicamento a ser dado a cada x horas
    valor = db.Column(db.String(100)) # valor a ser cobrado pelo medicamento
    
    # atributo de chave estrangeira
    cachorro_id = db.Column(db.Integer, db.ForeignKey(Cachorro.id))
    # atributo de relacionamento, para acesso aos dados via objeto
    cachorro = db.relationship("Cachorro")

    def __str__(self): # expressão da classe em forma de texto
        return self.nome + ", " + self.dosagem + ", " + self.valor + ", " + str(self.cachorro)

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "dosagem": self.dosagem,
            "valor": self.valor,
            "cachorro_id": self.cachorro_id,
            "cachorro": self.cachorro.json()
        } 
  
if __name__ == "__main__":

    if os.path.exists(arquivobd):
        os.remove(arquivobd)


    db.create_all()

    # teste da classe Cachorro

    cachorroum = Cachorro(nome = "Toby", genero = "masculino", idade = "5 meses", raca = "labrador", porte = "grande", cor = "preto", problemaDeSaude = "pulgas")
    cachorrodois = Cachorro(nome = "Lulu", genero = "feminino", idade = "4 anos", raca = "sem raça definida", porte = "pequeno", cor = "branco com marrom", problemaDeSaude = "vermes")
    cachorrotres = Cachorro(nome = "Tommy", genero = "masculino", idade = "14 anos", raca = "poodle", porte = "médio", cor = "branco", problemaDeSaude = "carrapatos")         


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

    # teste da classe Veterinario

    veterinarioum = Veterinario(nome = "José da Silva", registro = "CRMV nº 7263", clinica = "Clínica Veterinária Anjo de Quatro Patas")
    veterinariodois = Veterinario(nome = "Maria do Carmo", registro = "CRMV nº 4729", clinica = "Clínica Veterinária Bom Amigo")
    veterinariotres = Veterinario(nome = "Luíza Santos", registro = "CRMV nº 9482", clinica = "Clínica Veterinária Arranhões Amorosos")


    db.session.add(veterinarioum)
    db.session.add(veterinariodois)
    db.session.add(veterinariotres)
    db.session.commit()
    

    print(veterinarioum)
    print(veterinariodois)
    print(veterinariotres)

    
    print(veterinarioum.json())
    print(veterinariodois.json())
    print(veterinariotres.json())

    # teste da classe Medicamento

    medicamentoum = Medicamento(nome = "Antipulgas e Carrapatos Bravecto", dosagem = "único comprimido mastigável", valor = "R$ 150,00")
    medicamentodois = Medicamento(nome = "Vermífugo Helfine Plus", dosagem = "1 comprimido a cada 10 kg do cachorro", valor = "R$ 40,00")
    medicamentotres = Medicamento(nome = "Suplemento Mineral Nutripharme Defengy OC", dosagem = "1 g a cada refeição", valor = "R$ 130,00")


    db.session.add(medicamentoum)
    db.session.add(medicamentodois)
    db.session.add(medicamentotres)
    db.session.commit()
    

    print(medicamentoum)
    print(medicamentodois)
    print(medicamentotres)

    
    print(medicamentoum.json())
    print(medicamentodois.json())
    print(medicamentotres.json())