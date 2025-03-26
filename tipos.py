# No Python os VALORES possuem um tipo forte e bem definido
# Existem três principais tipos primitivos

# bool (booleano):
# tipo de valor lógico, possui apenas dois valores possíveis, true e false
numero_par = True

# int (inteiro):
# tipo de valor numérico inteiro, por exemplo 1, 2, 9, -20, -328
idade = 125

# float (ponto flutuante):
# tipo de valor numérico real, números com vírgula, como 1.5, 8.1, -987.0024
preco = 84.25
        
# str/string (texto/cadeia de caracteres):
# tipo de valor textual, identificado por aspas, por exemplo "João", "65.725", "e"
nome = "Beniverson"

# CUIDADO
# No Python, operações só podem ser feitas com tipos de valores compatíveis,
# por exemplo "50" + 10 não é uma operação válida, porque não é possível somar um texto com um número,
# matematicamente não faz sentido, e textualmente um texto só pode ser juntado com outro texto

# soluções
# 1)
valor1 = "50"
valor2 = 10
resultado = int(valor1) + valor2 # operação matemática de soma

# 2)
valor1 = "50"
valor2 = 10
resultado = valor1 + str(valor2) # operação de concatenação, emenda dois texto em um

# CUIDADO 2
# "asd" + 10 só é possível na segunda solução, pois LETRAS NÃO SÃO CONVERSÍVEIS para números

