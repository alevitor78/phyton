"""
Exercicios seção 5


# 1 - recebe 2 números e mostra qual é o maior

num1 = float(input('Informe o primeiro número para comparação: '))
num2 = float(input('Informe o segundo número para comparação: '))
if num1 > num2:
    print(f'O maior número é o {num1}')
elif num1 == num2:
    print(f'Os dois números são iguais!')
else:
    print(f'O maior número é o {num2}')


# 2 - calcular a raiz quadrada de um número positivo e informar que é inválido se for negativo

num = float(input('Informe o número para cálculo da Raiz Quadrada: '))
if num >= 0:
    res = num ** (1/2)
    print(f'A raiz quadrada de {num} é {res}')
else:
    print(f'O número informado é inválido!')


# 3 - ler um número real, se for positivo, imprimir a raiz quadrada, se for negativo, imprimir o número ao quadrado
import math

num = float(input('Informe um número real para cálculo: '))
if num >= 0:
    res = math.sqrt(num)
    print(f'A raiz quadrada do número informado é {res}')
else:
    res = num ** 2
    print(f'O número elevado ao quadrado é {res}')


# 4 - leia um número e se for positivo, calcule e mostre o número digitado ao quadrado
# e sua raiz quadrada
import math

num = float(input('Informe um número: '))
if num >= 0:
    numqd = num ** 2
    numrqd = math.sqrt(num)
    print(f'O número {num} ao quadrado é {numqd} e sua raiz quadrada é {numrqd}')
else: print(f'O número não é positivo!')
# funcionou


# 5 - programa que verifica se um número é par ou ímpar
num = int(input('Informe o número para verificar: '))
if (num % 2) == 0:
    print(f'O número informado é par!')
else: print(f'O número informado é ímpar!')
# funcionou


# 6 - recebe dois números inteiros e mostra o maior deles e a diferença entre eles.
num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
dif = num1 - num2
if num1 > num2:
    print(f'O maior número é {num1} e a diferença entre {num1} e {num2} é {dif}')
elif num1 == num2:
    print(f'Os dois números são iguais! e a diferença entre eles é 0!')
else: print(f'O maior número é {num2} e a diferença entre {num1} e {num2} é {dif}')
# funcionou

# 7 - recebe dois números inteiros e mostra o maior deles e se eles são iguais.
num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
if num1 > num2:
    print(f'O maior número é {num1}')
elif num1 == num2:
    print(f'Os dois números são iguais!')
else: print(f'O maior número é {num2}')
# funcionou


# 8 - recebe duas notas entre 0.0 e 10.0, valida e informa a média
nota1 = float(input('Informe a primeira nota do aluno: '))
if nota1 < 0 or nota1 > 10:
    print(f'A nota digitada está incorreta!')
    exit()
nota2 = float(input('Informe a segunda nota do aluno: '))
if nota2 < 0 or nota2 > 10:
    print(f'A nota digitada está incorreta!')
    exit()
media = (nota1 + nota2) / 2
print(f'A média entre as notas informadas é {media:.1f}')
# funcionou


# 9 - Lê o salário e a prestação do empréstimo, se a prestação for menor que 20% concede, senão não concede

salario = float(input('Informe o salário do trabalhador R$ '))
parcela = float(input('Informe o valor da parcela do empréstimo R$ '))
analise = salario * 0.2
if parcela > analise:
    print(f'Empréstimo não concedido, excede 20 % do salário!')
else:
    print(f'Empréstimo concedido!')
# funcionou


# 10 - recebe a altura e o sexo da pessoa e retorna o seu peso ideal

altura = float(input('Informe sua altura em metros '))
sexo = (input('Informe seu sexo H para Homem ou M para Mulher: ').upper())
if sexo == 'H':
    peso = (72.7 * altura) - 58
elif sexo == 'M':
    peso = (62.1 * altura) - 44.7
else:
    print(f'O sexo informado é inválido!')
    exit()
print(f'Seu peso ideal é {peso} kg')
# funcionou


# 11 - leia um número inteiro maior que zero e devolva a soma dos seus algarismos

num = int(input('Informe um número maior que 0: '))
numero = str(num)
if num > 0:
    soma = int(numero[0]) + int(numero[1]) + int(numero[2]) + int(numero[3])
    print(f'A soma dos algarismos do número informado é {soma}')
else:
    print(f'Número inválido!')
# funcionou


# 12 - ler um número inteiro positivo e calcular o logaritmo dele
import math

num = int(input('Informe um número inteiro: '))
if (num > 0):
    res = math.log(num,10)
    print(f'O logaritmo do número informado é {res}')
else:
    print(f'Número inválido!')
# funcionou


# 13 - calcula a média ponderada de 3 notas

n1 = float(input('Informe a primeira nota com peso 1: '))
n2 = float(input('Informe a segunda nota com peso 1: '))
n3 = float(input('Informe a terceira nota com peso 2: '))
media = (n1 + n2 + (2 * n3)) / 4
if media >= 60:
    print(f'O Aluno foi aprovado com média {media:.1f}')
else:
    print(f'O Aluno foi reprovado com média {media:.1f}')
# funcionou


# 14 - calcula a média ponderada com diversos pesos

n1 = float(input('Informe a nota do trabalho de laboratório de 0 a 10: '))
if n1 > 10 or n1 < 0:
    print(f'Nota inválida!')
    exit()
n2 = float(input('Informe a nota de avaliação semestral de 0 a 10: '))
if n2 > 10 or n2 < 0:
    print(f'Nota inválida!')
    exit()
n3 = float(input('Informe a nota de exame final de 0 a 10: '))
if n3 > 10 or n3 < 0:
    print(f'Nota inválida!')
    exit()
media = float(((n1 * 2) + (n2 * 3) + (n3 * 5)) / 10)

if media <= 2.9:
    print(f'Aluno reprovado, média {media:.1f}')
elif 2.9 < media <= 4.9:
    print(f'Aluno em recuperação, média {media:.1f}')
else:
    print(f'Aluno aprovado, média {media:.1f}')

# funcionou


# 15 - leia um número inteiro e imprima o dia da semana usando switch

def diasemana(dsemana):
    opcoes = {
        1: "domingo",
        2: "segunda",
        3: "terça",
        4: "quarta",
        5: "quinta",
        6: "sexta",
        7: "sábado",
    }
    return opcoes.get(dsemana, "Dia informado é inválido")


dsemana = int(input('Informe o número do dia da semana: '))
print(f'o dia da semana é {diasemana(dsemana)}')
# funcionou


# 16 - leia um número inteiro entre 1 e 12 e imprima o mês

def mesext(mesnum):
    opcoes = {
        1: "janeiro",
        2: "fevereiro",
        3: "março",
        4: "abril",
        5: "maio",
        6: "junho",
        7: "julho",
        8: "agosto",
        9: "setembro",
        10: "outubro",
        11: "novembro",
        12: "dezembro",
    }
    return opcoes.get(mesnum, "inválido!")

mesnum = int(input("Informe o número correspondente ao mês: "))
print(f'O mês informado é {mesext(mesnum)}')
# funcionou


# 17 - calcula e mostra a área de um trapézio

basemenor = float(input('Informe a base menor do trapézio: '))
if basemenor <= 0:
    print(f'O valor informado deve ser maior que 0!')
    exit()
basemaior = float(input('Informe a base maior do trapézio: '))
if basemaior <= 0:
    print(f'O valor informado deve ser maior que 0!')
    exit()
altura = float(input('Informe a altura do trapezio: '))
if altura <= 0:
    print(f'O valor informado deve ser maior que 0!')
    exit()
area = ((basemaior + basemenor) * altura) / 2

print(f'A área do trapézio é {area}')
# funcionou


# 18 - seleciona e executa as 4 operações matemáticas

print(f'Programa para cálculo de operações matemáticas:')
print(f'Informe 1 para Soma, 2 para Subtração, 3 para Multiplicação e 4 para Divisão')
operador = int(input('Informe a operação desejada: '))
valor1 = float(input('Informe o primeiro valor para o cálculo: '))
valor2 = float(input('Informe o segundo valor para o cálculo: '))

if operador == 1:
    calculo = valor1 + valor2
    formula = "soma"
elif operador == 2:
    calculo = valor1 - valor2
    formula = "diferença"
elif operador == 3:
    calculo = valor1 * valor2
    formula = "multiplicação"
elif operador == 4:
    calculo = valor1 / valor2
    formula = "divisão"
else:
    print(f'A operação informada é inválida!')
    exit()
print(f'O resultado da {formula} entre {valor1} e {valor2} é: {calculo}')

# funcionou


# 19 - programa para verificar se um número é divisível por 3 e por 5 mas não pelos dois.

numero = int(input('Informe um número para verificar a divisão por 3 e 5: '))

if (numero % 3 == 0 and numero % 5 != 0):
    print(f'O número {numero} é divisível por 3')
if (numero % 5 == 0 and numero % 3 != 0):
    print(f'O número {numero} é divisível por 5')
if (numero % 5 == 0 and numero % 3 == 0):
    print(f'O número {numero} está inválido, pois é divisível por 3 e por 5 simultaneamente!')
# funcionou


# 20 - verificar um triângulo e o tipo

ladoa = float(input('Informe a medida do lado A do triângulo: '))
ladob = float(input('Informe a medida do lado B do triângulo: '))
ladoc = float(input('Informe a medida do lado C do triângulo: '))
# validações
if (ladoa <= ladob + ladoc and ladob <= ladoa + ladoc and ladoc <= ladoa + ladob):
    print(f'Os tamanhos dos lados são válidos para formarem um triângulo')
else:
    print(f'O tamanho dos lados é inválido!')
    exit()
if (ladoa == ladob == ladoc):
    print(f'O triângulo formado é equilátero!')
elif (ladoa == ladob or ladoa == ladoc or ladob == ladoc):
    print(f'O triângulo formado é isósceles!')
else:
    print(f'O triângulo formado é escaleno!')
# funcionou


# 21 - executa operações matemáticas de acordo com o menu

opcao = int(input('Escolha a opção: \n '
                  '1 - Soma de 2 números \n '
                  '2 - Diferença entre 2 números \n '
                  '3 - Produto entre 2 números \n '
                  '4 - Divisão entre 2 números \n '
                  'Opção '))
if opcao < 1 or opcao > 4:
    print(f'A opção escolhida é inválida!')
    exit()
num1 = float(input('Informe o primeiro número para a operação: '))
num2 = float(input('Informe o segundo número para a operação: '))
if opcao == 1:
    calc = num1 + num2
    operacao = 'soma'
elif opcao == 2:
    if num1 > num2:
        calc = num1 - num2
    else:
        calc = num2 - num1
    operacao = 'diferença'
elif opcao == 3:
    calc = num1 * num2
    operacao = 'multiplicação'
elif opcao == 4:
    if num2 == 0:
        print('O denominador não pode ser zero!')
        exit()
    else:
        calc = num1 / num2
        operacao = 'divisão'
else:
    exit()
print(f'o cálculo de {operacao} entre os números informados é {calc}')

# funcionou


# 22 - Aposentadoria

idade = int(input('Informe a idade do trabalhador: '))
tempotrab = int(input('Informe o tempo trabalhado em anos: '))
if idade >= 65:
    print(f'O trabalhador pode se aposentar!')
elif tempotrab >= 30:
    print(f'O trabalhador pode se aposentar!')
elif idade >= 60 and tempotrab >= 25:
    print(f'O trabalhador pode se aposentar!')
else:
    print(f'O trabalhador não pode se aposentar!')

# funcionou

# 23 - Verifica se um ano é bissexto

ano = int(input('Informe o ano para validação: '))
if ((ano % 400 == 0) or (ano % 4 == 0)) and (ano % 100 != 0):
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')
# funcionou


# 24 - calcula o preço final por estado

def impostouf(estado):
    opcoes = {
        'MG': 7,
        'SP': 12,
        'RJ': 15,
        'MS': 8,
        }
    return opcoes.get(estado, 0)

valor = float(input('Informe o valor do produto R$ '))
estado = input('Informe o Estado onde o produto será vendido: ').upper()

if impostouf(estado) == 0:
    print(f'O Estado informado está inválido!')
    exit()
else:
    precofinal = valor + ((valor * impostouf(estado)) / 100)
    print(f'O preço final do produto é R$ {precofinal}')
# funcionou


# 25 - Calcula as raízes de equações do 2º grau

# definição das variáveis da equação
vara = int(input('Informe a varável a da equação: '))
if vara == 0:
    print(f'O valor é inválido, não é equação do segundo grau!')
    exit()
varb = int(input('Informe a variável b da equação: '))
varc = int(input('Informe a variável c da equação: '))

# cálculo do delta
delta = varb ** 2 - (4 * vara * varc)

# cálculo das raízes
x1 = ((varb * (-1)) + (delta ** (1/2))) / 2 * vara
x2 = ((varb * (-1)) - (delta ** (1/2))) / 2 * vara

# impressão dos resultados
print(f'A equação formada é {vara}x² + {varb}x + {varc} = 0')
if delta < 0:
    print(f'Não existe raiz!')
elif delta == 0:
    print(f'Existe uma raiz real: {x1}')
else:
    print(f'As raízes da equação são {x1} e {x2}.')
# funcionou

# 26 - calcula o consumo e mostra mensagem

dist = float(input('Informe a distância percorrida em km: '))
litros = float(input('Informe a quantidade de litros de gasolina gastos: '))
consumo = dist / litros
if consumo < 8:
    print(f'Consumo {consumo} km/l - Venda o carro!')
elif consumo >= 8 and consumo < 12:
    print(f'Consumo {consumo} km/l - Econômico!')
else:
    print(f'Consumo {consumo} km/l - Super Econômico!')
# funcionou


# 27 - informa a categoria do nadador de acordo com sua idade

idade = int(input('Informe a idade do nadador: '))
if idade < 5:
    print(f'Idade inválida!')
elif idade >= 5 and idade <= 7:
    print(f'Categoria Infantil A')
elif idade >= 8 and idade <= 10:
    print(f'Categoria Infantil B')
elif idade >= 11 and idade <= 13:
    print(f'Categoria Juvenil A')
elif idade >= 14 and idade <= 17:
    print(f'Categoria Juvenil B')
else:
    print(f'Categoria Sênior')
# funcionou


# 28 - lê 3 números e 1 opção para cálculo da média

numx = int(input('Informe o primeiro número: '))
numy = int(input('Informe o segundo número: '))
numz = int(input('Informe o terceiro número: '))

if numx <= 0 or numy <= 0 or numz <= 0:
    print(f'Foi informado um valor negativo ou zero, o programa será encerrado!')
    exit()

opmedia = input('Informe a opção de média desejada \n'
                'A - Média Geométrica \n'
                'B - Média Ponderada \n'
                'C - Média Harmônica \n'
                'D - Média Aritmética \n'
                'Opção: ').upper()
if opmedia == 'A':
    media = float((numx * numy * numz) ** (1/3))
    tipo = 'Geométrica'
elif opmedia == 'B':
    media = float((numx + (2 * numy) + (3 * numz)) / 6)
    tipo = 'Ponderada'
elif opmedia == 'C':
    media = float(1 / ((1 / numx) + (1 / numy) + (1 / numz)))
    tipo = 'Harmônica'
elif opmedia == 'D':
    media = float((numx + numy + numz) / 3)
    tipo = 'Aritmética'
else:
    print(f'Opção inválida!')
    exit()

print(f'A Média {tipo} dos números informados é {media}')
# funcionou


# 29 - prova de matemática com 5 questões
import random

count = 0
acerto = 0

while count < 5:
    count = count + 1
    numa = random.randint(1,100)
    numb = random.randint(1,100)
    soma = numa + numb
    resp = int(input(f'Questão {count}: Informe a soma dos números: {numa} + {numb}: '))
    if resp == soma:
        acerto = acerto + 1
        print(f'A resposta está correta! Acertos: {acerto}')
    else:
        print(f'A resposta está errada! A resposta correta é {soma}! Acertos: {acerto}')

# funcionou


# 30 - recebe três números e os ordena:

lista = [int(input('Informe o número 1: \n')),
         int(input('Informe o número 2: \n')),
         int(input('Informe o número 3: \n'))]
lista.sort()
print(lista)
# funcionou

# 31 - recebe a altura e o peso e retorna a classificação

peso = int(input('Informe o peso da pessoa em kg: '))
altura = float(input('Informe a altura da pessoa em metros: '))

if altura < 1.2:
    if peso < 60:
        clas = 'A'
    elif peso >= 60 and peso <= 90:
        clas = 'D'
    else:
        clas = 'G'
elif altura >= 1.2 and altura <= 1.7:
    if peso < 60:
        clas = 'B'
    elif peso >= 60 and peso <= 90:
        clas = 'E'
    else:
        clas = 'H'
else:
    if peso < 60:
        clas = 'C'
    elif peso >= 60 and peso <= 90:
        clas = 'F'
    else:
        clas = 'I'
print(f'Para a altura de {altura} m e o peso de {peso} kg, a classificação da pessoa é {clas}')

# funcionou


# 32 - calcula o preço do lanche de acordo com o cardápio

def cardapio(codigo):
    valor = {
        100: 1.2,
        101: 1.3,
        102: 1.5,
        103: 1.2,
        104: 1.7,
        105: 2.2,
        106: 1.0,
    }
    return valor.get(codigo, 0)

codigo = int(input('Informe o código do produto: '))
qtd = int(input('Informe a quantidade do produto: '))

if cardapio(codigo) == 0:
    print(f'O código do produto está inválido!')
    exit()
else:
    conta = cardapio(codigo) * qtd
    print(f'O valor da conta para a {qtd} produto(s) {codigo} é {conta}')

# funcionou


# 33 - recebe o preço antigo e calcula o preço novo e exibe mensagem

precoant = float(input('Informe o preço antigo do produto R$ '))
if precoant < 50:
    aum = 5
elif precoant >= 50 and precoant <= 100:
    aum = 10
else:
    aum = 15

preconovo = precoant + (precoant * aum / 100)

if preconovo <= 80:
    msg = 'BARATO'
elif preconovo > 80 and preconovo <= 120:
    msg = 'NORMAL'
elif preconovo > 120 and preconovo <= 200:
    msg = 'CARO'
else:
    msg = 'MUITO CARO'

print(f'O preço era R$ {precoant} e aumentou {aum} % e agora é R$ {preconovo} e está {msg}!')

# funcionou


# 34 - lê a nota e as faltas e retorna o conceito do aluno

nota = float(input('Informe a nota: '))
faltas = int(input('Informe a quantidade de faltas: '))

if faltas <= 20 and faltas >= 0:
    if nota >= 0 and nota <= 3.9:
        conceito = 'E'
    elif nota >= 4 and nota <= 4.9:
        conceito = 'D'
    elif nota >= 5 and nota <= 7.4:
        conceito = 'C'
    elif nota >= 7.5 and nota <= 8.9:
        conceito = 'B'
    elif nota >= 9 and nota <= 10:
        conceito = 'A'
    else:
        conceito = 'VALORES INFORMADOS SÃO INVÁLIDOS'
else :
    if nota >= 0 and nota <= 3.9:
        conceito = 'E'
    elif nota >= 4 and nota <= 4.9:
        conceito = 'E'
    elif nota >= 5 and nota <= 7.4:
        conceito = 'D'
    elif nota >= 7.5 and nota <= 8.9:
        conceito = 'C'
    elif nota >= 9 and nota <= 10:
        conceito = 'B'
    else:
        conceito = 'VALORES INFORMADOS SÃO INVÁLIDOS'

print(f'O conceito do aluno é {conceito}')

# funcionou


# 35 - valida a data

dia = int(input('Informe o dia para validação: '))
mes = int(input('Informe o mês para validação: '))
ano = int(input('Informe o ano para validação: '))

if ((ano % 400 == 0) or (ano % 4 == 0)) and (ano % 100 != 0):
    bis = True
else:
    bis = False

if mes in (1, 3, 5, 7, 8, 10, 12) and dia <= 31:
    mesv = True
    diav = True
elif mes == 2:
    mesv = True
    if (bis == True and dia <= 29) or (bis == False and dia <= 28):
        diav = True
    else:
        diav = False
elif mes in (4, 6, 9, 11) and dia <= 30:
    mesv = True
    diav = True
else:
    mesv = False
    diav = False

if diav == True and mesv == True:
    print(f'A data informada {dia}/{mes}/{ano} é válida!')
else:
    print(f'A data informada {dia}/{mes}/{ano} é inválida!')

# funcionou

# 36 - lê a venda, calcula e imprime a comissão

venda = float(input('Informe o valor da venda R$ '))

if venda >= 100000:
    comissao = (700 + (venda * 16 / 100))
elif venda < 100000 and venda >= 80000:
    comissao = (650 + (venda * 14 / 100))
elif venda < 80000 and venda >= 60000:
    comissao = (600 + (venda * 14 / 100))
elif venda < 60000 and venda >= 40000:
    comissao = (550 + (venda * 14 / 100))
elif venda < 40000 and venda >= 20000:
    comissao = (500 + (venda * 14 / 100))
elif venda < 20000 and venda >= 0:
    comissao = (400 + (venda * 14 / 100))
else:
    print(f'Valor de venda deve ser maior que R$ 0')
    exit()

print(f'O valor da comissão é R$ {comissao}')

# funcionou]


# 37 - estacionamento

cheg = input('Informe a hora de entrada hh:mm: ')
sai = input('Informe a hora de saída hh:mm: ')

hcheg,mcheg = cheg.split(":")
hsai,msai = sai.split(":")

hcheg = int(hcheg)
mcheg = int(mcheg)
hsai = int(hsai)
msai = int(msai)
tempoh = 0
tempom = 0

# calculo do tempo de estacionamento
if hcheg < hsai:
    tempoh = hsai - hcheg
    if mcheg < msai:
        tempoh = tempoh + 1
elif hcheg > hsai:
    tempoh = 24 - (hcheg - hsai)
    if mcheg < msai:
        tempoh = tempoh + 1
elif hcheg == hsai and mcheg >= msai:
    tempoh = 24
elif hcheg == hsai and mcheg < msai:
    tempoh = 1

# calculo do valor cobrado
if tempoh < 3:
    pagar = (tempoh * 1)
elif tempoh >= 3 and tempoh < 5:
    pagar = (tempoh - 2) * 1.4 + 2
else:
    pagar = (tempoh - 4) * 2 + 4.8

print(f'O tempo estacionado foi de {tempoh} horas e o valor a pagar é R$ {pagar:.2f}')

# funcionou


# 38 - informa uma data e testa a validade dela.

datanasc = input('Informe a data de nascimento para validação no formato dd/mm/aaaa: ')
datavalidar = datanasc.split("/")

if len(datavalidar) != 3:
    print('Data informada inválida, informe no padrão correto!')
    exit()

dia = int(datavalidar[0])
mes = int(datavalidar[1])
ano = int(datavalidar[2])

if ano > 2022:
    anov = False
else:
    anov = True

if ((ano % 400 == 0) or (ano % 4 == 0)) and (ano % 100 != 0):
    bis = True
else:
    bis = False

if mes in (1, 3, 5, 7, 8, 10, 12) and dia <= 31:
    mesv = True
    diav = True
elif mes == 2:
    mesv = True
    if (bis == True and dia <= 29) or (bis == False and dia <= 28):
        diav = True
    else:
        diav = False
elif mes in (4, 6, 9, 11) and dia <= 30:
    mesv = True
    diav = True
else:
    mesv = False
    diav = False

if diav == True and mesv == True and anov == True:
    print(f'A data informada {dia}/{mes}/{ano} é válida!')
else:
    print(f'A data informada {dia}/{mes}/{ano} é inválida!')

# funcionou


# 39 - calculo de aumento de salário e bônus

salatual = float(input('Informe o salário atual R$ '))
temposerv = int(input('Informe o tempo de serviço: '))

if salatual <= 500:
    reaj = 25
elif salatual > 500 and salatual <= 1000:
    reaj = 20
elif salatual > 1000 and salatual <= 1500:
    reaj = 15
elif salatual > 1500 and salatual <= 2000:
    reaj = 10
else:
    reaj = 0

if temposerv < 1:
    bonus = 0
elif temposerv >= 1 and temposerv <= 3:
    bonus = 100
elif temposerv >= 4 and temposerv <= 6:
    bonus = 200
elif temposerv >= 7 and temposerv <= 10:
    bonus = 300
else:
    bonus = 500

salnovo = salatual + (salatual * reaj / 100) + bonus

if salnovo == salatual:
    print(f'O funcionário não tem direito a aumento!')
else:
    print(f'O novo salário é R$ {salnovo:.2f}')


# 40 - Cálculo do custo de um carro novo

custofab = float(input('Informe o custo de fábrica do veículo R$ '))

if custofab <= 12000:
    com = 5
    imposto = 0
elif custofab > 12000 and custofab <= 25000:
    com = 10
    imposto = 15
else:
    com = 15
    imposto = 20

custo = custofab + (custofab * com / 100) + (custofab * imposto / 100)

print(f'O custo ao consumidor do veículo é R$ {custo:.2f}')

# funcionou


# 41 - calculo do IMC

peso = float(input('Informe o peso em kg: '))
altura = float(input('Informe a altura em mt: '))
imc = peso / (altura * altura)

if imc <= 18.5:
    msg = 'Abaixo do peso'
elif imc >= 18.6 and imc <= 24.9:
    msg = 'Saudável'
elif imc >= 25 and imc <= 29.9:
    msg = 'Peso em excesso'
elif imc >= 30 and imc <= 34.9:
    msg = 'Obesidade Grau I'
elif imc >= 35 and imc <= 39.9:
    msg = 'Obesidade Grau II (severa)'
else:
    msg = 'Obesidade Grau III (mórbida)'

print(f'O IMC é {imc:.1f} - {msg}')

# funcionou

"""