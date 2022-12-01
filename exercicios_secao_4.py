"""
Exercicios seção 4

# exercicio 1 - programa para ler numero inteiro e imprimir

numero = int(input('Informe o número inteiro para imprimir '))
print(f'o número informado é {numero}')
print(type(numero))
# funcionou


# exercicio 2 - programa para ler o numero real e imprimir

numreal = complex(input('Informe o número inteiro para imprimir '))
print(f'o número informado é {numreal}')
print(type(numreal))
# funcionou


# exercicio 3 - insira 3 valores inteiros e imprima a soma deles

int1 = int(input('Informe o primeiro número inteiro: '))
int2 = int(input('Informe o segundo número inteiro: '))
int3 = int(input('Informe o terceiro número inteiro: '))
print(f'A soma dos três números informados é {int1 + int2 + int3}')
# funcionou


# exercício 4 - informe um número real e imprime o seu quadrado

numReal = complex(input('Informe um número real: '))
print(f'O quadrado do número informado é {numReal ** 2}')
# funcionou


# exercicio 5 - informe um número real e imprima a quinta parte desse número

numReal = float(input('Informe um número real: '))
print(f'A quinta parte do número informado é {numReal / 5}')
# funcionou


# exercicio 6 - conversão de temperatura de Celsius para Farenheit

tempcelsius = float(input('Informe a temperatura em Graus Celsius: '))
tempfarenheit = tempcelsius * (9.0/5.0)+32.0
print(f'A temperatura convertida em Graus Farenheit é {tempfarenheit}')
# funcionou


# exercicio 7 - conversão de temperatura de Farenheit para Celsius

tempfarenheit = float(input('Informe a temperatura em Graus Farenheit: '))
tempcelsius = 5.0 * (tempfarenheit - 32.0) / 9.0
print(f'A temperatura convertida em Graus Celsius é {tempcelsius}')
# funcionou


# exercicio 8 - conversão de temperatura de Kelvin para Celsius

tempkelvin = float(input('Informe a temperatura em Graus Kelvin: '))
tempcelsius = tempkelvin - 273.15
print(f'A temperatura convertida em Graus Celsius é {tempcelsius}')
# funcionou


# exercicio 9 - conversão de temperatura de Celsius para Kelvin

tempcelsius = float(input('Informe a temperatura em Graus Celsius: '))
tempkelvin = tempcelsius + 273.15
print(f'A temperatura convertida em Graus Kelvin é {tempkelvin}')
# funcionou


# exercício 10 - converter de km/h para m/s

velkm = float(input('Informe a velocidade em km/h: '))
velm = velkm / 3.6
print(f'A velocidade convertida em m/s é {velm}')
# funcionou


# exercício 11 - converter de m/s para km/h

velm = float(input('Informe a velocidade em m/s: '))
velkm = velm * 3.6
print(f'A velocidade convertida em km/h é {velkm}')
# funcionou


# exercício 12 - converter distância de milhas para km

distm = float(input('Informe a distância em milhas: '))
distkm = 1.61 * distm
print(f'A distância convertida em km é {distkm}')
# funcionou


# exercício 13 - converter distância de km para milhas

distkm = float(input('Informe a distância em km: '))
distm = distkm / 1.61
print(f'A distância convertida em milhas é {distm}')
# funcionou


# exercício 14 - converter ângulos de graus para radianos

graus = float(input('Informe o ângulo em graus: '))
rad = graus * (3.14 / 180)
print(f'O valor do ângulo em radianos é {rad}')
# funcionou


# exercício 15 - converter ângulos de radianos para graus

rad = float(input('Informe o ângulo em radianos: '))
graus = rad * (180 / 3.14)
print(f'O valor do ângulo em graus é {graus}')
# funcionou


# exercício 16 - converter comprimento de polegada para centímetro

pol = float(input('Informe o comprimento em polegadas: '))
cent = pol * 2.54
print(f'O valor do comprimento em centímetros é {cent}')
# funcionou


# exercício 17 - converter comprimento de centímetro para polegada

cent = float(input('Informe o comprimento em centímetros: '))
pol = cent / 2.54
print(f'O valor do comprimento em polegadas é {pol}')
# funcionou


# exercício 18 - converter volume de metros cúbicos para litros

volm3 = float(input('Informe o volume em metros cúbicos m³: '))
vollt = 1000 * volm3
print(f'O volume em litros é {vollt}')
# funcionou


# exercício 19 - converter volume de litros para metros cúbicos

vollt = float(input('Informe o volume em litros: '))
volm3 = vollt / 1000
print(f'O volume em metros cúbicos é {volm3}')
# funcionou


# exercício 20 - converter massa de quilogramas para libras

massakg = float(input('Informe a massa em quilogramas: '))
massalb = massakg / 0.45
print(f'A massa em libras é {massalb}')
# funcionou


# exercício 21 - converter massa de libras para quilogramas

massalb = float(input('Informe a massa em libras: '))
massakg = massalb * 0.45
print(f'A massa em quilogramas é {massakg}')
# funcionou


# exercício 22 - converter comprimento de jardas para metros

compjar = float(input('Informe o comprimento em jardas: '))
compmt = 0.91 * compjar
print(f'O comprimento em metros é {compmt}')
# funcionou


# exercício 23 - converter comprimento de metros para jardas

compmt = float(input('Informe o comprimento em metros: '))
compjar = compmt / 0.91
print(f'O comprimento em jardas é {compjar}')
# funcionou


# exercício 24 - converter área de metros quadrados para acres

aream2 = float(input('Informe a área em metros quadrados: '))
areaacres = aream2 * 0.000247
print(f'A área em acres é {areaacres}')
# funcionou


# exercício 25 - converter área de acres para metros quadrados

areaacres = float(input('Informe a área em acres: '))
aream2 = areaacres * 4048.58
print(f'A área em metros quadrados é {aream2}')
# funcionou


# exercício 26 - converter área de metros quadrados para hectares

aream2 = float(input('Informe a área em metros quadrados: '))
areahec = aream2 * 0.0001
print(f'A área em hectares é {areahec}')
# funcionou


# exercício 27 - converter área de hectares para metros quadrados

areahec = float(input('Informe a área em hectares: '))
aream2 = areahec * 10000
print(f'A área em metros quadrados é {aream2}')
# funcionou


# exercicio 28 - cálculo da soma dos quadrados de três valores

v1 = float(input('Informe o primeiro valor: '))
v2 = float(input('Informe o segundo valor: '))
v3 = float(input('Informe o terceiro valor: '))
res = (v1 ** 2) + (v2 ** 2) + (v3 ** 2)
print(f'A soma dos quadrados dos números {v1}, {v2} e {v3} é {res}')
# funcionou


# exercício 29 - cálculo da média aritmética de 4 notas

nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
nota3 = float(input('Informe a terceira nota: '))
nota4 = float(input('Informe a quarta nota: '))
res = (nota1 + nota2 + nota3 + nota4) / 4
print(f'A média das notas {nota1}, {nota2}, {nota3}, {nota4} é {res}')
# funcionou


# exercício 30 - conversão de real para dólar

real = float(input('Informe o valor em reais para ser convertido para dólares R$ '))
cotacao = float(input('Informe a cotação do dólar R$ '))
print(f'O valor em dólares é US$ {real / cotacao}')
# funcionou


# exercício 31 - ler um número inteiro e imprimir seu antecessor e sucessor

numero = int(input('Informe um número inteiro: '))
print(f'O antecessor do número {numero} é {numero - 1} e o sucessor é {numero + 1}')
# funcionou


# exercício 32 - ler um número inteiro e imprimir a soma do sucessor do seu triplo com o antecessor do seu dobro

numero = int(input('Informe um número inteiro: '))
res = (numero * 3 + 1) + (numero * 2 - 1)
print(f'A soma do sucessor do seu triplo com o antecessor do seu dobro é {res}')
# funcionou


# exercício 33 - calculo da área do quadrado

lado = int(input('Informe o tamanho do lado do quadrado: '))
print(f'A área do quadrado é {lado ** 2}')
# funcionou


# exercício 34 - calculo da área do círculo

raio = float(input('Informe o raio do círculo: '))
res = 3.141592 * (raio ** 2)
print(f'A área do círculo é {res}')
# funcionou


# exercício 35 - Cálculo da hipotenusa

a = float(input('Informe o cateto A do triângulo: '))
b = float(input('Informe o cateto B do triângulo: '))
hip = ((a ** 2)+(b ** 2)) ** 0.5
print(f'A hipotenusa mede {hip}')
# funcionou


# exercício 36 - cálculo do volume do cilindro circular

raio = float(input('Informe o raio do cilindro: '))
altura = float(input('Informe a altura do cilindro: '))
volume = 3.141592 * (raio ** 2) * altura
print(f'O volume do cilindro é {volume}')
# funcionou


# exercício 37 - leia um produto e imprima o valor com desconto de 12%

valor = float(input('Informe o valor do produto R$ '))
print(f'O valor do produto com desconto de 12% é {valor - (valor * 0.12)}')
# funcionou


# exercício 38 - leia o salário do funcionário e calcule o novo salário com aumento de 25%

salario = float(input('Informe o salário atual do empregado: '))
print(f'O novo salário do empregado será {salario + (salario * 0.25)}')
# funcionou


# exercício 39 - ler uma quantia e dividir entre 3 ganhadores

premio = float(input('Informe o valor do premio R$ '))
ganhador1 = premio * 0.46
ganhador2 = premio * 0.32
ganhador3 = premio - ganhador1 - ganhador2
print(f'O premio será dividido da seguinte forma: \n Ganhador 1 recebe {ganhador1} \n Ganhador 2 recebe {ganhador2} \n
Ganhador 3 recebe {ganhador3}')
# funcionou

# exercício 40 - calculo do pagamento líquido para encanador que recebe 30,00 por dia descontando 8% para imposto renda

diarias = int(input('Informe a quantidade de diarias: '))
calculo = (30 - (30 * 0.08)) * diarias
print(f'O valor líquido para pagamento do encanador pelas {diarias} diárias é R$ {calculo}')
# funcionou


# exercicio 41 - ler valor da hora, horas trabalhadas calcular o valor a ser pago + 10%

valorhora = float(input('Informe o valor da hora a ser pago R$: '))
qtdhoras = int(input('Informe a quantidade de horas trabalhadas no mês: '))
valor = (valorhora * qtdhoras)
valor = valor + (valor * 0.1)
print(f'O valor a ser pago ao funcionário é R$ {valor}')
# funcionou


# exercício 42 - recebe salário base, calcula gratificação, calcula imposto e calcula salário a receber

salbase = float(input('Informe o salário base R$: '))
gratificacao = salbase * 0.05
imposto = salbase * 0.07
salreceber = salbase + gratificacao - imposto
print(f'O salário a receber é R$ {salreceber}')
# funcionou


# exercício 43 - ajuda dos vendedores:

valorvenda = float(input('Informe o valor do produto R$: ')) # valor da venda parcelada
valorvista = valorvenda - (valorvenda * 0.1) # calcula o valor a pagar com 10% desconto
valorparcela = valorvenda / 3 # calcula o valor da parcela em 3x sem juros
comissaovista = valorvista * 0.05 # calcula comissão de 5% do valor a vista
comissaoparcela = valorvenda * 0.05 # calcula comissão de 5% do valor total
print(f'O valor para pagamento à vista com 10% de desconto é R$ {valorvista} \n'
      f'O valor de cada parcela em 3x sem juros é R$ {valorparcela} \n'
      f'A comissão do vendedor à vista é R$ {comissaovista} \n'
      f'A comissão do vendedor na venda parcelada é R$ {comissaoparcela}') # impressão na tela
# funcionou


# exercício 44 - recebe a altura do degrau e a altura desejada e calcula a quantidade de degraus

altdegrau = float(input('Informe a altura de cada degrau da escada em centímetros: '))
altsubida = float(input('Informe a altura desejada em metros: '))
qtddegraus = (altsubida * 100) / altdegrau
print(f'A quantidade de degraus necessária é {qtddegraus}')
# funcionou


# exercício 45 - converte uma letra maiúscula em minuscula usando a tabela ASCII

letMai = input('Digite uma letra em maisculo: ')
ordAsciiMa = ord(letMai)
ordAsciiMi = ord(letMai) + 32
LetMi = chr(ordAsciiMi)
print(f"A letra em misculo é: {LetMi}")
# funcionou


# exercício 46 - recebe um número inteiro de 3 dígitos e retorna ele invertido

numint = int(input('Insira um número inteiro entre 100 e 999: '))
if numint >= 100 and numint <= 999:
    var = str(numint)
    print(f'O número invertido é {var[::-1]}')
else: print('Esse número não é válido')
# funcionou

# exercício 47 - recebe um número de 4 dígitos e imprime 1 dígito por linha

numint = int(input('Insira um número inteiro de 4 dígitos de 1000 a 9999: '))
if numint >= 1000 and numint <= 9999:
    var = str(numint)
    print('O número inserido é: ')
    print(var[0])
    print(var[1])
    print(var[2])
    print(var[3])
else: print('O número inserido não é válido!')
# funcionou


# exercício 48 - recebe um valor inteiro em segundos e converte em horas, minutos e segundos

converter = int(input('Insira um valor em segundos para converter: '))
horas = int(converter / 3600)
minutos = int(((converter % 3600) * 60) / 3600)
segundos = int((((converter % 3600) * 60) % 3600) / 60)
print(f'O total convertido é {horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s)')
# funcionou

# exercício 49 - recebe o horário de início de uma experiência e sua duração e retorna o horário final

iniciohora = int(input('Informe a hora de início: '))
iniciominuto = int(input('Informe os minutos de início: '))
iniciosegundo = int(input('Informe os segundos de início: '))
duracao = int(input('Informe o tempo em segundos de duração da experiência: '))

resultado = (iniciohora * 3600) + (iniciominuto * 60) + (iniciosegundo) + duracao

horas = int(resultado / 3600)
minutos = int(((resultado % 3600) * 60) / 3600)
segundos = int((((resultado % 3600) * 60) % 3600) / 60)

print(f'O horário de término da experiência é: {horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s)')
# funcionou


# exercicio 50 - calcula o ano de nascimento a partir da sua idade e ano atual

idade = int(input('Informe a sua idade em anos: '))
anoatual = int(input('Informe o ano atual: '))
result = anoatual - idade
print(f'O ano de nascimento é {result}')
# funcionou


# exercício 51 - calcula a distância entre um ponto e a origem (0,0) no gráfico cartesiano

x1 = int(input('Informe a coordenada X: '))
y1 = int(input('Informe a coordenada Y: '))
distancia = ((x1 ** 2) + (y1 ** 2)) ** (1/2)
print(f'A distância é entre os pontos {x1}, {y1} e a origem é {distancia}')
# funcionou


# exercício 52 - calcula o prêmio de cada um dos 3 apostadores baseados no valor investido de cada um

ap1 = float(input('Informe o valor investido pelo Apostador 1 R$ '))
ap2 = float(input('Informe o valor investido pelo Apostador 2 R$ '))
ap3 = float(input('Informe o valor investido pelo Apostador 3 R$ '))
premio = float(input('Informe o valor do prêmio da loteria R$ '))
totalap = ap1 + ap2 + ap3
perc1 = ap1 / totalap * 100
perc2 = ap2 / totalap * 100
perc3 = ap3 / totalap * 100
premioap1 = premio * perc1 / 100
premioap2 = premio * perc2 / 100
premioap3 = premio * perc3 / 100
print(f'O premio do apostador 1 é R$ {premioap1}')
print(f'O premio do apostador 2 é R$ {premioap2}')
print(f'O premio do apostador 3 é R$ {premioap3}')
# funcionou

# exercicio 53 - calcule o valor para cercar um terreno informando a largura, comprimento e o valor do metro da tela

comp = float(input('Informe o comprimento do terreno: '))
larg = float(input('Informe a largura do terreno: '))
tela = float(input('Informe o valor do metro da tela R$ '))
custo = ((2 * comp) + (2 * larg)) * tela
print(f'O custo total da tela é R$ {custo}')
# funcionou

"""