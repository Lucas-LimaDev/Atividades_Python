class Pessoa:
    def __init__(self,nome,idade,altura): #Construtor de uma classe pelo método __init__
        self.nome = nome                  #Self é obrigatório no Python
        self.idade = idade
        self.altura = altura
       

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")  
        print(f"Idade: {self.idade} anos")
        print(f"Altura: {self.altura: .2f} metros")

class Funcionario(Pessoa):
    def __init__(self, nome,idade,altura,cargo,salario):
        super().__init__(nome,idade,altura)
        self.cargo = cargo
        self.salario = salario
    
    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(F"Cargo : {self.cargo}\nSalário: R$ {self.salario: ,.2f}")


func1 = Funcionario("Ana", 25, 1.70, "CEO", 20000)
func1.exibir_informacoes()