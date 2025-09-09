# Estruturas de execução de código condicionam um código a executar de uma maneira específica
# FOR é uma estrutura de repetição de código. Em linhas gerais, ele permite que um bloco de código
# execute repetidamente enquanto uma condição é satisfeita.
# Cada linguagem, em geral, pode apresentar formas diferentes de usar o 'for,
# mas no geral elas seguem o seguinte padrão.
# for<inicialização da variável de controle>; <condição para repetição>; <incremento>
#   <código>

# Em Python, esse padrão é escrito da seguinte forma:
#for i in <condição para repetição>:
#  <código>

# Um exemplo prático em Python é fazer uma contagem. Nesse caso,
# podemos usar a função 'range()' para determinar o valor inicial e o final dessa contagem.
# No exemplo abaixo, a variável de controle 'i' serve para contar o número de repetições efetuadas.
for i in range(0, 10):
  print(i)

# No exemplo acima, 'i' aumenta de 1 em 1. Mas é possível aumentar esse incremento.
# Abaixo, 'i' aumenta de 2 em 2
for i in range(0, 10, 2):
  print(i)

# Você pode se perguntar aonde estão a inicialização e a condição de repetição. Na verdade, elas estão implicitas.
# Os valores dentro do 'range' que determinam isso:
# O primeiro valor é de onde 'i' irá COMEÇAR;
# O segundo valor é o LIMITE que 'i' pode atingir, ou seja, REPETIRÁ ENQUANTO 'i' NÃO CHEGAR NELE;
# O último valor, se informado é o incremento, de quanto em quanto é feita essa contagem.

# Geralmente, quando estudamos 'for', sempre o vemos associado a arrays ou listas.
# Isso porque podemos usar a variável de controle, o contador de repetição, para acessar os índices de um array.
# Portanto, o seguinte ALGORITMO é válido e muito comum em diversas linguagens:

arr = [] # uma lista qualquer
for i in range(0, len(arr)):
  print(arr[i])

# Usamos o 'len' para pegar o numero de elementos da lista. Definimos esse número como o limite de repetição
# e usamos 'i' para iterar sobre a lista.
# Iterar significa andar e acessar todos os índices de uma estrutura de dados, como arrays ou listas.
