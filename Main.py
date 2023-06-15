from classes import *

while True:
    print( '=' * 50)
    print(f'1 - Cadastrar animal\n'
        f'2 - Cadastrar Pessoa\n'
        f'3 - Lista de animais e pessoas interessadas\n'
        f'4 - Adoção')  
    print( '=' * 50)
    opcao = input("Escolha uma opção: ")
    if opcao == '1':
        casdastro_animal = Prefeitura()
        casdastro_animal.cadastrar_animal()
    elif opcao == '2':
        casdastro_pessoa = Prefeitura()
        casdastro_pessoa.cadastrar_pessoa()
    elif opcao == '3':
        prefeitura = Prefeitura()
        prefeitura.mostrar_animais_cadastrados()
        prefeitura.mostrar_pessoas_cadastradas()

