# Considerando que você esteja desenvolvendo um sistema de cálculo de datas,
# escreva um trecho de código em que o usuário informe o valor de um ano,
# e o código deve exibir no console se esse ano é bissexto ou não.

# Para facilitar, podemos quebrar a prblema em partes:

# (...) usuário informe o valor de um ano
year = int(input("Digite o ano desejado:"))

# (...) ano é bissexto ou não
# para um ano ser bissexto, ele deve ser divisível por 4 ou por 400
# na divisão de inteiros isso representa que se um número for divisível por 4
# o resto será zero, se ele NÃO for divisível por 4, o resto será diferente de zero
bissexto = (year % 4) == 0 or (year % 400) == 0

# (...) exibir no console
if bissexto:
  print("o ano digitado é bissexto")
else:
  print("o ano digitado não é bissexto")

# OUTRA FORMA DE RESOLVER

if (year % 4) == 0 or (year % 400) == 0:
  print("o ano digitado é bissexto")
else:
  print("o ano digitado não é bissexto")

# OBS: "%" é o operador 'resto da divisão', e retorna o valor do resto da divisão entre dois números
# por exemplo "5 % 2" retorna 1, pois 1 é o resto da divisão de inteiros entre 5 e 2.
  
# Seguindo o problema, se "year" tiver valor 1995, por exemplo, será feito "1995 % 4", que retorna 3.
# Logo em seguida é verificado "3 == 0", ou seja, o resultado do resto da divisão, 3, é igual a zero?
# como não é, essa parte da condiçao é falsa, e o mesmo se repetiria para "1995 % 400"
