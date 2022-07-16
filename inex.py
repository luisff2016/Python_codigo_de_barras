# Menu do programa
import os

def tela():
    imprimirLinha()
    print('\t'*4,'CONTAS E TRIBUTOS')
    print('\t'*3,'(Agua, Luz, Telefone, IPTU, ISS)')
    imprimirLinha()
    print('\t'*3,'1) Pagamento c/ Código de Barras')
    print('\t'*3,'2) Imprimir 2ª Via de Boletos')
    print('\t'*3,'3) Sair')
    imprimirLinha()
    texto = '\t'*3 +'Digite a opção: '
    opcao = int(input(texto))
    validarOpcao(opcao)
    
def validarOpcao(opc):
    if opc == 1:
        print('TODO')
        print('Opção 1! ==> Pagamento c/ Código de Barras')
    elif opc == 2:
        print('TODO')
        print('Opção 2! ==> Imprimir 2ª Via de Boletos')
    elif opc == 3:
        print('SAIR!')
    else:
        os.system('clear')
        print('Opção Invalida!')
        tela()
        
def imprimirLinha():
        print('-'*70)
    
tela()