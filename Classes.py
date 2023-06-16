class Animal:
    def __init__(self, especie, idade_estimada, cor, porte, particularidade):
        self.especie = especie
        self.idade_estimada = idade_estimada
        self.cor = cor
        self.porte = porte
        self.particularidade = particularidade

    def exibir_dados(self):
        print('Animais')
        print(f"Espécie: {self.especie}")
        print(f"Idade Estimada: {self.idade_estimada}")
        print(f"Cor: {self.cor}")
        print(f"Porte: {self.porte}")
        print(f"Particularidade: {self.particularidade}")
    
    def __eq__(self, other):
        if isinstance(other, Animal):
            return (
                self.especie == other.especie
                and self.idade_estimada == other.idade_estimada
                and self.cor == other.cor
                and self.porte == other.porte
                and self.particularidade == other.particularidade
            )
        return False


class Pessoa:
    def __init__(self, nome, telefone, email, endereco, especie_interesse, preferencia_animal):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.especie_interesse = especie_interesse
        self.preferencia_animal = preferencia_animal

    def exibir_dados(self):
        print('Pessoas')
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print(f"E-mail: {self.email}")
        print(f"Endereço: {self.endereco}")
        print(f"Espécie de Interesse: {self.especie_interesse}")
        print(f"Preferência de Animal: {self.preferencia_animal}")

    def __eq__(self, other):
        if isinstance(other, Pessoa):
            return (
                self.nome == other.nome
                and self.telefone == other.telefone
                and self.email == other.email
                and self.endereco == other.endereco
                and self.especie_interesse == other.especie_interesse
                and self.preferencia_animal == other.preferencia_animal
            )
        return False


class Prefeitura: 
    def __init__(self):
        self.animais = []
        self.pessoas = []
        

    def cadastrar_animal(self):
        especie = input('Tipo do animal: ')
        idade_estimada = int(input('Idade do animal: '))
        cor = input('Cor do animal: ')
        porte = input('Porte do animal: ')
        particularidade = input('Particularidade do animal: ')
        animal = Animal(especie, idade_estimada, cor, porte, particularidade)
        self.animais.append(animal)

    def cadastrar_pessoa(self):
        nome = input('Nome da pessoa: ')
        telefone = int(input('Telefone da pessoa: '))
        email = input('Email da pessoa: ')
        endereco = input('Endereço da pessoa: ')
        especie_interesse = input('Espécie de interesse da pessoa: ')
        preferencia_animal = input('Preferência de animal da pessoa: ')
        pessoa = Pessoa(nome, telefone, email, endereco, especie_interesse, preferencia_animal)
        self.pessoas.append(pessoa)

    def mostrar_cadastrados(self):
        for animal in self.animais:
            animal.exibir_dados()
        for pessoa in self.pessoas:
            pessoa.exibir_dados()

    def adocao(self):
        
        especie = input('Tipo do animal a ser adotado: ')
        idade_estimada = int(input('Idade do animal a ser adotado: '))
        cor = input('Cor do animal a ser adotado: ')
        porte = input('Porte do animal a ser adotado: ')
        particularidade = input('Particularidade do animal a ser adotado: ')
        animal = Animal( especie, idade_estimada, cor, porte, particularidade)
        self.animais.remove(Animal(especie, idade_estimada, cor, porte, particularidade))

        nome_pessoa = input('Nome da pessoa que está adotando: ')
        telefone_pessoa = int(input('Telefone da pessoa que está adotando: '))
        email_pessoa = input('Email da pessoa que está adotando: ')
        endereco_pessoa = input('Endereço da pessoa que está adotando: ')
        especie_interesse_pessoa = input('Espécie de interesse da pessoa que está adotando: ')
        preferencia_animal_pessoa = input('Preferência de animal da pessoa que está adotando: ')
        pessoa = Pessoa(nome_pessoa, telefone_pessoa, email_pessoa, endereco_pessoa, especie_interesse_pessoa, preferencia_animal_pessoa)
        self.pessoas.remove(pessoa)
