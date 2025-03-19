# Valor é qualquer tipo de dados ou informação. Por exemplo:
#   * "Jorge" é o valor de um nome de uma pessoas;
#   * 16 anos é  valor de idade de uma pessoa;
#   * 100km é o valor da velocidade de um carro

# Para guardar qualquer valor, um código depende de dois tipos de estruturas: variáveis e constantes.
# Constante é uma estrutura cujo o valor armazenado nunca muda ao longo da execução de um código. Por exemplo:
# * pi - o seu valor, 3.14, nunca muda, e se mudar, não é mais será mais pi

# Variável é uma estrutura cujo o valor armazenado PODE mudar ao longo da execução de um código

# No Python, para se declarar uma variável basta dizer o nome dela.
# Ao declarar uma variável, informamos ao computador que ela existe e que ela pode guardar um valor
life # delcaração

# Para inicializar uma variável declaramos o nome dela e atribuimos um valor inicial a ela
life = 100 # inicialização
name = "Jorge" # inicialização

# Variáveis e valores, dependendo das linguagens podem ter tipos de valor. Existem 4 maneiras de uma linguagem de programação lidar com variáveis e valores: 

# tipos de variáveis
# * tipo dinâmico: uma variável pode armazenar tipos de valores diferentes ao longo do código (Python, JavaScript)
# * tipo estático: uma variável armazenará apenas valores de um tipo, ao longo do código (C++, Java, C#)

# tipos de valores:
# * tipo fraco: um valor pode ser interpretado em mais de um tipo, e, portanto, no geral, ele não tem tipo fixo (JavaScript, C)
# * tipo forte: todo valor tem um tipo bem definido e fixo, e só pode interagir com tipos compatíveis (C++, Python, Java)

# Python é uma linguagem de tipagem dinâmica forte. Significa que cada valor tem um tipo bem definido e fixo,
# mas as variáveis podem mudar o tipo de valor que guardam
ammo = 25 # valor de tipo inteiro
print(type(ammo))
ammo = "25" # valor de tipo string
print(type(ammo))
