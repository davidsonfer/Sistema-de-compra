print('=' * 10, end=' ')
print('LOJAS DAVIDSON', end=' ')
print('=' * 10)

preco = float(input('Preço das compras: R$ '))
opçao = int(input('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão 
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão.
Qual é a opcão: '''))
if opçao == 1:
    preco = preco - (preco * 10 / 100)
    print(f'O valor final da compra é de R$ {preco:.2f}')
elif opçao == 2:
    preco = preco - (preco * 5 / 100)
    print(f'O valor da compra é no total de R$ {preco:.2f}')
elif opçao == 3:
    parcela2x = preco / 2
    print(f'O valor total da compra é de R$ {preco:.2f} em 2x de {parcela2x} no cartão')
elif opçao == 4:
    parcelamento = int(input('Em quantas vezes você gostaria de fazer? '))
    preco = preco + (preco * 20 / 100)
    parcela = preco / parcelamento
    print(f'O valor total da compra é de {preco:.2f} em {parcelamento}x de {parcela:.2f}')
else:
    print(f'Opção inválidade de pagamento. Tente navamente!')