from Classes import *
prefeitura = Prefeitura()

while True:
    print('=' * 50)
    print(f'1 - Cadastrar animal\n'
          f'2 - Cadastrar Pessoa\n'
          f'3 - Lista de animais e pessoas interessadas\n'
          f'4 - Adoção\n'
          f'0 - Sair')
    print('=' * 50)
    opcao = input("Escolha uma opção: ")
    if opcao == '1':
        prefeitura.cadastrar_animal()
    elif opcao == '2':
        prefeitura.cadastrar_pessoa()
    elif opcao == '3':
        prefeitura.mostrar_cadastrados()
    elif opcao == '4':
        prefeitura.adocao()
    elif opcao == '0':
        break  # Sair do loop
    else:
        print('Opção inválida. Escolha novamente.')
