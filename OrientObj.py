class Pessoa:
    def __init__(self,nome,idade,altura):        #Construtor de uma classe pelo método __init__
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.__saudacao()

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")  #Self é obrigatório no Python
        print(f"Idade: {self.idade} anos")
        print(f"Altura: {self.altura: .2f} metros")

    def __saudacao(self):  # Dois __ encapsulamento do método saudacao
        print("Oi,Seja Bem vindo! ")


pessoa1 = Pessoa("Ana", 35, 1.70)    #pessoa1 é um objeto da classe Pessoa
pessoa1.exibir_informacoes()



pessoa2 = Pessoa("Lucas Lima", 27, 1.65)
pessoa2.exibir_informacoes()


