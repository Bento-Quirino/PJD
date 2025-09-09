# IF-ELSE é uma instrução que serve para verificar se uma condição é verdadeira
# e executar um bloco de código baseado nessa verificação

# Exemplo: verifique se um valor informado pelo usuário é positivo ou negativo

valor = int(input(""))

if valor >= 0:
  print("valor digitado é positivo")
else:
  print("valor digitado é negativo")

# No exemplo, "valor >= 0" é a condição verificada.
# É possível ler a instrução como uma pergunta:
# "o valor é maior ou igual a zero?"
#  - Se sim, execute o código abaixo do "if"
#  - Se não, execute o código abaixo do "else"

# O "else" pode ser opcional, dependendo do problema ele será necessário ou não.
# exemplo:
if valor < 0:
  print("valor digitado é negativo")
  print("transformando ele em positivo")
  valor = valor * -1
