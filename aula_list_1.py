# Estrutura de dados: Array/List
# Estrutura de dados é um método de organizar e manipular dados em um computador
# Python não tem array de forma direta. A estrutura que substitui o array no Python é o List.

# No Super Mario World, existe apenas um slot de item, portanto, apenas uma variável
# serve para guardar o valor do item do jogador.
mushroom = "get_taller"

# Há situações em que é necessário guardar mais de um valor ao mesmo tempo, numa mesma variável.
# Uma forma é usar uma variável do tipo List.
# Ela permite criar uma sequência de valores em uma só variável, ao mesmo tempo.

# declarando uma variável List de nome 'hot_bar'.
hot_bar = [] #é possível saber que se trata de um List pela presença dos colchetes
# inicializando um 'List', ou seja, atribuindo um valor a ele
hot_bar = [50, "picareta", True, "dinamite"]

# Para acessar um elemento dentro de um list é necessário usar '[]' (colchetes) logo depois de seu nome.
# Dentro do colchetes é preciso informar o índice do elemento desejado.
# O índice é SEMPRE baseado em zero, ou seja, conta-se a partir do primeiro elementos, considerando-o como zero.

# Podemos acessar um elemento para ler/usar o valor
print(hot_bar[1]) # acessando e exibindo o valor
print(hot_bar[0] + 20) # acessando, lendo, fazendo uma conta e exibindo o resultado

# Ou podemos acessar um elemento para modificar o valor presente nele
hot_bar[2] = "água" # trocando o valor 'True' por '"água"'

# Índices positivos 'andam' pelo list da esquerda para a direita
# Índices negativos 'andam' pelo list da direita para a esquerda
# Nesse caso, será exibido '"água"', porque voltando dois índices a partir do zero, cai nele
print(hot_bar[-2])

# NÃO É POSSÍVEL acessar um índice INEXISTENTE, portanto a linha abaixo gera erro e não compilar/interpreta
#print(hot_bar[10])

# Podemos saber o tamanho do List, ou seja, a quantidade de elementos que ele armazena
# através da função 'len()'
print(f"numero de elementos: {len(hot_bar)}")

# Podemos também zerar o List, remover todos os elementos armazenados, e deixa-lo vazio
# usando a função clear()
hot_bar.clear()
print(f"numero de elementos: {len(hot_bar)}") # exibe zero porque esvaziamos o List
