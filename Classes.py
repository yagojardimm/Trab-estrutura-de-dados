class Animal:
    def init(self, especie, idade_estimada, cor, porte, particularidade):
        self.especie = especie
        self.idade = idade_estimada
        self.cor = cor
        self.porte = porte
        self.particularidade = particularidade

    def exibir_dados(self):
        print(f"Espécie: {self.especie}")
        print(f"Idade Estimada: {self.idade_estimada}")
        print(f"Cor: {self.cor}")
        print(f"Porte: {self.porte}")
        print(f"Particularidade: {self.particularidade}")

class Pessoa:
    def init(self, nome, telefone, email, endereco, especie_interesse, preferencia_animal):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.especie_interesse = especie_interesse
        self.preferencia_animal = preferencia_animal

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print(f"E-mail: {self.email}")
        print(f"Endereço: {self.endereco}")
        print(f"Espécie de Interesse: {self.especie_interesse}")
        print(f"Preferência de Animal: {self.preferencia_animal}")

class Prefeitura: 
    def __init__(self):
        self.animais = []
        self.pessoas = []
        

    def cadastrar_animal(self):
        animal = Animal()
        animal = str(input(f'Tipo do animal: '))
        animal = int(input(f'Idade do animal: '))
        animal = str(input(f'Cor do animal: '))
        animal = str(input(f'Porte do animal: '))
        animal = str(input(f'Particularidade do animal: '))
        self.animais.append(animal)

    def cadastrar_pessoa(self):
        pessoa = Pessoa()
        pessoa = str(input('Nome da pessoa: '))
        pessoa = int(input('Telefone da pessoa: '))
        pessoa = str(input('Email da pessoa: '))
        pessoa = input('Endereço da pessoa: ')
        pessoa = str(input('Espécie de interesse da pessoa: '))
        pessoa = str(input('Preferencia de animal da pessoa: '))
        self.pessoas.append(pessoa)

    def mostrar_cadastrados(self):
        for animal in self.animais:
            animal.exibir_dados()
        for pessoa in self.pessoas:
            pessoa.exibir_dados()

    def adocao(self):
        animal_adotado = Animal()
        animal_adotado = str(input(f'Tipo do animal: '))
        animal_adotado = int(input(f'Idade do animal: '))
        animal_adotado = str(input(f'Cor do animal: '))
        animal_adotado = str(input(f'Porte do animal: '))
        animal_adotado = str(input(f'Particularidade do animal: '))
        self.animais.remove(animal_adotado)
        pessoa = Pessoa()
        pessoa = str(input('Nome da pessoa: '))
        pessoa = int(input('Telefone da pessoa: '))
        pessoa = str(input('Email da pessoa: '))
        pessoa = input('Endereço da pessoa: ')
        pessoa = str(input('Espécie de interesse da pessoa: '))
        pessoa = str(input('Preferencia de animal da pessoa: '))
        self.pessoas.remove(pessoa)
