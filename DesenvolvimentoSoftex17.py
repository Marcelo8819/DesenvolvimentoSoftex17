

def calc(a, b, op):
   if (op == 1):
       res = a + b
   elif (op == 2):
       res = a - b
   elif (op == 3):
       res = a * b
   elif (op == 4):
       res = a / b
   else:
       res = 0
   return res


def opcoes():
   print('Escolha a operação você deseja realizar:')
   print('_____' * 8)
   print('digite 1 para adição')
   print('digite 2 para subtração')
   print('digite 3 para multiplicação')
   print('digite 4 para divisão')
   print('_____' * 8)


n = 1
while n != 0 or (op == 0 and op > 4):
   print('operações matemática!')
   opcoes()
   op = int(input(f' start '))
   if op <= 4 and op >= 1:
       print('ok, vamos para o próximo passo')
   else:
       print('opção inválida, por favor, dgite um dos nº solicitados. \n')
       opcoes()
       op = int(input(f' start '))
   a = int(input(' primeiro numero:  '))
   b = int(input('insira o segundo número:  '))
   calc(a, b, op)
   print(f'o resultado é {calc(a, b, op)}')

   n = int(input('se desejar parar, digite [0], para continuar digite [1]'))
print('fim!')

