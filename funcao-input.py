# a função input() solicita que o usuário digite algo no console
# tudo o que o usuário digita através da função input() é interpretado como string
# a linha abaixo lê o ano informado como texto
# year = input("Digite o ano desejado:")

# a linha abaixo lê o ano informado como texto
# MAS CONVERTE o texto em número (int, número inteiro)
year = int(input("Digite o ano desejado:"))

print(f"o ano digitado foi: {year}")
