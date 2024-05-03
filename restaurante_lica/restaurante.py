import os 
#inserir 2 restaurantes na list
# restaurantes=['Bife Sujo', 'Saco de Feijão'] 
restaurantes = [
    {'nome': 'Lilica na cozinha ', 'categoria': 'prato-feito', 'ativo': True},
    {'nome': 'Simons', 'categoria': 'pizzaria', 'ativo': False},
    {'nome': 'Lanche ou Net', 'categoria': 'lanchonete', 'ativo': True}
]


def mostrar_subtitulo():
    os.system('cls')
    print ('texto')
    print()
    
def finalizar_app():
    # os.system('cls')
    # print ('Finalizando app\n')
    mostrar_subtitulo('Finalizando o app')



def chamar_nome_do_app():
     print ('''ℜ𝔈𝔰𝔱𝔞𝔲𝔯𝔞𝔫𝔱𝔢 𝔢𝔵𝔭𝔯𝔢𝔰𝔰𝔬''') 

def opcao_invalida():
    print('Opção invalida\n')
    # input('Digite uma tecla para voltar ao menu principal: ')
    # main() 
    voltar_ao_menu_principal()

def exibir_opcoes():
    print('1-Cadastrar um restaurante')
    print('2-Listar restaurantes')
    print('3-Ativar um restaurante')
    print('4-Sair do programa')

def voltar_ao_menu_principal():
     input("\n Digite uma tecla para voltar ao menu principal: \n")
     main() 


def cadastrar_novo_restaurante():
     os.system('cls')
     nome_do_restaurante=input('Digite o nome do novo restaurante: \n')
     categoria= input (f'Digite a categoria do restaurante {nome_do_restaurante}: ' )
     dados_do_restaurante ={'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
     restaurantes.append(dados_do_restaurante)
     print(f'O restaurante {nome_do_restaurante}, foi cadastrado com sucesso\n')
     voltar_ao_menu_principal()

def listar_restaurantes():
    os. system('cls')
    print('Listando os restaurantes \n')
    #em português
    for restaurante in restaurantes:
        # print(f'-{restaurante}')
    #modificando a maneira de listar restaurante
    #para manipular o dicionário
        nome_res=restaurante['nome']
        categoria=restaurante['categoria']
        ativo=restaurante['ativo']
        print(f'-{nome_res} |- {categoria} | -{ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    mostrar_subtitulo("Alternano o estado o restaurante")
    nome_restaurante=input("Digite o nome do restaurante que desejas alternar o estado")
    restaurante_encontrado=False
    for restaurante in restaurantes:
        if nome_restaurante==restaurante['nome']:
            restaurante_encontrado=True
            restaurante['ativo']=not restaurante['ativo']
            mensagem=f'O restaurante{nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante}foi desativado com sucesso'
            print(mensagem)
            if not restaurante_encontrado:
                print('O restaurante não foi encontrado')

def escolher_opcoes(): 
    try:
        opcao_digitada = int(input('Escolha uma opção: '))
        print('Você selecionou a opção:', opcao_digitada, '\n')
        if opcao_digitada == 1:
            print('Você escolheu cadastrar um restaurante\n')
            cadastrar_novo_restaurante()
        elif opcao_digitada == 2:
            listar_restaurantes()
        elif opcao_digitada == 3:
            alternar_estado_restaurante()  # Adicionando a chamada para alternar o estado do restaurante
        elif opcao_digitada == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls') 

    chamar_nome_do_app() 

    exibir_opcoes() 

    escolher_opcoes() 


if(__name__=='__main__'):
    main()